class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        '''
        Return a list of stepping numbers between a give low and high range
        
        Test Cases:
            - [0,21]->[0,1,2,3,4,5,6,7,8,9,10,12,21]
            - [10,15]->[10,12]
            - [100,112]->[100,101,102,103,104,105,106,107,108,109]
        
        Assumptions:
            - Only Integers
        
        Cases:
            - First no. should be always present
            - -ve, +ve and 0
        
        Edge Cases:
            - 3 digit nos? 
        '''

        res=[0] if low==0 else []
        q=deque(range(1,10))
        while q:
            x=q.popleft()
            if x>high: break
            if x>=low: res.append(x)
            d=x%10
            if d>0: q.append(x*10+d-1)
            if d<9: q.append(x*10+d+1)
        return res