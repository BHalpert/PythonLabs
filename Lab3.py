year = 1990
pop = 89.2
print('enter number of years')
changeyear = int(input())
def increase():
    return pop * 1.023
def decrease():
    return pop / 1.023
endyear = 1990 + changeyear
while year != endyear:
    if changeyear >= 0:  # Checks if input if positive or negative
        pop = increase()
        year += 1
    else:
        pop = decrease()
        year -= 1
print(pop, endyear)
