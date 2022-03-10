from transaction import transaction
from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/7a99188377d641cf8bba51559b9ed4d9'

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

def batch_trans(from_addr, private_key):
  w3 = Web3(Web3.HTTPProvider(infura_url))
  if not w3.isConnected():
    return

  #get the nonce. prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice

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
      #signed_tx = w3.eth.account.signTransaction(tx, private_key)
      #w3.eth.sendRawTransaction(signed_tx.rawTransaction)
      print("%f eth is sent to wallet %s" % (eth_value, tx['to']))

      # count for the loop
      entry_num=+1

if __name__ == "__main__":
    # Source addres is removed here
    from_addr = ???
    private_key = ???
    print("Translating from wallet %s" % from_addr)
    batch_trans(from_addr, private_key)
