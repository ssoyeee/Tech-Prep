class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        return "".join(result)
 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i) 
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            i = j+1+length 
            result.append(word)
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))