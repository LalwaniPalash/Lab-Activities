def name_filter(data):
    names = []
    for name in data:
        if len(name) > 5:
            names.append(name)
    return names
    
data = ["Jack", "John", "Jenny", "Jennifer", "Paul", "Pauline"]
filtered_names = name_filter(data)

print(filtered_names)
