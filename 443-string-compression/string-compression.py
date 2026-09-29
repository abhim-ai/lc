class Solution:
    def compress(self, chars: list[str]) -> int:
        '''
        return the length of the compressed string array. Compression logic:
        character, followed by the count of the similar characters. If only one character then just the character no count needed

        Test Cases:
        - chars = ["a","a","b","b","c","c","c"] -> 6 (["a","2","b","2","c","3"])
        - chars = ["a"]->1(["a"])
        - chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]-> 4(["a","b","1","2"])

        Assumptions & 
        - Count lower case & Upper Case characters separately, dont combine

        Constraints:
        - 1 <= chars.length <= 2000
        - chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

        Cases to handle:
        - Counting digits/symbols/upper/lower
        - When the count is more than single digit then split the count as separate characters
        '''

        #Approch 1
        #Use 2 pointers, 1 for start and 1 for end of group and string to hold the chars and counts
        s,i="",0
        while i<len(chars):
            j=i
            while j<len(chars) and chars[j]==chars[i]:
                j+=1
            s+=chars[i]+(str(j-i) if j-i>1 else "")
            i=j
        chars[:len(s)]=s
        return len(s)




