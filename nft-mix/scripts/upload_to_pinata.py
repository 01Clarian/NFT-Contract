import requests
import os
from pathlib import Path

PINATA_BASE_URL = 'https://api.pinata.cloud/'
endpoint = 'pinning/pinFileToIPFS'
# Change this to upload a different file
filepath = './img/pug.png'
filename = filepath.split('/')[-1:][0]
headers = {'pinata_api_key': os.getenv('PINATA_API_KEY'),
           'pinata_secret_api_key': os.getenv('PINATA_API_SECRET')}


with Path(filepath).open("rb") as fp:
    image_binary = fp.read()
    response = requests.post(PINATA_BASE_URL + endpoint,
                             files={"file": (filename, image_binary)},
                             headers=headers)
    print(response.json())
