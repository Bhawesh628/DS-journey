
def greet_user():
    print(" hello wssgoin")
   
greet_user()


def homie_calling():
    print("yo homies assemble")
homie_calling() 

def is_even(number):
    "return True if the number is even, false otherwise"
    return number % 2 == 0
print(is_even(4))
print(is_even(7))

def calculate_total_bill(subtotal, tip_percentage , promo_code):
  tip_amount = subtotal * (tip_percentage/100)
  discount = 0 
  if promo_code == "save10":
    discount = 10
  elif promo_code == "welcome5":
    discount = 5
 final_total = subtotal + tip_amount - discount
  return final_total
bill_one = calculate_total_bill(50, 15, "save10")
print("first_bill_total:" , bill_one)
bill_two = calculate_total_bill(100, 15, "welcome5")
print("secod_bill_total:", bill_two)

def get_passing_grade(all_score):
    passing_scores = []
    for score in all_score:
     if score >= 70:
        passing_scores.append(score)
    return passing_scores
    classroom_grades = [85, 62, 91, 45, 73, 68, 100]
passed_students = get_passing_grade(classroom_grades)
print("Passing grades are:", passed_students)

def make_little_box(text):
   length = len(text)
   border = "+" + "-" *(length + 2) + "+"
   print(border)
   print(f"|{text}|")
   print(text)
make_little_box("GAME OVER")
make_little_box("LOADING...")
make_little_box("CONGRATULATIONS!")

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

def student(fname, lname):
    print(fname, lname)

student(fname= ' bhawesh', lname='man of no religion')
student(lname='the man of no religion ', fname= 'bhawesh')
