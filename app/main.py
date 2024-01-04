# docker build -t dominimage .
# docker run -d --name containerapi -p 80:80 dominimage
from fastapi import FastAPI  

app = FastAPI()

@app.get('/')
def root():
    return {"Hello" : "World"}


def lengthCalc(filename):
    import string
    # Opening and reading file in 
    f = open(filename, "r")
    text = f.read()

    # Cleaning all punctuation out of the string and splitting words
    punctuationToClean = string.punctuation.replace("-","").replace("'","").replace("&","").replace("/","")
    cleanText = text.translate(str.maketrans("", "", punctuationToClean)).split() # removes punctuation and splits on whitespace

    # Declaring counting vars
    lengths = [0 for i in range(45)] # define array used to store length values
    count = 0 # total word count
    charcount = 0

    # Looping through clean text, counting and averaging
    for word in cleanText:
        wordLength = len(word)
        count += 1 # output: word count
        charcount += wordLength
        lengths[wordLength] += 1 # output: array of word length counts

    averageWordLength = charcount / count # output: average length of words
    mostFrequentCount = max(lengths) # output: most frequent word lengths
    mostFrequentCountLengths = [index for index, value in enumerate(lengths) if value == mostFrequentCount] # output: word lengths of most frequent lengths

    return {"Word_Count" : count, 
            "Avg_Length" : averageWordLength, 
            "Length_Array": lengths, 
            "Length_Mode": mostFrequentCount, 
            "Length_Mode_Length": mostFrequentCountLengths}