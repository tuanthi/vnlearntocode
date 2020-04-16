# Day 15: Product of Array Except Self

Link: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

```
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
```

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


**Solution's direction:** 

Sample input: arr = [1,2,3,4]

1. Create an array with value: [1, arr[0], arr[0]*arr[1], arr[0]*arr[1]*arr[2]]
2. create another array with value: [arr[2]*arr[1]*arr[0], arr[1]*arr[0], arr[0], 1]
3. Run a for loop. The product of two array's values at each index is the product of the other elements except itself in the inital array. 

This sample's output: [24,12,8,6]

###### This post is contributed by Christopher Le