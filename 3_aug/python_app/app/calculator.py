def mutliply(a,b):
    return a*b
    
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    if b==0:
        raise ValueError("Cant divide by zero")
    return a/b