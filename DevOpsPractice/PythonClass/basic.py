print('hello')
# python function


def add(a, b):
    #   a = 2
    #    b = 3
    c = a + b
    print(type(c))
    print(c)
    name = "John"
    school = 'Izaan School'
    print(school)


    # fancy way to print
    # print("My name is: {}, {}" .format(name, school))


    #print("name variable type: {}, school variable type: {}".format(type(name), type(school)))
    #print(f"name variable type: {name}, school variable type: {school}")


def students_info():
    students = ["mohi", "foysal", "shamim", "masud", 22]

    print(students)
    print(type(students))




add(2, 3)
students_info()


# how to write to exponential in python
var = 4 ** 2
print(var)

capital = 100
interest_rate = 10
net_worth = 100*(1.1**7)
print(net_worth)


fam = [17, 1.45, 1.22, 2.90]

print(fam[2:4])


#help(type)



p = "aaaaaaaaaahnnbnweruoifguiwv"
print(p.count(""))