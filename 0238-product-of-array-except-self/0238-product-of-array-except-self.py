class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # n=len(nums)
        # res=[1]*n
        # # Left
        # l=1
        # for i in range(n):
        #     res[i]=l
        #     l*=nums[i]
        
        # # Right
        # r=1
        # for i in range(n-1,-1,-1):
        #     res[i]*=r
        #     r*=nums[i]
        # return res

        n = len(nums)

        prefix=[1]*n
        suffix=[1]*n
        answer=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]

        for i in range(n):
            answer[i]=prefix[i]*suffix[i]
        
        return answer