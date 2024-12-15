def semordnilap(words):
    # Semordnilap <---> palindrome
    answer = []
    words_set = set(words) # in constant time
    
    for word in words:
        flipped = word[::-1] # in m time
        if flipped in words_set and flipped != word:
            answer.append([word, flipped])
            words_set.remove(word) # not having a duplicate
            words_set.remove(flipped) # not having a duplicate
    return answer

# Time O (n*m) where n is length of words array and m is max size of any string in that array
# Space: O(n*m)