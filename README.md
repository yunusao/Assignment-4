# Assignment-4
Assignment 4 for COMP 3005 made by Yunus Abu-Oshaibah

Note: The video below taught me how to connect python to postgres, 
how to make the connect variable and cursor variable, and what they do 
https://www.youtube.com/watch?v=M2NzvnfS-hI

Set-Up:

    -Create a Database in Postgres by the name of 'Assignment4' 
    
    - install psycopg2 module
        
        -For Windows: 
            
            -Open Comand Prompt
            
            -Enter 'pip install pycopg2'
            
        -For Mac/Linux:
            
            -Open Terminal
            
            -Enter 'pip3 install pycopg2'

        -This will install the pycopg2 module, which allows us to connect Postgres to our Python script
    
    -Postgres Credintials

        - Have your Host Name, Database name, username, password, 
        and port ID

Steps to Compile:

    - Very simply, copy and paste code into VS Code, save, and 
    click run


Function Explination:

    -def getAllStudents()

        -This function prints out all students in the table

    -def addStudent(first_name, last_name, email, enrollment_date)

        -This function takes in the properties of a student, and 
        adds them to the Students table

    -def udpateStudentEmail(student_id, email)

        -This function takes in the Student ID to locate the 
        specifc tuple, and reassigns their email based on user 
        input

    -def deleteStudent(student_id):

        -This function takes in the Student ID to locate the 
        specifc tuple, then deletes it from the table

    -def mainMenu():

        -Prints out the main menu of the program
    
    -def createScript():

        -This function inputs the given database schema into the 
        query to set up the table
    
    -def insertScript():

        -This function inputs the initial data into the query to 
        add values to the table
        