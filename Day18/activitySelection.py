def activitySelection(start, finish):
    
    activities = []

    for i in range(len(start)):
        activities.append((finish[i], start[i]))

    activities.sort()

    count = 1
    last_finish = activities[0][0]

    print("Selected Activities:")
    print((activities[0][1], activities[0][0]))

    for i in range(1, len(activities)):

        curr_finish = activities[i][0]
        curr_start = activities[i][1]

        if curr_start >= last_finish:
            count += 1
            last_finish = curr_finish
            print((curr_start, curr_finish))

    return count


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

print("Maximum Activities =", activitySelection(start, finish))