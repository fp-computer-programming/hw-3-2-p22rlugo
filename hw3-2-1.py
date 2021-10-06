# Ryan Lugo: RJL 10/6/21

average_grade = int(input("What is your Average numerical Grade for this quarter?: "))

# Putting each grade as a Value just in case prep changes the numbers
a = 93
a_minus = 90
b_plus = 87
b = 83
b_minus = 80
c_plus = 77
c = 73
c_minus = 70
d_plus = 65
d = 60

if average_grade >= a:
    print("You got an A")
elif average_grade >= a_minus:
    print("You got an A-")
elif average_grade >= b_plus:
    print("You got an B+")
elif average_grade >= b:
    print("You got an B")
elif average_grade >= b_minus:
    print("You got an B-")
elif average_grade >= c_plus:
    print("You got an C+")
elif average_grade >= c:
    print("You got an C")
elif average_grade >= c_minus:
    print("You got an C-")
elif average_grade >= d_plus:
    print("You got an D+")
elif average_grade >= d:
    print("You got an D")
else:
    print("You got an F")
