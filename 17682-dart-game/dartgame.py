def solution (dartResult):
    # 0. input and initialize
    scores = []
    start_index = 0
    power = {'S': 1, 'D': 2, 'T': 3} 

    # 1.  per dartResult
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power: # S, D, T
            scores.append(int(dartResult[start_index:i]) ** power[op])
        elif op == '*':
            scores[-2:] = [x*2 for x in scores[-2:]]
        elif op == '#':
            scores[-1] = -scores[-1]
        
        if not op.isnumeric():
            start_index = i+1

    # 2. return sum of scores
    return sum(scores)
solution('1S2D*3T')
