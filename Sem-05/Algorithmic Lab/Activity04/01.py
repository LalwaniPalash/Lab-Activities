def schedule_tasks(durations, T):
    durations.sort()
    
    total_time = 0
    task_count = 0
    
    for duration in durations:
        if total_time + duration <= T:
            total_time += duration
            task_count += 1
        else:
            break  # Stop if we exceed the maximum time T
    
    return task_count

durations = [5, 3, 4, 2, 1]
T = 6

result = schedule_tasks(durations, T)
print(f"Maximum number of tasks that can be completed within {T} time: {result}")
