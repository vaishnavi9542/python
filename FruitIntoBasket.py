class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        left,right=0,0
        maxLen=0
        n=len(arr)
        mpp={}
        while(right<n):
            if(arr[right] in mpp):
                mpp[arr[right]]+=1
            else:
                mpp[arr[right]]=1
            while(len(mpp)>2):
                mpp[arr[left]]-=1
                if(mpp[arr[left]]==0):
                    del mpp[arr[left]]
                left+=1
            if(len(mpp)<=2):
                maxLen=max(maxLen,(right-left+1))
            right+=1
        return maxLen
