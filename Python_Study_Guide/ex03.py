def squares(x):
    for i in range(x):
        yield x ** 2
        
squares(5)