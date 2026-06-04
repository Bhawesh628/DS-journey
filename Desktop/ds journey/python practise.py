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



