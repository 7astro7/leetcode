
package majority_element;
import java.util.HashMap;
import java.util.Map;

/*
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5e4
    -2**31 <= nums[i] <= 2**31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
*/


class Solution {
	
	public int majorityElement(int[] nums) {
		HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>(); 
		for (int i = 0; i < nums.length; i++) {
			if (freq.containsKey(nums[i])) {
				int newCount = freq.get(nums[i]) + 1;
				freq.replace(nums[i], newCount);
			}
			else {freq.put(nums[i], 1);}
		}
		int modeKey = nums[0], modeVal = freq.get(nums[0]);
		for (Map.Entry<Integer, Integer> mapping: freq.entrySet()) {
			if (mapping.getValue() > modeVal) {
				modeKey = mapping.getKey();
				modeVal = mapping.getValue();
			}
		}
		return modeKey;
	}
}
