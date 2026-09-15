class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for a in nums:
            if a in hashmap:
                return True
            else:
                hashmap.add(a) 
                continue
        return False
            
