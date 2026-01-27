from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        balance = 0
        sum_to_index = {0: -1} 

        for i in range(len(nums)):
            balance += 1 if nums[i] == 1 else -1
            
            if balance in sum_to_index:
                prev_index = sum_to_index[balance]
                current_len = i - prev_index
                max_len = max(max_len, current_len)
            else:
                sum_to_index[balance] = i
                
        return max_len