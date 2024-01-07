import requests

# url = 'http://127.0.0.1:80/upload/' # docker image url
url = 'http://127.0.0.1:8000/upload/' # uvicorn local test url
filepath = input("Please enter the absolute path of the file you would like to analyze: ")

try:
    # POST request and read data
    files = {'file': open(f'{filepath}', 'r')}
    response = requests.post(url, files=files) # API call
    data = response.json()

    # Formatting output print statements
    print(f"\nWord count = {data['Word_Count']} \nAverage word length = {data['Avg_Length']:.03f}")

    for key in data['Length_Array']:
        value = data['Length_Array'][key]
        print(f"The number of words of length {key} is {value}.")

    print(f"The most frequently occuring word length is {data['Length_Mode']}, for word lengths of {data['Length_Mode_Length']}\n")

except Exception as e:
    print(e)
