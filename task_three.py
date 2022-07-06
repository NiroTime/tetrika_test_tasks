def appearance(intervals):
    events = []
    for interval in intervals:
        event = intervals[interval]
        for i in range(len(event)):
            events.append((event[i], 1 - 2 * (i % 2)))
            events.sort()
    cnt = 0
    start = -1
    together_time = 0
    for event in events:
        cnt += event[1]
        if cnt == 3:
            start = event[0]
        if cnt == 2 and start > 0:
            together_time += event[0] - start
            start = -1
    return together_time
