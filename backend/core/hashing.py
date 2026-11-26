from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")


class Hasher: 
    @staticmethod #object can't be created only class name invokation
    def verify_passowrd(plan_password, hashed_passowrd):
        return pwd_context.verify(plan_password,hashed_passowrd)


    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)