

numbers = [-2, 2]

def treasureCode(codes):
    product = 1
    for code in codes:
        if code % 2 == 0:
            product *= code
    return product

print(treasureCode(numbers))

