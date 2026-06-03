# from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                
               
                ans = min(ans, max(ws, ls + ld) + wd)

                ans = min(ans, max(ls, ws + wd) + ld)

        return ans
