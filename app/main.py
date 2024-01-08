# docker build -t dominimage .
# docker run -d --name containerapi -p 80:80 dominimage
from fastapi import FastAPI, File, UploadFile
from cachetools import cached, TTLCache
import time, string, re, hashlib

app = FastAPI()
cache = TTLCache(maxsize=1024, ttl=1800) # 1KB cache, auto-delete after 30mins

# Root Method (Testing Host)
@app.get('/')
def root():
    return {"Root" : "Hello"}

# Upload Method (API)
@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    try:
        text = await file.read()
        checksum = get_checksum(text.decode()) # generate checksum

        # check data is in cache, return if present
        if checksum in cache:
            return cache[checksum]
        
        # compute and store in cache, return data
        data = lengthCalc(text.decode())
        cache[checksum] = data
        return data
    
    except Exception as e:
        return e


# Checksum Generation Method
def get_checksum(x):
    return hashlib.sha256(x.encode()).hexdigest()

# Metric Calculation Method
def lengthCalc(text):
    try:
        # Cleaning all whitespace characters and punctuation out of the string and splitting words
        cleanText = text.strip()
        punctuationToClean = string.punctuation.replace("-","").replace("'","").replace("&","").replace("/","")
        cleanText = cleanText.translate(str.maketrans("", "", punctuationToClean)).split() # removes punctuation and splits on whitespace

        # Declaring counting vars
        lengths = {} # define dictionary used to store length values
        count = 0 # total word count
        charcount = 0

        # Looping through clean text, counting and averaging
        for word in cleanText:
            wordLength = len(word)
            count += 1 # output: word count
            charcount += wordLength
            if wordLength in lengths.keys():
                lengths[wordLength] += 1 # output: array of word length counts
            else:
                lengths[wordLength] = 1

        lengths = dict(sorted(lengths.items())) # output: sorted array of word lengths
        averageWordLength = charcount / count # output: average length of words
        mostFrequentCount = max(lengths.values()) # output: most frequent word lengths
        mostFrequentCountLengths = [key for key, value in lengths.items() if value == mostFrequentCount] # output: word lengths of most frequent lengths

        return {"Word_Count" : count, 
                "Avg_Length" : averageWordLength, 
                "Length_Array": lengths, 
                "Length_Mode": mostFrequentCount, 
                "Length_Mode_Length": mostFrequentCountLengths}
    
    except Exception as e:
        return e