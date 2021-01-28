
package leetFindNumsEvenNumDigits;

class findNumsEvenNumDigits {

	public int findNumbers(int[] nums) {
		int i = 0, countEven = 0;
		while (i < nums.length) {
			int len = Integer.valueOf(nums[i]).toString().length();
			if (len % 2 == 0) {
				countEven++;
			}
			i++; 
		}
		return countEven;
	}
}
