from transaction import transaction
from web3 import Web3

# this is my project on infura
infura_url = 'https://mainnet.infura.io/v3/7a99188377d641cf8bba51559b9ed4d9'

# target address is assigned within "account.txt" file
def batch_trans(from_addr, private_key):
  w3 = Web3(Web3.HTTPProvider(infura_url))
  if not w3.isConnected():
    return

  #get the nonce.  Prevents one from sending the transaction twice
  nonce = w3.eth.getTransactionCount(from_addr)
  gas_price = w3.eth.gasPrice

  # same folder, so there is no directory 
  filename = 'account.txt' 
  with open(filename, 'r') as file_to_read:
    entry_num=0
    while True:
      lines = file_to_read.readline().strip() 
      if not lines:
        break
        pass
      if(len(lines) != 42):  # len need to take into "0x"
        break
        pass
      if (lines[:2] != '0x'):
        break
        pass
      #build a transaction in a dictionary
      eth_value = 0.001
      to_addr = lines
      tx = {
          'nonce': nonce+entry_num,
          'to': to_addr,
          'value': w3.toWei(eth_value, 'ether'),
          'gas': 2000000,
          'gasPrice': gas_price
      }
      #sign the transaction
      signed_tx = w3.eth.account.signTransaction(tx, private_key)
      w3.eth.sendRawTransaction(signed_tx.rawTransaction)
      buf = "%f eth is sent to wallet %s" % (eth_value, tx['to'])
      yield buf

      # count for the loop
      entry_num=+1

    pass

if __name__ == "__main__":
    # Source addres is removed here
    from_addr = ???
    private_key = ???
    print("Translating from wallet %s" % from_addr)

    for n in batch_trans(from_addr, private_key):
        print(n)
