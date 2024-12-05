import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.getenv('API_TOKEN')

headers = {
    'Authorization': API_TOKEN
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'scan_type': 'Gitleaks Scan',
    'active': 'true',
    'verified': 'true',
    'minimum_severity': 'low',
    'engagement': '17',  # This is the engagement id
}

files = {
    'file': open('gitleaks-report.json', 'rb')
}

response = requests.post(url, headers=headers, files=files, data=data)
if response.status_code == 201:
    print('Scan report imported successfully')
else:
    print('Failed to import scan report')
    print(response.content)