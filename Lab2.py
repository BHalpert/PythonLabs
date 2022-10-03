# + – *  /  %  ^
print('Enter a number:')
num1 = int(input())
print('Enter an operator:')
opp = str(input())
print('Enter a number:')
num2 = int(input())

opdict = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
        "%": num1 % num2,
        "^": num1 ** num2
    }
if opp in opdict:
    print('Result:', opdict.get(opp))
else:
    print('error, invalid operator')
