
# # house list of lists
# house = [["hallway", 11.25, "MYHOUSE"],
#          ["kitchen", 18.0, "MY2222HOUSE"],
#          ["living room", 20.0],
#          ["bedroom", 10.75],
#          ["bathroom", 9.50]]
# for x in house:
#     print(f"the {x[0]} is {x[1]} square meteres ")
# # HOLL=["hallway", 11.25]
# # print(HOLL[0])

########DICTIONARY LOOOPING#################

world = {"afghanistan": 30.55,
         "albania": 2.77,
         "algeria": 39.21}

print(world.items())  # turns dictionary into tuples
# dict_items([('afghanistan', 30.55), ('albania', 2.77), ('algeria', 39.21)])
# in order to loop a dictionary, we will have to turn the dictionary to tuples and
for x in range(1, 5, 3):
    print(x)