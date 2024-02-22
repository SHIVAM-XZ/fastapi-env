from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'rohan'}}

@app.get('/about')
def abot():
    return {'data': 'about page'}