# import pyttsx3


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[1].id)
# engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# a = str(input("Enter the words or things that you want the system to speak:\n"))
# speak(a)

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