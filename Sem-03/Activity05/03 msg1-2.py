def msg1():
    print("Message 1")

def msg2():
    print("Message 2")

vars_output = vars().keys()
dir_output = dir()

vars_set = set(vars_output)
dir_set = set(dir_output)

common_elements = vars_set.intersection(dir_set)
unique_to_vars = vars_set.difference(dir_set)
unique_to_dir = dir_set.difference(vars_set)

print("Common elements:", common_elements)
print("Unique to vars:", unique_to_vars)
print("Unique to dir:", unique_to_dir)
