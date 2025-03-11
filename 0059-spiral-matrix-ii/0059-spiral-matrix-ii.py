class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[' ' for _ in range(n)] for _ in range(n)]
        top,bottom,left,right=0,n-1,0,n-1
        v=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans[top][i]=v
                v+=1
            top+=1
            for i in range(top,bottom+1):
                ans[i][right]=v
                v+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans[bottom][i]=v
                    v+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans[i][left]=v
                    v+=1
                left+=1
        return ans

        