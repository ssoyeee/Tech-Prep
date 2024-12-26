from collections import defaultdict

def solution(survey, choices):
    # Create a defaultdict with a default value of an empty int
    letter2score = defaultdict(int)
    for (a, b), choice in zip(survey, choices): #survey is always two letters ex AN, CF, ... --(a, b)
        if choice < 4:
            letter2score[a] += 4 - choice # strongly disagree = 1, not sure = 4
        elif choice > 4: # not sure = 4, strongly agree = 7
            letter2score[b] += choice - 4
    type1, type2 = ["R", "C", "J", "A"], ["T", "F", "M", "N"]
    answer = ''
    for t1, t2 in zip(type1, type2): # R vs T, C vs F
        if letter2score[t1] > letter2score[t2] or (letter2score[t1] == letter2score[t2] and t1 <t2):
            answer += t1
        else: 
            answer += t2
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])) #result: "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3])) #result: "RCJA"
