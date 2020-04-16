class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Calculate the product of other elements of the array, except itself.

        Args:
          nums: the input array.

        Returns:
          An array output such that output[i] is equal to
          the product of all the elements of nums except nums[i].
          
        """
        result = [1]
        current = 1
        
        for i in range(len(nums)-1): 
            current *= nums[i]
            result.append(current)
            
        current = 1
        for i in range(len(nums)-1, -1, -1): 
            result[i] *= current
            current *= nums[i]
            
        return result