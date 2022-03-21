def switch(module):
    switch_statement = {
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object-Oriented Programming"

    }
    return switch_statement.get(module, "an Invalid Module Code")


module = input("Enter the Module Name: ")

print("The Module " + module + " is " + switch(module))
