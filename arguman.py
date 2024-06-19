def student_info(name, age=22, city="Tehran"):
    return f"name={name}, age={age}, city={city}"


#print(student_info(age=33, name="ebi"))

#tuple unpacking 
s1 = ("Alireza", 28, "mashhahd")
print(student_info(*s1))

# dic unpacking
s2 = {"name":"Alireza", "age":33, "city":"Neyshabur"} 
print(student_info(**s2))

def student_lesson_info(name, *args):
    sum_ = sum(args)
    return f"name={name}, avg={sum_/len(args)}"

print(student_lesson_info("Ebi", 20, 12, 13, 15, 19))


def student_lesson_info2(name, **kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
student_lesson_info2(name="Ebi", city="Ney", age=33, avg=19)