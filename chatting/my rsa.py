test = ['237', '53', '241', '124', '44', '156', '33', '188']
print(test[0])
print(type(test[0]))


a = ['1','2','3']
print ([int(s) for s in a])
print(a)

for i in range (0, len(test)) :
    test[i] = int(test[i])


print(test)