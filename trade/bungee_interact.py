import sys
from web3 import Web3
from enum import Enum

INFURA_SECRET_KEY = '7a99188377d641cf8bba51559b9ed4d9'

class Network_name(Enum): 
 ETH_MAINNET = 'mainnet'
 ROPSTEN = 'ropsten'
 RINKEBY = 'rinkeby'
 OP_MAINNET = 'optimism-mainnet'
 AR_MAINNET = 'arbitrum-mainnet'
 AR_RINKEBY = 'arbitrum-rinkeby'

def get_network_name_by_chainid(chainid):
    if(chainid == 1): 
        network = Network_name.ETH_MAINNET;
    elif(chainid == 3):
        network = Network_name.ROPSTEN;
    elif(chainid == 4):
        network = Network_name.RINKEBY;
    elif(chainid == 10):
        network = Network_name.OP_MAINNET;
    elif(chainid == 42161):
        network = Network_name.AR_MAINNET;
    else:
        network = Network_name.ETH_MAINNET;

    return network.value

# get w3 endpoint by network name
def get_w3_by_network(chainid=1):
    network = get_network_name_by_chainid(chainid)
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3

def eth_addr_parse_from_file(filename):
  with open(filename, 'r') as f:
    entry_num=0
    while True:
      lines = f.readline().strip() 
      if not lines:
        return
      
      eth_address, temp_str = lines.split()
      eth_value = float(temp_str)
      if (len(eth_address) != 42):  return # len need to take into "0x"
      if (eth_address[:2] != '0x'): return
      if (eth_value <= 0): return
      if (eth_value >= 3): return          # only support small number transfer

      yield eth_address, eth_value

def parse_private_key_from_addr(eth_address):
  
  filename = 'private_key.txt'
  with open(filename, 'r') as f:
    entry_num=0
    while True:
      lines = f.readline().strip() 
      if not lines:
        return None
      
      temp_addr, temp_str = lines.split()
      if (len(eth_address) != 42):   return None # len need to take into "0x"
      if (eth_address[:2] != '0x'):  return None
      if (eth_address == temp_addr): return temp_str

def bungee_refeul(chainId, from_addr, destChainId, contract_addr, amount_in_eth):
  w3 = get_w3_by_network(chainId)
  if not w3.isConnected():
    return

  contract_addr = Web3.toChecksumAddress(contract_addr)
  print('Interact with contract ' + contract_addr)

  # get private key
  from_addr = Web3.toChecksumAddress(from_addr)
  print(from_addr)
  private_key = parse_private_key_from_addr(from_addr)
  print(private_key)

  ABI = '[{"inputs":[{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"depositNativeToken","outputs":[],"stateMutability":"payable","type":"function"}]'

  contract = w3.eth.contract(address=contract_addr, abi=ABI)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  #get decimals to multiply by token amount
  amount = w3.toWei(amount_in_eth, 'ether')
  if (w3.eth.get_balance(from_addr) < amount):
    return {'status': 'failed', 'error': 'insufficient balance', 'task': 'bungee refuel'}

  params = {
      'chainId': chainId, 
      'nonce': nonce,
      'gas': 2000000,
      'gasPrice': gas_price,
      'value': amount,
  }

  func = contract.functions.depositNativeToken(destChainId, from_addr)
  #sign the transaction
  try:
    tx = func.buildTransaction(params)
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return {'status': 'success', 'txn_hash': w3.toHex(txn), 'task': 'Transfer'}
  except Exception as e:
    return {'status': 'failed', 'error': e, 'task': 'Transfer'}

if __name__ == "__main__":

    # Optimism chain to Arbitrum chain 
    srcChainId = 10 # optimism
    destChainId = 42161 #arbitrum

    # bungee exchange refeul module(from optimism)
    contract_addr   = '0x5800249621DA520aDFdCa16da20d8A5Fc0f814d8'

    # optimism chainId is 42161
    filename = 'account.txt'
    for from_addr, amount_in_eth in eth_addr_parse_from_file(filename):
      result = bungee_refeul(srcChainId, from_addr, destChainId, contract_addr, amount_in_eth)
      if (result['status'] == 'failed'): print(result)

