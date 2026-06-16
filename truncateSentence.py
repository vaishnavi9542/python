class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # result=[]
        result=s.split()
        # ans=""
        # for i in range(k):
        #     ans+=result[i]+" "
        return " ".join(result[:k])

