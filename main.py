from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # return published is getting in string
    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return {'data': f'{limit} blog from the db'}
    

@app.get('/blog/unmatched')
def unmatched():
    return {'data':'unmatched blog'}
# /blog/unmatched cannot write this after the dynamic routing(/blog/{id})

@app.get('/blog/{id}')
def show(id: int):
    # fetch the blog in id = id
    return {'data': id}

@app.get('/blog/{id}/comment')
def comment(id):
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data': f'the blog is created with title {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)