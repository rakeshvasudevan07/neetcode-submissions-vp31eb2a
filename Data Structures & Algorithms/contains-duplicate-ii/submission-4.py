class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windo=set()
        L=0
        for R in range(len(nums)):
            if R-L> k:
                windo.remove(nums[L])
                L+=1
            if nums[R] in windo:
                return True
            windo.add(nums[R])
        return False

        