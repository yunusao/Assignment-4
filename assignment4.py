#modules that were downloaded to connect postegres to python
import psycopg2             
import psycopg2.extras  

#Postgres credentials used to connect to database (change to yours)
hostname = 'localhost'
database = 'Assignment4'
username = 'postgres'
pwd = 'INSERT POSTGRES PASSWORD HERE' 
port_id = 5433 

connection = None
cur = None

# function that when called, retreives and prints all students in database, using cur.fetchall
def getAllStudents():
    cur.execute('SELECT * FROM students ORDER BY student_id ASC')
    print('{:<10} {:<10} {:<10} {:<30} {:<15}'.format('Student ID', 'First Name', 'Last Name', 'Email', 'Enrollment Date'))
    for i in cur.fetchall():
        print('{:<10} {:<10} {:<10} {:<30} {:<15}'.format(i['student_id'],i['first_name'],i['last_name'], i['email'], i['enrollment_date'].strftime('%Y-%m-%d')))
    return cur.fetchall()

# Function that when called, adds the student's information to the database
def addStudent(first_name, last_name, email, enrollment_date):
    insert = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
    insertVal =[(first_name, last_name, email, enrollment_date)]
    for i in insertVal:
        cur.execute(insert, i)
        connection.commit()
    
# Function that when called, updates the student's email, using given student ID
def udpateStudentEmail(student_id, email):
    update = 'UPDATE students SET email = %s WHERE student_id = %s'
    cur.execute(update, (email, student_id))
    connection.commit()

#Function that when called, deletes student from database using given student ID
def deleteStudent(student_id):
    delete = 'DELETE FROM students WHERE student_id = %s'
    deleteRec = (student_id,)
    cur.execute(delete, deleteRec)
    connection.commit()

#Function that asks user to choose an option from the main menu, where they can either print all students, add student, update
#student email, delete student, or exit program
def mainMenu():
    print("MAIN MENU:\n")
    print('1. Get All Students')
    print('2. Add Student')
    print('3. Update Student Email')
    print('4. Delete Student')
    print('0. Exit')
    return input('\nEnter your choice: ')

#Creates the table for database in postgres 
def createScript():
    create_script = '''
        CREATE TABLE IF NOT EXISTS students
        (
            student_id		SERIAL PRIMARY KEY,
            first_name      TEXT NOT NULL,
            last_name       TEXT NOT NULL,
            email           TEXT NOT NULL UNIQUE,
            enrollment_date DATE  

        )
    '''
    cur.execute(create_script)

#Inserts given values into table that was created in createScript
def insertScript():
    insert = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
    insertVal =[('John', 'Doe', 'john.doe@example.com', '2023-09-01'), ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')]
    for i in insertVal:
        cur.execute(insert, i)

#Main functionality of the code, where connection to the server is made, and user is using the database based on the options given in the main menu
try:
    with psycopg2.connect(

        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id) as connection:

        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS students')

            createScript()
            
            insertScript()

            while True:
                choice = mainMenu()
                if choice == '1':
                    getAllStudents()
                elif choice == '2':
                    first_name = input('Enter first name: ')
                    last_name = input('Enter last name: ')
                    email = input('Enter email: ')
                    enrollment_date = input('Enter enrollment date: ')
                    addStudent(first_name, last_name, email, enrollment_date)
                elif choice == '3':
                    student_id = input('Enter student id: ')
                    email = input('Enter email: ')
                    udpateStudentEmail(student_id, email)
                elif choice == '4':
                    student_id = input('Enter student id: ')
                    deleteStudent(student_id)
                elif choice == '0':
                    break
                else:
                    print('Invalid choice') 
            

except Exception as e:
    print(e)

finally: 
    if connection is not None:
        connection.close()