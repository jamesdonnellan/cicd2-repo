from typing import Annotated 
 
from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints 
 
NameStr = Annotated[str, StringConstraints(min_length=2, max_length=50)] 
StudentIdStr = Annotated[str, StringConstraints(pattern=r"^S\d{7}$")] 
 
class UserCreate(BaseModel): # Validates incoming JSON. It has no id because the database generates the value
    name: NameStr 
    email: EmailStr 
    age: int = Field(gt=18, lt=120) 
    student_id: StudentIdStr 
  
class UserRead(BaseModel): # Defines outgoing JSON. It includes the generated id. 
    model_config = ConfigDict(from_attributes=True) # Allows Pydantic to build the response model from SQLAlchemy object attributes. 
 
    id: int 
    name: NameStr 
    email: EmailStr 
    age: int 
    student_id: StudentIdStr 