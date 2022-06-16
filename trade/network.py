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

def _get_network_name_by_chainid(chainid) -> str:
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
def get_w3_by_network(chainid=1) -> Web3:
    network = _get_network_name_by_chainid(chainid)
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3
