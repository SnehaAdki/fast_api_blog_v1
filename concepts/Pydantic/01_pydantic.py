
from pydantic import BaseModel , Field
from typing import Optional
from enum import Enum
from datetime import datetime
import time

class Language(str,Enum):
    PY = "python"
    JAVA = "Java"
    GO = "go"

class Blog(BaseModel):
    title : str = Field(min_length = 10)
    is_active : bool
    description : Optional[str] = None
    language : Language = Language.PY
    created_at : datetime = Field(default_factory = datetime.now)


f1 = Blog(title = "My tittle 12345" , is_active=True)
print(f1)

time.sleep(5)

f2 = Blog(title = "2nd title 742992" , is_active=True)
print(f2)