import requests

def get_branch_number() -> int:
    """
    Get a quantum random number x where 0 <= x <= 7
    """
    print("Getting a quantum random number")
    url = 'http://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8&size=1'
    response = requests.get(url).json()
    return(response['data'][0]%8)

if __name__ == "__main__":
    print(get_branch_number())
