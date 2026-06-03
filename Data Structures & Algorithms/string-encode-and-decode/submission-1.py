class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedResult = []
        for word in strs:
            encodedResult.append(f"{len(word)}#{word}")
        return "".join(encodedResult)
            

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i=0

        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            wordStart = j+1
            wordEnd = wordStart + length
            decodedStrings.append(s[wordStart:wordEnd])
            i=wordEnd
        return decodedStrings
