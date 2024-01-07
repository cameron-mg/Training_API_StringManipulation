import requests, time, os

# url = 'http://127.0.0.1:80/upload/' # docker image url
url = 'http://127.0.0.1:8000/upload/' # uvicorn local test url
directory = './test_text_files'

for filename in os.listdir(directory): # looping through files in test directory
    for i in range(2): # loop twice to check once without cache and once with

        files = {'file' : open(os.path.join(directory, filename), 'r')}
        
        start = time.time()
        response = requests.post(url, files=files) # API call
        end = time.time()

        match i:
            case 0:
                nocachetime = end-start
            case 1:
                cachetime = end-start

    print(f"For file: {filename}, caching saved: {(nocachetime-cachetime)*1000:.03f}ms")

