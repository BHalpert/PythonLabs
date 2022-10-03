salary = 0
hours = 0
print('enter your salary')
x = input()
if int(x) <= 0:  # checks if input is a valid number, quits if not
    print('Error, salary must be positive')
    quit()
else:
    salary = int(x)
print('enter your hours')
x = input()
if int(x) <= 0:  # checks if input is a valid number, quits if not
    print('Error, hours must be positive')
    quit()
else:
    hours = int(x)
if hours > 40:  # checks if the worker qualifies for overtme
    money = salary * 40
    money += (hours - 40) * (salary * 1.5)
    print('you earned: ', money)
else:
    print('you earned ', hours * salary)
