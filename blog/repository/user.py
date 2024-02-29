from .. import schemas,models
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi import HTTPException,status


def create_user(request:schemas.user,db:Session):
    new_user=models.user(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f'id {id} with user is not available')
    db.commit()
    return user