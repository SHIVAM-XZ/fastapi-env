from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models,token
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    users = db.query(models.user).filter(models.user.email == request.username).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credential')
    if not Hash.Verify(users.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'incorrect password')
    
    access_token = token.create_access_token( data={"sub": users.email})
    return {"access_token": access_token, "token_type":"bearer"}