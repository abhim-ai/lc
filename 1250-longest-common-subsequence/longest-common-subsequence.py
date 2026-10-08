class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''

        Constraints:
        only lowercase eng char
        1<=len(text1),len(text2)<=1000

        Cases to handle:
        No match return 0
        Full match return len(text2)
        partial match len(matched_text2)
        len(text2)>len(text1)

        text1='trauipyhe', text2='tape'-> 4
        text1='bullfrog',text2='bully'->4


        '''

        store = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    store[i][j]=1+store[i+1][j+1]
                else:
                    store[i][j]=max(store[i][j+1],store[i+1][j])
        
        return store[0][0]


''' 
i=0,j=0
text1=[a,b,c,d,e]
text1=[a,c,e]
[      a c e
 a    [3,2,1,0]
 b   ,[2,2,1,0]
 c   ,[2,2,1,0]
 d   ,[1,1,1,0]
 e   ,[1,1,1,0]
     ,[0,0,0,0]
]

3
'''

        