def circular_lock(start, target):

    # Find minimum moves required to convert start -> target Each digit is on a circular dial (0-9)
    
    moves = 0
    for s, t in zip(start, target):
        s, t = int(s), int(t)
        diff = abs(s - t)
        moves += min(diff, 10 - diff)  
    return moves

start = input("Enter starting combination: ")  
target = input("Enter target combination: ")   

print("Minimum moves required:", circular_lock(start, target))
