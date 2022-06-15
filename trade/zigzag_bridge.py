import sys
from web3 import Web3
from enum import Enum
from dynaconf import settings
from web3 import gas_strategies
from web3.gas_strategies.time_based import medium_gas_price_strategy

from local_types import AddressLike
from util import (
    _str_to_addr,
    _addr_to_str,
    _validate_address,
    _load_contract,
    _load_contract_erc20,
    is_same_address,
)

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

def zigzag_bridge(chainId, contract_addr, token, from_addr, amount_in_eth):
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

  contract = _load_contract(w3, "zksync", contract_addr)

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice
  baseFee = w3.eth.getBlock("latest").baseFeePerGas
  maxPriorityFee = w3.toWei('3', 'gwei')
  maxFee = baseFee + maxPriorityFee

  params = {
      'type': 2,
      'chainId': chainId, 
      'nonce': nonce,
      'gas': 2000000,
      #'gasPrice': gas_price,
      'maxFeePerGas': maxFee,
      'maxPriorityFeePerGas': maxPriorityFee,
      #'gasLimit': "21000",
  }

  #get decimals to multiply by token amount
  amount = int(amount_in_eth * 10 **18)
  func = contract.functions.depositERC20(token, amount, from_addr)
  #sign the transaction
  try:
    tx = func.buildTransaction(params)
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return {'status': 'success', 'txn_hash': w3.toHex(txn), 'task': 'Zigzag bridge'}
  except Exception as e:
    return {'status': 'failed', 'error': e, 'task': 'Zigzag bridge'}

if __name__ == "__main__":

    # Zksync contract address (from mainnet)
    contract_addr = '0xabea9132b05a70803a4e85094fd0e1800777fbef'

    # DAI stablecoin Token
    dai = '0x6B175474E89094C44Da98b954EedeAC495271d0F'

    # mainnet chainId is 1
    filename = 'account.txt'
    for from_addr, amount_in_eth in eth_addr_parse_from_file(filename):
      result = zigzag_bridge(1, contract_addr, dai, from_addr, amount_in_eth)
      if (result['status'] == 'failed'): print(result)

