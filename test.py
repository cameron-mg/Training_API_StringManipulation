import requests

url = 'http://127.0.0.1:8000/upload/'
files = {'file': open(r'C:\Users\camer\Documents\Coding_Misc\DominAPI\test_text_files\text.txt', 'r')}

response = requests.post(url, files=files)

print(response.text)