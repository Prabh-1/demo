def remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[(),('1'),('2','3'),(),('hello','khush')]
print(tuples)
print(remove(tuples))