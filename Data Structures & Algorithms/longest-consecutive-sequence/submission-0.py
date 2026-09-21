class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        ans = 0
        if lookup:
            t = 1
            temp = lookup.pop()
        else:
            return 0

        val = 1
        changetemp = temp
        while lookup:
            changetemp += val
            

            if changetemp in lookup:
                t += 1
                lookup.remove(changetemp)

            else:
                if val == -1:
                    ans = max(ans,t)
                    if lookup:
                        temp = lookup.pop()
                        val = 1
                        t = 1
                    else:
                        return ans
                else:
                    val = -1
                changetemp = temp
        return max(t,ans)