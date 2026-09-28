class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        #nums is empty 
        #nums=[-4,-1,0,3,10]
        #out=[0,1,9,16,100]
        out=[] # [16,1,0,9,100]
        for i in nums: 
            out.append(i*i) 
        
        def mergesort(out: List[int])->List[int]: # out=[16,1,0,9,100], out=[16,1],out=[16],out=[1]
            if len(out)==1:
                return out
            mid=len(out)//2 #mid=2,mid=1
            leftList=mergesort(out[:mid]) #out[0:2],out[0:1]-> LeftList=16
            rightList=mergesort(out[mid:]) #out[1:2],rightList->1
            return merge(leftList,rightList) #[1,16]
        
        def merge(L:List[int],R:List[int])->List[int]: #L=[16],R=[1]
            res=[]#res=[1]
            i,j=0,0#j=1
            while i<len(L) and j<len(R): #0<1,0<1,0<1,1<=1
                if L[i]<=R[j]:
                    res.append(L[i])
                    i+=1
                else:
                    res.append(R[j]) 
                    j+=1
                

            return res+L[i:]+R[j:] #[1,16]

        return mergesort(out) # [16,1,0,9,100]

'''
mergesort([16,1,0,9,100]), mid=2
|--mergesort([16,1]),mid=1
    |--mergesort([16])->16
    |--mergesort([1])->1
    |--merge([16],[1])->[1,16]
    ->[1,16]
|--mergesort([0,9,100]),mid=1
    |--mergesort([0])->0
    |--mergesort([9,100]),mid=1
        |--mergesort([9])->9
        |--mergesort([100])->100
        |--merge([9],[100])->[9,100]
        ->[9,100]
    |--merge([0],[9,100])->[0,9,100]
|--merge([1,6],[0,9,100])->[0,1,6,9,100]

'''

