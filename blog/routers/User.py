from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from ..repository import user



router = APIRouter(
    prefix= '/user',
    tags=['Users']
    )


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.showuser)
def create_user(request:schemas.user,db:Session=Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}',status_code=200,response_model=schemas.getuser)
def getuser(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)