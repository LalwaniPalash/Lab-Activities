def schedule_classes(classes):
    classes.sort(key=lambda x: x[1])
    
    scheduled_classes = []
    last_end_time = 0
    
    for start, end in classes:
        if start >= last_end_time:
            scheduled_classes.append((start, end))
            last_end_time = end  # Update the last end time
    
    return scheduled_classes

classes = [(1, 4), (2, 3), (3, 5), (4, 6)]

result = schedule_classes(classes)
print(f"Scheduled classes: {result}")
