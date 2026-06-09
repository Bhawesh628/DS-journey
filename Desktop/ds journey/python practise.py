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



