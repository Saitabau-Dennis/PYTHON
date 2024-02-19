names_string = input("Enter the names for all the students separated by white space:")
name_list = names_string.split()
name_list = sorted(set(name_list))
print(name_list)
