# import random
# a = [1,2,3,4,5,6,7,8,9,0]
# b = random.choice(a)
# print(b)


# import calendar
# a = int(input("Enter a year for printing its calendar;\n"))
# b = calendar.calendar(a)
# print(b)

# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# x = str(input("Enter anything that you want the syatem to speak:\n"))
# speak(x)
a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
c = str(input("Choose an operator, 'a' for add, 's' for subtract, 'm' for multiply, 'd' for divide:\n"))
if c == "a":
    print(f'The sum of the given numbers is {a+b}')
elif c == "s":
    print(f"The difference of the given numbers is {a-b}")
elif c == "m":
    print(f"The product of the given numbers is {a*b}")
elif c == "d":
    print(f"The division of the given number is {a/b}")
else:
    print(f"Please enter a valid input!!")