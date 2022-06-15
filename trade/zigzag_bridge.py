import sys
from web3 import Web3

from local_types import AddressLike
from util import (
    _str_to_addr,
    _addr_to_str,
    _validate_address,
    _load_contract,
    _load_contract_erc20,
    is_same_address,
)
from network import (
    get_w3_by_network,        
)
from file_parser import (
    eth_addr_parse_from_file,
    parse_private_key_from_addr,
)

def zigzag_bridge(chainId, contract_addr, token, from_addr, amount_in_eth):
  w3 = get_w3_by_network(chainId)
  if not w3.isConnected():
    print("w3 is not connected")
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

