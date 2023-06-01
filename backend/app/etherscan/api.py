import requests
from config import Config


def get_transactions(start_block=0):
    """Get ERC20 token transactions from Etherscan API"""

    url = f"{Config.ETHERSCAN_API_ENDPOINT}?module=account&action=tokentx&address=0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640&startblock={start_block}&sort=desc&apikey={Config.ETHERSCAN_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('status') == '1' and response.json().get('result') or []
    except requests.exceptions.HTTPError as err:
        print(err)
        return []
    except:
        print("Unexpected error")
        return []
