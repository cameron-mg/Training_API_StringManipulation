# docker build -t dominimage .
# docker run -d --name containerapi -p 80:80 dominimage
from fastapi import FastAPI, File, UploadFile
# from fastapi_cache2 import *
import re

app = FastAPI()

@app.get('/')
def root():
    return {"Root" : "Hello"}

@app.post('/upload/')
async def upload(file: UploadFile = File(...)):
    text = await file.read()
    return lengthCalc(str(text))


def lengthCalc(text):
    import string

    # Cleaning all whitespace characters and punctuation out of the string and splitting words
    # cleanText = re.sub(r"\\n", "", text)
    punctuationToClean = string.punctuation.replace("-","").replace("'","").replace("&","")
    cleanText = text.translate(str.maketrans("", "", punctuationToClean)).split() # removes punctuation and splits on whitespace
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

    averageWordLength = charcount / count # output: average length of words
    mostFrequentCount = max(lengths.values()) # output: most frequent word lengths
    mostFrequentCountLengths = [key for key, value in lengths.items() if value == mostFrequentCount] # output: word lengths of most frequent lengths

    return {"Word_Count" : count, 
            "Avg_Length" : averageWordLength, 
            "Length_Array": lengths, 
            "Length_Mode": mostFrequentCount, 
            "Length_Mode_Length": mostFrequentCountLengths}