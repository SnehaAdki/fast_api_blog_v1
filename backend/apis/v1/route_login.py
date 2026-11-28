from fastapi import APIRouter , status, Depends , HTTPException

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import get_db
from core.hashing import Hasher

from core.config import settings

from db.repository.login import get_user_by_email 

from core.security import create_acess_token
from jose import jwt, JWTError

router = APIRouter()

def authenticate_user(email: str , password :str, db : Session):
    user = get_user_by_email(email=email , db=db)
    if not user:
        return False
    if not Hasher.verify_passowrd(password , user.password):
        return False
    return user 

@router.post("/token")
def login_access_token(form_data : OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db : Session = Depends(get_db)):
    user = authenticate_user(form_data.username , form_data.password , db)
    if not user:
        return HTTPException(detail="Incorrect email or password" , status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_acess_token(data={"sub" : user.email})
    return {"access_token": access_token , "token_type":"bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme) , db: Session = Depends(get_db)):
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials, Pelase login again"
    )
    try : 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(payload)
        email : str = payload.get("sub")
        if email is None:
            raise credential_exceptions
    except JWTError:
        raise credential_exceptions
    user = get_user_by_email(email=email , db = db)
    if user is None:
        raise credential_exceptions
    return user