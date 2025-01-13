# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students):
    student_register = {}
    
    for student in students:
        name, age = student
        if name not in student_register: 
            student_register[name] = age
    
    return student_register

students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
    
print(create_student_register(students))

