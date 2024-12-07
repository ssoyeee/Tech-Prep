class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs: #we access string by string in the input
            res += str(len(s)) + "#" + s # 4#leet#5code, use delimiter to seperate two words, followed by string itself
        return res    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # result of encoded, pointer i: what position that we're at in the input str
        res, i = [], 0 

        while i < len(s): #i is still in bounds
            j = i #second pointer, delimiter character
            while s[j] != "#": #find the delimiter to find the end of the integer "4neet#4code"
                j += 1 # increment the pointer by 1 until find a pound
            length = int(s[i:j]) # length of first word excluding 'int' 'delimiter'
            res.append(s[j+1 : j+1+length]) # "code" idx 6~11->6,7,8,9
            i = j + 1 + length #could be the end of the entire string, beginning of the next string
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))