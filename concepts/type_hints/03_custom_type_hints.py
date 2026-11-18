class Job:
    def __init__ (self , title : str, description : Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self): #it's a magic methods which invokes the repr
        return self.title


obj1 = Job(title = "Team Lead" , description = "Sshgjsfgksnf")
obj2 = Job(title = "XYZ" , description = "afadaffd")

jobs : list[Job] = [obj1 , obj2]
print(jobs)