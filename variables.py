# name = 'Ben Sherman'
# school = 'Seneca Valley High School'

# print("{} works at {}.".format(name, school))

# def addition():
#     a = int(input("enter a number: "))
#     b = int(input("enter another number: "))
#     print(a + b)

# addition()

# def user_info(name, age, city):
#     print("{} is {} years old, from {}".format(name, age, city))

# user_info("Janet", 58, "Oklahoma City")

# def application(fname, lname, email, company, *args, **kwargs):
#     print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

# application("Jess", "Ingrass", "mail@mail.com", "Teach Code", 75000, hire_date="September 2010")

name = input("What's your name?: ")

if name == "Jessica":
    print("Hello, nice to see you {}".format(name))

elif name == "Danielle":
    print("Hello, you are a great person!")

elif name != "Mariah":
    print("You're not Mariah!")

elif name == "KIngston":
    print("Hi, {}, let's have lunch soon!".format(name))

else:
    print("Have a nice day!")