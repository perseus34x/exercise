import sys
from web3 import Web3
from enum import Enum

INFURA_SECRET_KEY = '7a99188377d641cf8bba51559b9ed4d9'

class Network_name(Enum): 
 ETH_MAINNET = 'mainnet'
 RINKEBY = 'rinkeby'
 ROPSTEN = 'ropsten'
 OP_MAINNET = 'optimism-mainnet'
 AR_MAINNET = 'arbitrum-mainnet'
 AR_RINKEBY = 'arbitrum-rinkeby'

def get_network_name_by_chainid(chainid):
    if(chainid == 1): 
        network = Network_name.ETH_MAINNET;
    elif(chainid == 3):
        network = Network_name.ROPSTEN;
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

def single_trans(chainid, from_addr, to_addr):
  w3 = get_w3_by_network(chainid)
  if not w3.isConnected():
    return

  # get private key
  private_key = parse_private_key_from_addr(from_addr)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  print("nonce %d, gas_price %d" % (nonce, gas_price))

  eth_value = 0.002
  tx = {
      'nonce': nonce,
      'to': to_addr,
      'value': w3.toWei(eth_value, 'ether'),
      'gas': 2000000,
      'gasPrice': gas_price
  }
  #sign the transaction
  try:
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return {'status': 'success', 'txn_hash': w3.toHex(txn), 'task': 'Transfer ETH'}
  except Exception as e:
    return {'status': 'failed', 'error': e, 'task': 'Transfer ETH'}

def scatter_trans(chainid, from_addr):
  w3 = get_w3_by_network(chainid)
  if not w3.isConnected():
    return

  # get private key
  private_key = parse_private_key_from_addr(from_addr)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  print("nonce %d, gas_price %d" % (nonce, gas_price))

  # same folder, so there is no directory 
  entry_num=0
  filename = 'account.txt' 
  for to_addr, eth_value in eth_addr_parse_from_file(filename): 
      tx = {
          'nonce': nonce+entry_num,
          'to': to_addr,
          'value': w3.toWei(eth_value, 'ether'),
          'gas': 2000000,
          'gasPrice': gas_price
      }
      #sign the transaction
      try:
        signed_tx = w3.eth.account.signTransaction(tx, private_key)
        txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
      except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'Scatter ETH'}

      # count for the loop
      entry_num += 1

  return {'status': 'success', 'task': 'Scatter ETH'}

def merge_trans(chainid, to_addr):
  w3 = get_w3_by_network(chainid)
  if not w3.isConnected():
    return

  #get the nonce. prevents one from sending the transaction twice
  gas_price = w3.eth.gasPrice

  # same folder, so there is no directory 
  filename = 'account.txt' 
  for from_addr, eth_value in eth_addr_parse_from_file(filename): 
      
      # get private key
      private_key = parse_private_key_from_addr(from_addr)

      nonce = w3.eth.getTransactionCount(from_addr)
      tx = {
          'nonce': nonce,
          'to': to_addr,
          'value': w3.toWei(eth_value, 'ether'),
          'gas': 2000000,
          'gasPrice': gas_price
      }
      #sign the transaction
      try:
        signed_tx = w3.eth.account.signTransaction(tx, private_key)
        txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
      except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'Merge ETH'}

  return {'status': 'success', 'task': 'Scatter ETH'}

if __name__ == "__main__":

    chainid = int(sys.argv[1])
     
    # Source addres
    from_addr = ???
    to_addr   = ???

    print("Translating from wallet %s on chainid %d" % (from_addr, chainid))
    #result = single_trans(chainid, from_addr, to_addr)
    #result = scatter_trans(chainid, from_addr)
    result = merge_trans(chainid, to_addr)
    print(result)

