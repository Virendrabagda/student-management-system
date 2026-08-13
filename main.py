from database import DB 
print("students managment system")

cursor = DB.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS  STUDENTS (
ID INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(100),
AGE INT,
COURSE VARCHAR(100),
MARK INT 
)
""")
DB.commit()
while True:
    print("\n---student mangment system")
    print("students table ready!")
    print("1. Add student")
    print("2. View student")
    print("3. update student")
    print("4. delete student")
    print("5. search student")
    print("6. Exit")

    choice = input("Enter your choice:")
    print("CHOICE =", repr(choice))
    if choice == "1":
        name = input("Enter student name:")
        age = int(input("Enter age:"))
        course = input("Enter course:")
        mark = int(input("Enter marks:"))

        query = """
        INSERT INTO STUDENTS(NAME,AGE,COURSE,MARK)
        VALUES(%s,%s,%s,%s)
        """
        cursor.execute(query,(name,age,course,mark))
        DB.commit()
        print("students added successfully!")
    elif choice == "2":
        cursor.execute("SELECT * FROM STUDENTS")
        students=cursor.fetchall()
        
        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")
        input("press enter to continue")

    elif choice =="3":
        while True:
            try: 
                student_id = int(input("Enter student ID:"))
                break
            except ValueError:
                print("please enter valid number")   
        new_name = input("Enter new name")
        try:
            new_mark = int(input("Enter new marks:"))
            query = "UPDATE STUDENTS SET NAME=%s,MARK=%s WHERE ID = %s"
            cursor.execute(query,(new_name,new_mark,student_id))
            DB.commit()
            print("student updated successfully!")
        except ValueError:
            print("Invalid input fot marks")
    elif choice == "4":
        try:
            student_id = int(input("Enter student ID:"))
            check_query = "SELECT * FROM STUDENTS WHERE ID=%s"
            cursor.execute(check_query_query,(student_id,))
            student = cursor.fetchone()
            
            if student:
                delete_query = "DELETE FROM STUDENTS WHERE ID=%s"
                cursor.execute(delete_query,(student_id,))
                DB.commit()
                print("student deleted successfully!")
            else
                print("press enter not found!")
            input("press Enter to continue...")    
        except ValueError:
            print("please enter a valid id")
            input("press Enter to continue...")
    elif choice == "5":
        try:
            student_id = int(input("Enter student ID:"))
            print("id enterd successfully")
            query ="SELECT * FROM STUDENTS WHERE ID=%s"
            cursor.execute(query,(student_id,))
            student = cursor.fetchone()
            
            if student:
                print("student found:",student)
            else:
               print("student not found:")
            input("press Enter to continue...")
        except Exception  as e:
            print("Error:",e)
            input("press Enter to continue...")
    elif choice == "6":
        print("Exiting...")   
        break

    else:
        print("Invalid choice")