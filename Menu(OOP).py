import json
class Student:
    def __init__(self, stu_id, stu_name, stu_class):
# __init__ ek special method hy jo object bnaty wqt parametres ko automatically execute krega, self ->ek parametre hy jo current object ko refer krta hy
# parametres-> stu_id, name, stu_class 
        self.id = stu_id
        # self.id -> current object ka attribute = stu_id -> argument ki wo value jo object banate waqt di gai thi        
        self.name = stu_name
        self.student_class = stu_class
        self.marks = {}
        # Yani object.id -> current jo bi object hoga us mn jo arguments bhi diye jaein gy wo values ko hm parametres ko assign kr dein gy 



    def add_marks(self):# self ka matlab hy current Student object.
# Is method ki wjah se student ki ID dobara search karne ki zaroorat nahi!            
        while True:
            stu_sub = input("Enter Subject: ")
            stu_marks = int(input("Enter Marks: "))
            self.marks[stu_sub] = stu_marks#current Student object ki marks dictionary
            print("Marks added successfully!")
            again = input("Do you want to add another subject? (yes/no):")
            if again == "no":
                break

            def calculate_result(self):
                if not self.marks:
                    return None
            total = sum(self.marks.values())#marks ki dictionary mn jitni bhi values hein un ka sum ly lo
            percentage = total / len(self.marks)

            if percentage >= 95:
                grade = "A+"

            elif percentage >= 90:
                grade = "A"

            elif percentage >= 85:
                grade = "B+"

            elif percentage >= 80:
                grade = "B"

            elif percentage >= 75:
                grade = "C+"

            elif percentage >= 70:
                grade = "C"

            elif percentage >= 65:
                grade = "D"

            else:
                grade = "Fail"
            return total, percentage, grade    

    def show_result(self):
        result = self.calculate_result()
        if result is None:
            print("Marks not added yet!")
            return

        for subject, mark in self.marks.items():
            print(subject, ":", mark)
        total, percentage, grade = result  

        print("Total:", total)
        print("Percentage:", percentage, "%")
        if grade == "Fail":
            print("You are fail...")

        else:
            print("Grade =", grade)  

    def student_report(self): 
        print("ID:", self.id)
        print("Name:", self.name)
        print("Class:", self.student_class)

        self.show_result()       

class ManagementSystem:
    def __init__(self):
        self.stu_list = []
        self.filename = "stu_data.json"

    def find_student(self, stu_id):

        for current_stu in self.stu_list:

            if current_stu.id == stu_id:
                return current_stu

        return None  

    def add_student(self):

        stu_id = int(input("Enter ID: "))

        for current_stu in self.stu_list:

            if stu_id == current_stu.id:
                print("Duplicate ID!")
                return

        stu_name = input("Enter Name: ")
        stu_class = input("Enter Class: ")

        student = Student(stu_id, stu_name, stu_class)
    # student -> object hy aur 1, "Sidra", "CS" -> arguments hein    
        self.stu_list.append(student)
    # student object stu_list mn store hogya
    #print(stu_list)
        print("Student added successfully!")

    def view_student(self):

        if not self.stu_list:
            print("No student found!")
            return

        for current_stu in self.stu_list:

            print("\nID:", current_stu.id)
            print("Name:", current_stu.name)
            print("Class:", current_stu.student_class)

            if current_stu.marks:
                print("Marks:", current_stu.marks)  

    def search_student():

        stu_id = int(input("Enter ID that you want to search: ")) 

        current_stu = self.find_student(stu_id)
        if current_stu is not None:

            print("Student found!")
            print("ID:", current_stu.id)
            print("Name:", current_stu.name)
            print("Class:", current_stu.student_class)

        else:
            print("Student not found!")

    def update_student(self):

        stu_id = int(input("Enter student ID: "))

        current_stu = self.find_student(stu_id)

        if current_stu is not None:

            print("Student found!")

            current_stu.name = input("Enter new name: ")

            current_stu.student_class = input(
                "Enter new class: "
            )

            print("Student updated successfully!")

        else:
            print("Student not found!") 

    def delete_student(self):

        stu_id = int(input("Enter student ID: "))

        current_stu = self.find_student(stu_id)

        if current_stu is not None:

            self.stu_list.remove(current_stu)

            print("Student deleted successfully!")

        else:
            print("Student not found!")  

    def result_student(self):

        stu_id = int(
            input("Enter ID that you want to search: ")
        )

        current_stu = self.find_student(stu_id)

        if current_stu is not None:

            current_stu.show_result()

        else:
            print("Student not found!")                    


    def student_report(self):

        stu_id = int(input("Enter student ID: "))

        current_stu = self.find_student(stu_id)

        if current_stu is not None:

            current_stu.student_report()

        else:
            print("Student not found!")

    def statistics(self):

        percent_list = []

        highest_percent = None
        highest_student = ""

        lowest_percent = None
        lowest_student = ""

        pass_students = 0
        fail_students = 0

        for current_stu in self.stu_list:

            result = current_stu.calculate_result()

            if result is None:

                print(
                    current_stu.name,
                    "your marks not added yet!")

                continue

            total, percentage, grade = result

            if (highest_percent is None or percentage > highest_percent):

                highest_percent = percentage
                highest_student = current_stu.name

            if (
                lowest_percent is None or percentage < lowest_percent):

                lowest_percent = percentage
                lowest_student = current_stu.name

            percent_list.append(percentage)

            if percentage >= 65:

                print(
                    "Congrats",current_stu.name,"! you are pass...")

                pass_students += 1

            else:

                print(
                    "Oops",current_stu.name,"! you are fail...")

                fail_students += 1

        if percent_list:

            avg = sum(percent_list) / len(percent_list)

            print("\nClass Average:", avg, "%")

            print("Highest Scorer:", highest_student)
            print("Highest Percentage:", highest_percent, "%")

            print("Lowest Scorer:", lowest_student)
            print("Lowest Percentage:", lowest_percent, "%")

            print("Pass Students:", pass_students)
            print("Fail Students:", fail_students)

        else:

            print("No marks available for statistics!")


    def save_data(self):

        data = []#ye aik list hy jis mn student ki dictionaries temporarily store hon gi

        for current_stu in self.stu_list:# phir loop chly ga k stu_list mn jitny bhi students hein un ki dictionaries data naam ki list mn store kr do

            student_data = {

                "id": current_stu.id,

                "name": current_stu.name,

                "class": current_stu.student_class,

                "marks": current_stu.marks

            }

            data.append(student_data)# data wali list mn student se bnny wali dictionary ko append kr do

        with open(self.filename, "w") as file:

            json.dump(data, file, indent=4)#hm ne yhan data ki jgah syudent list isi liye use nhi ki k us mn objects ki form mn data hy jb k json  
                                          #objects k liye kaam nhi krta jb k data mn ye objects dictionaries ki form mn store hein

        print("Data saved successfully!")

    def load_data(self):

        try:

            with open(self.filename, "r") as file:# "r" → file ko read karna hai

                data = json.load(file)# json.load(file) → JSON file ka data Python mein le aayega,data mein ab dictionaries ki list hogi. 

            self.stu_list = []

            for current_stu in data:

                student = Student(

                    current_stu["id"],

                    current_stu["name"],

                    current_stu["class"]

                )

                student.marks = current_stu.get("marks", {})

                self.stu_list.append(student)

            print("Data loaded successfully!")

        except FileNotFoundError:

            print(
                "No saved data found. Starting with empty data."
            )

        except json.JSONDecodeError:

            print("Saved data file is empty or invalid.")
    

    def menu(self):

        self.load_data()

        while True:

            print("\n===== Student Management System =====")

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Add Marks")
            print("7. Student Result")
            print("8. Student Report")
            print("9. Show Statistics")
            print("10. Save the Data")
            print("11. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.add_student()

            elif choice == "2":

                self.view_student()

            elif choice == "3":

                self.search_student()

            elif choice == "4":

                self.update_student()

            elif choice == "5":

                self.delete_student()

            elif choice == "6":

                self.add_marks()

            elif choice == "7":

                self.result_student()

            elif choice == "8":

                self.student_report()

            elif choice == "9":

                self.statistics()

            elif choice == "10":

                self.save_data()

            elif choice == "11":

                print("It's Over!")

                break

            else:

                print("Invalid choice, try again...")


app = ManagementSystem()

app.menu()                