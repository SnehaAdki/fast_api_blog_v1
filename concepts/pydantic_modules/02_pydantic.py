# Before = Modify or validate raw incoming data before field validation.
# After = Validate relationships and business rules using already validated model fields.


from pydantic import BaseModel , field_validator , model_validator
class CreateUser(BaseModel):
    email : str
    password : str
    confirm_password : str

    @field_validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("Admin keyword is not allowed ..........")
        return value

    @model_validator(mode='before')
    @classmethod
    def validate_password(cls, values):
        print("inside the validate password method using mode as before.........")
        print(values)
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError("Password and Confirm Password do not match")
        return values

    # @model_validator(mode='after')
    # def validate_password(self):
    #     print("inside the validate password method using mode as after.........")
    #     print(self)
    #     password = self.password
    #     confirm_password = self.confirm_password
    #     if password != confirm_password:
    #         raise ValueError("Password and Confirm Password do not match")
    #     # return self

c1 = CreateUser(email = 'sn@abc.com' , password='123',confirm_password = '123')

c2 = CreateUser(email = 'admin@abc.com' , password='123',confirm_password = '12883')
