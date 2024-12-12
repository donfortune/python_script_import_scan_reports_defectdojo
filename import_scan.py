import requests
import os
from dotenv import load_dotenv
import sys #read user input

file_name = sys.argv[1] #get the file name from the user input
scan_type = ''

if file_name == 'gitleaks.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'nmap.json':
    scan_type = 'Nmap Scan'
elif file_name == 'njsscan.serif':
    scan_type = 'SARIF'
elif file_name == 'semgrep.json':
    scan_type = 'Semgrep JSON Report'
else:
    print('Invalid file name')
    sys.exit()


load_dotenv()


API_TOKEN = os.getenv('API_TOKEN')

headers = {
    'Authorization': API_TOKEN
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    # 'scan_type': 'Gitleaks Scan',
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

