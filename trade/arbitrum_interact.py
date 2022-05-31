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

def arbitrum_depositEth(chainId, from_addr, contract_addr, amount_in_eth):
  w3 = get_w3_by_network(chainId)
  if not w3.isConnected():
    return

  from_addr = Web3.toChecksumAddress(from_addr)
  contract_addr = Web3.toChecksumAddress(contract_addr)

  # get private key
  private_key = parse_private_key_from_addr(from_addr)

  ABI = '[{"inputs":[{"internalType":"uint256","name":"maxSubmissionCost","type":"uint256"}],"name":"depositEth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"}]'
  contract = w3.eth.contract(address=contract_addr, abi=ABI)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  amount_in_wei = w3.toWei(amount_in_eth, 'ether')
  params = {
      #'type': '0x1',
      'chainId': chainId, 
      'nonce': nonce,
      'gas': 2000000,
      'gasPrice': gas_price,
      'value': amount_in_wei,
      'from': from_addr,
      #'maxFeePerGas': w3.toWei('50', 'gwei'),
      #'maxPriorityFeePerGas': w3.toWei('5', 'gwei')
  }

  maxSubmissionCost = int(amount_in_wei * 0.01)
  func = contract.functions.depositEth(maxSubmissionCost)
  #sign the transaction
  try:
    tx = func.buildTransaction(params)
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return {'status': 'success', 'txn_hash': w3.toHex(txn), 'task': 'deposit ETH on Arbitrum'}
  except Exception as e:
    return {'status': 'failed', 'error': e, 'task': 'Deposit ETH on Arbitrum'}

if __name__ == "__main__":

    # Arbitrum chain(42161)
    chainId = 42161

    # Source addres
    from_addr = Web3.toChecksumAddress(sys.argv[1])
    contract_addr   = '0x578bade599406a8fe3d24fd7f7211c0911f5b29e'

    amount_in_eth = 0.005

    result = arbitrum_depositEth(chainId, from_addr, contract_addr, amount_in_eth)
    print(result)

