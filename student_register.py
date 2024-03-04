# user_file = open(r'C:\Users\harry\Documents\Python Code Camp\Tasks' 'reg_form.txt', 'w') 

user_file = open('registration_form.txt', 'w') 
student_count = int(input("Please enter the number of students on the register: \n"))

print(f"You have entered {student_count} students.") 

for student_reg in range(student_count): 
    student_id = input("Please enter the student's ID number: \n")
    user_file.write('......................................................................... \n')
    user_file.write(student_id + '\n') 

user_file.write('...........................END OF REGISTER............................... \n')

user_file.close() 

