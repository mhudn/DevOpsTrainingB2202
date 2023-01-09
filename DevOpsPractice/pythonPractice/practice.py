# How to write a python function

def add(x, y):
    # z = x + y
    # print(z)
    return x + y


add(2, 3)


def devide(x, y):
    z = x / y
    print(round(z, 2))


devide(11, 3)

name = "Mohi"
school = 'Izaan School'
print(f"My name is {name} and I go to {school}")

fam = [1, "aaa", 3, "bb", 5, "ccc", 6.5, "ddd", 7.7, "eee", 8]
A = [1, 3, 4, 5]
B = [[1, 3, 4, 5], [2, 4, 6, 9]]
C = [1 + 2, "a" * 5, 3]

print("\n", A, "\n", B, "\n", C, "\n", )

print(fam[3])
print("\n")

print(fam[3])
print(fam[3:])
print(fam[0:])
print(fam[0:-1])
print(fam[-1])
print(fam[-3:-2])

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# live_sleep_are = areas[4] + areas[7]

print(areas[5] + areas[7])

tuples = (2, 4.3, 5.1, 2, 3)
print(tuples)

x = ["a", "b", "c", "d"]
x[2:3] = ["s", "t"]
print(x)

x = ["a", "b", "c", "d"]
x[2:] = [1, [1, 5]]
print(x)

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas)
new_washroom_area = 10.5
areas[-1] = new_washroom_area
print(areas)
areas.append(11)
print(areas)
areas.append(15.45)
print(areas)
areas.reverse()

print(areas)

fam = [1.7, 1.68, 1.13, 1.89]

# ------------- WHO IS THE TALLEST and shortest IN MY FAMILY--------------------???????????????

print(max(fam))

print(min(fam))

# ---------------- ROUND FUNCTIONS ------------------------ #
print(round(1.69, 1))
print(round(1.69, 0))
print(round(1.69))

# help(round)

# help(type)

# ---------------- SORTED FUNCTION WITH EXAMPLE ---------------------- #
# Create lists first and second

first = [1, 2, 3]
second = [4, 5]
full = first + second
print(f"this list {full} is a combination of {first} and {second}")

# Sort full in descending order: full_sorted
full_sorted = sorted(full)
print(full_sorted)

full_sorted = sorted(full, reverse=True)
print(full_sorted)


# ____________________________________________________________
def my_first_function(item, lyst):
    index_number = lyst.index(item)
    print(f"the index number of your given {item} is {index_number}")


list1 = ["salmon", "sashimi", "salmon", "sushi", "salmon"]

my_first_function("sashimi", ["salmon", "sashimi", "salmon", "sushi"])

wali = ["salmon", "sashimi", "salmon", "sushi", "salmon"]


def second_function(fish, list_of_fish):
    total_count = list_of_fish.count(fish)
    print(f"the count of your given {fish} is {total_count}")


second_function("salmon", wali)
# _____________________________________________________________

population = [200, 123, 5000, 2500]
countries = ["Bangladesh", "asgfd", "India", "Pakistan"]
index_of_India = countries.index("India")
print(index_of_India)
print(population[2])

world = {"Bangladesh": 200, "asgfd": 123, "India": 5000, "Pakistan": 2500}

print(world.keys())
print(world.values())

print(world["India"])

world["India"] = 5555
print(world)
print(world["India"])

world.pop('Bangladesh', None)  # Deletes Bangladesh value:key pairs
print(world)



# complex(real, imaginary)
print(complex(10, 20))  # Represents the complex number (10 + 20j)
print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

complex_1 = complex(0, 2)
complex_2 = complex(2, 0)
print(complex_1)
print(complex_2)


# numbers = 10
#
# for num in range(numbers):
#     print(num)
#
#
#
# for i in range(1, 11):  # A sequence from 1 to 10
#     if i % 2 == 0:
#         print(i, " is even")
#     else:
#         print(i, " is odd")



foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for f in foo:
    print(f)



