Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

<h4>Example 1:</h4>

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

<h4>Example 2:</h4>
Input: nums = [3,2,4], target = 6
Output: [1,2]

<h4>Example 3:</h4>
Input: nums = [3,3], target = 6
Output: [0,1]
 

<h4>Constraints:</h4>

2 <= nums.length <= 104\n
-109 <= nums[i] <= 109\n
-109 <= target <= 109\n
Only one valid answer exists.
