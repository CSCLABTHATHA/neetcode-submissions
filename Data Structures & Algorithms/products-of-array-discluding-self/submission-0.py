class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = [1], [1]
        ans = []
        for i in range(1, len(nums)):
            pref.append(pref[i-1] * nums[i-1])
            suff.append(suff[i-1] * nums[-i])

        for i in range(len(nums)):
            ans.append(pref[i] * suff[-i-1])

        return ans