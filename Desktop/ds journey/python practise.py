PRACTISE PROBLEMS
I'm going to build a simple program that asks the user for a few words, stores them in variables, and then plugs them into a funny story.

name = input("enter a name")
adjective = input("enter an adjective (describing word) :")
number = int(input("enter a number: "))

plural_noun = input("enter a plural_noun :")

print(f"Yesterday, {name} found a {adjective} box in the backyard. ")
print(f" inside, there were exactly {number} shiny {plural_noun} ")
#result 
Yesterday,  bhawesh found a glowing box in the backyard. 
 inside, there were exactly 2 shiny robots 

print(10 + 2)
print(2*2)
print(4-2)
print(4/2)

print("5" + "5")

print("ha" * 10)
print("my name is bhawesh " * 5)

print(11 % 2)

Imagine you have 23 slices of pizza and you are splitting them equally among 5 friends.
# Write a one-line program using the % sign to find out how many slices of pizza will be left over in the box.
# print(23%5)

# You are building a weather app. The user inputs the temperature in Celsius,
#  and your program needs to convert it to Fahrenheit.The algebraic formula to convert Celsius to Fahrenheit
 
celcius = 20 
farhenheit = (celcius * 9/5+32)
print(farhenheit)
celcius = 20 
farhenheit = (celcius * 9/5+32)
print(farhenheit)
print(f"The temperature is {farhenheit} degrees.")
if farhenheit > 60:
    print("It is warm outside, wear a t-shirt!")
else:
    print("It is cold outside, bring a jacket!")


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527]
for number in numbers:
    if number == 601:
        break 
    if number % 2 == 1:
        continue
    print(number)

try:
    integer = int(input("enter your lucky number: "))
    if integer % 2 == 0:
        print(f"{integer} is an even number")
    else:
          print(f"{integer} is an odd number" )
except ValueError:
    print("invalid input.Please enter a valid number")

     
try:
    number = int(input("enter your number: "))
    if number % 2 != 0:
        print(f"{number} is an odd number")
    else:
        print(f"{number} is not an odd number")
except ValueError:
    print("invalid input. type integer")
        print(f"{integer} is an odd number" )
except ValueError:
    print("invalid input.Please enter a valid number")
class Scores:
    count = 0 # class variable
    all_student_lists = []
    def __init__(self, serial_num, name, gender, date_of_birth, location, maths_marks,physics_marks,chemistry_marks):
        self.serial_num = serial_num
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.location = location
        self.maths_marks = maths_marks
        self.physics_marks = physics_marks
        self.chemistry_marks = chemistry_marks
        self.total_marks = maths_marks + physics_marks + chemistry_marks

        Scores.count += 1
        # Each instantiation in class keeps a record of the count
        Scores.all_student_lists.append(self)
        # Each instatiation in class updates the student to the all_students_list

    # Let's just define a class method to calculate the average marks of any subject
    @classmethod
    def avgmarks(cls, subject_marks):
        total_subject_marks = 0
        for student in Scores.all_student_lists:
            total_subject_marks += getattr(student, subject_marks)
        print(f"The average {subject_marks} is {total_subject_marks / len(Scores.all_student_lists)}")

    # Creating a way to view each student card (method) 
    def display_student_card(self):
      print("\n=====================Student Card==========================\n")
        print(f" Student ID : {self.serial_num}")
        print(f" Name       : {self.name}")
        print(f" Gender     : {self.gender}")
        print(f" DOB        : {self.date_of_birth}")
        print(f" Town/City  : {self.location}")
        print("\n===========================================================\n")
        print(f" Maths      : {self.maths_marks}")
        print(f" Physics    : {self.physics_marks}")
        print(f" Chemistry  : {self.chemistry_marks}")
        print("\n===========================================================\n")
        print(f" Total      : {self.total_marks}")
        print("\n===========================================================\n")
# create the students objects
s1  = Scores(0,"Bhuvanesh", 'M', "7 Nov","Erode", 68, 64, 78)
s2  = Scores(1,"Harish" ,'M', "3 June", "Salem", 62, 45, 91)
s3  = Scores(2,"Shashank" ,'M', "4 Jan",    "Chennai", 57, 54, 77)
s4  = Scores(3,"Rida" ,'F', "5 May","Chennai", 42, 53, 78)
s5  = Scores(4,"Ritika" ,'F', "17 Nov","Madurai", 87, 64, 89)
s6  = Scores(5,"Akshaya" ,'F', "8 Feb","Chennai", 71, 92, 84)
s7  = Scores(6,"Sameer" ,'M', "23 Mar","Ambur", 81, 82, 87)
s8  = Scores(7,"Aditya" ,'M', "15 Mar","Vellore", 84, 92, 76)
s9  = Scores(8,"Surya" ,'M', "28 Feb","Bengaluru", 74, 64, 51)
s10 = Scores(9,"Clarence" ,'M', "6 Dec","Bengaluru", 63, 88, 73)
s11 = Scores(10,"Kavya" ,'F', "12 Jan","Chennai", 64, 72, 68)
s12 = Scores(12,"Srinidhi" ,'F', "14 Jan","Chennai", 52, 64, 71)
s13 = Scores(13,"Gopi" ,'M', "6 May","Madurai", 65, 73, 89)
s14 = Scores(14,"Sophia" ,'F', "23 Jul","Trichy", 89, 62, 93)
s15 = Scores(15,"Goutami" ,'F', "22 Sep","Teni", 76, 58, 90)
s16 = Scores(16,"Tauseef" ,'M', "30 Dec","Trichy", 87, 86, 43)
s17 = Scores(17,"Arshad" ,'M', "14 Dec","Chennai", 62, 81, 67)
s18 = Scores(18,"Abirami" ,'F', "9 Oct","Erode", 72, 92, 97)
s19 = Scores(19,"Vetrival" ,'M', "30 Aug","Trichy", 56, 78, 62)
s20 = Scores(20,"Kalyan" ,'M', "17 Sep","Vellore", 93, 68, 91)
s21 = Scores(21,"Monika" ,'F', "15 Mar","Bengaluru", 78, 69, 74)
s22 = Scores(22,"Priya" ,'F', "17 Jul","Nagercoli", 62, 62, 57)
s23 = Scores(23,"Deepika" ,'F', "13 May","Bengaluru", 97, 91, 88)
s24 = Scores(24,"Siddharth" ,'M', "26 Dec","Madurai", 44, 72, 58)
s25 = Scores(25,"Geeta" ,'F', "16 May","Chennai", 87, 75, 92)
s26 = Scores(26,"JK" ,'M', "22 Jul","Chennai", 74, 71, 82)
s27 = Scores(27,"Jagan" ,'M', "4 Mar","Madurai", 81, 76, 52)
s28 = Scores(28,"Nisha" ,'F', "10 Sep","Madurai", 74, 83, 83)
s29 = Scores(29,"Naveen" ,'M', "13 Oct","Vellore", 72, 66, 81)
        # students_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29]


# Q1: Count the number of cards

count = 0
for _ in Scores.all_student_lists:
    count += 1
print (count)
print(Scores.count)
print(len(Scores.all_student_lists))
        
# Q2: Find the average maths marks

# Declaration and Initialization
total_math_marks = 0 

# Iterations 
for students in Scores.all_student_lists:
    total_math_marks += students.maths_marks

print(f"The average total_math_marks = {total_math_marks/count}")
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

# calling the class method
Scores.avgmarks("maths_marks")
Scores.avgmarks("physics_marks")
Scores.avgmarks("chemistry_marks")

# Displaying the card calling the display method
s1.display_student_card()

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")


