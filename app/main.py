# docker build -t dominimage .
# docker run -d --name containerapi -p 80:80 dominimage
from fastapi import FastAPI  

app = FastAPI()

@app.get('/')
def root():
    return {"Hello" : "World"}