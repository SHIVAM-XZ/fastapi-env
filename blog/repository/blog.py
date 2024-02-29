from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status


def get_all(db:Session):
    blog = db.query(models.blog).all()
    return blog

def create(request:schemas.Blog,db:Session):
    new_blog = models.blog(title=request.title,body=request.body,user_id=1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id:int,db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with an id {id} is not available')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'blog with an id {id} is not available'}
    return blog
    
def discard(id:int,db:Session):
    blog=db.query(models.blog).filter(models.blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with an id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.blog).filter(models.blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with an id {id} is not available')
    blog.update(request.__dict__)
    db.commit()
    return 'updated'