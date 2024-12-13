trees = [2, 4, 5, 9]

def countApples(trees):
    product = 0
    for apple in trees:
        product += apple
    return product

print(countApples(trees))