class Person:
    """
    Base class representing a Person
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

class Worker:
    """
    Class representing a worker.
    """
    def __init__(self, job_title: str, company: str):
        self.job_title = job_title
        self.company = company
    
    def work(self) -> None:
        print(f"{self.job_title} working at {self.company}")

class Stundent:
    """
    Class representing a student.
    """
    def __init__(self, major: str, university: str):
        self.major = major
        self.university = university
    
    def study(self) -> None:
        print(f"Studying {self.major} at {self.university}")


class WorkingStudent(Person, Worker, Stundent):
    """
    Derived class representing a person who is both worker and student.
    """
    def __init__(self, name: str, age: int, job_title: str, company: str, major: str, university: str):
        Person.__init__(self, name, age)
        Worker.__init__(self, job_title, company)
        Stundent.__init__(self, major, university)
        

def main() -> None:
    # creat a working student obj
    ws = WorkingStudent(
        name="Alice",
        age = 25,
        job_title="Software Engineer",
        company="TechCrop",
        major="Computer Science",
        university="MIT"
    )

    ws.display_info()
    ws.work()
    ws.study()

if __name__ == "__main__":
    main()