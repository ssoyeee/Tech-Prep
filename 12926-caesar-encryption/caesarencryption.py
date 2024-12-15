def solution(s, n):
    UPPER_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    answer = ''
    
    for letter in s:
        if letter.islower():
            answer += lower_alpha[(lower_alpha.index(letter)+n)%26]
        elif letter.isupper():
            answer += UPPER_ALPHA[(UPPER_ALPHA.index(letter)+n)%26]
        # space
        else:
            answer += letter
    
    return answer