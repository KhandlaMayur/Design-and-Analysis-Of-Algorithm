def activity_selection(start_times, finish_times):
    n = len(start_times)

    activities = list(zip(range(n), start_times, finish_times))
    
    activities.sort(key=lambda x: x[2])
    
    selected_activities = []
    last_finish_time = 0
    
    for activity in activities:
        index, start, finish = activity
        if start >= last_finish_time:
            selected_activities.append(index)  
            last_finish_time = finish
    
    return selected_activities

start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start_times, finish_times)
print("Selected Activities (by index):", selected)
