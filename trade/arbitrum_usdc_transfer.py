import sys
from web3 import Web3
from enum import Enum
from dynaconf import settings

INFURA_SECRET_KEY = settings.INFURA_PROJECT_ID

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
    print(INFURA_SECRET_KEY)
    return
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

def arbitrum_usdc_transfer(chainId, from_addr, to_addr, contract_addr, amount_in_eth):
  w3 = get_w3_by_network(chainId)
  if not w3.isConnected():
    return

  from_addr = Web3.toChecksumAddress(from_addr)
  to_addr = Web3.toChecksumAddress(to_addr)
  contract_addr = Web3.toChecksumAddress(contract_addr)
  print('Interact with contract ' + contract_addr)

  # get private key
  private_key = parse_private_key_from_addr(from_addr)

  ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":true,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
  contract = w3.eth.contract(address=contract_addr, abi=ABI)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  params = {
      'chainId': chainId, 
      'nonce': nonce,
      'gas': 2000000,
      'gasPrice': gas_price,
  }

  # get name from contract
  name = contract.functions.name().call()
  #get decimals to multiply by token amount
  d = contract.functions.decimals().call()
  amount = amount_in_eth * 10**d
  if(contract.functions.balanceOf(from_addr).call() < amount):
    return {'status': 'failed', 'error': 'insufficient balance', 'task': 'arbitrum USDC transfer'}

  func = contract.functions.transfer(to_addr, int(amount))
  #sign the transaction
  try:
    tx = func.buildTransaction(params)
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    ret_string = 'Transfer ' + name
    return {'status': 'success', 'txn_hash': w3.toHex(txn), 'task': ret_string}
  except Exception as e:
    return {'status': 'failed', 'error': e, 'task': ret_string}

if __name__ == "__main__":

    # USDC transfer on arbitrum chain
    # arbiturm chain
    chainId = 42161
    # USDC contract address on arbitrum
    contract_addr   = '0xff970a61a04b1ca14834a43f5de4533ebddb5cc8'
     
    # USDC transfer from source to destination address
    from_addr = Web3.toChecksumAddress(sys.argv[1])
    to_addr   = Web3.toChecksumAddress(sys.argv[2])

    amount_in_eth = 0.44

    # arbitrum chainId is 42161
    result = arbitrum_usdc_transfer(chainId, from_addr, to_addr, contract_addr, amount_in_eth)
    print(result)

