def isMagicNumber(number):
    isMagic = sum(int(digit) for digit in str(number))
    if isMagic % 7 == 0:
        return True
    else:
        return False

print(isMagicNumber(43))