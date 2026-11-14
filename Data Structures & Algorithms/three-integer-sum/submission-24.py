class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_output=[]
        for i in range(len(nums)-2):

            nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1

            while left<right:

                if nums[left]+nums[right]+nums[i]==0:
                    
                    if left>i+1 and nums[left]==nums[left-1]:
                      left=left+1
                    elif right<len(nums)-1 and nums[right]==nums[right+1]:
                       right=right-1

                    else:
                        final_output.append([nums[i],nums[left],nums[right]])
                        left=left+1
                        right=right-1

                elif nums[left]+nums[right]+nums[i]< 0:
                    left=left+1
                else:
                    right-=1
            
        
        return final_output
                



        
        
        
                


        