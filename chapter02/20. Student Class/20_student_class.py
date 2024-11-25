class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def main():
    st = Student("Bob", "M.")

    print("First name:", st.firstname)
    print("Last name:", st.lastname)

if __name__ == "__main__":
    main()