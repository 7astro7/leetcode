
class romanToInteger {

    //Given a roman numeral, convert it to an integer.
    //Example 1:
    //Input: s = "III"
    //Output: 3
    
    //Example 2:
    //Input: s = "IV"
    //Output: 4
    
    //Example 3:
    //Input: s = "IX"
    //Output: 9

    //Example 4:
    //Input: s = "LVIII"
    //Output: 58
    //Explanation: L = 50, V= 5, III = 3.
    
    //Example 5:
    //Input: s = "MCMXCIV"
    //Output: 1994
    //Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    //Constraints:
    //1 <= s.length <= 15
    //s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    //It is guaranteed that s is a valid roman numeral in the range [1, 3999].

    //Roman numerals are usually written largest to smallest from left to right. 
    //However, the numeral for four is not IIII. Instead, the number four is written 
    //as IV. Because the one is before the five we subtract it making four. The same 
    //principle applies to the number nine, which is written as IX. There are six 
    //instances where subtraction is used:

    //I can be placed before V (5) and X (10) to make 4 and 9. 
    //X can be placed before L (50) and C (100) to make 40 and 90. 
    //C can be placed before D (500) and M (1000) to make 400 and 900.

    
    //static String s = "III";
    //static String s = "IV";
    //static String s = "IX";
    //static String s = "LXVIII";
    //static String s = "MCMXCIV"; // 1994
    //static String s = "MMMDCXIX"; //3619
    //static String s = "MMCCCLXXI"; // 2371 
    //static String s = "MMMCCCL"; // 3350
    //static String s = "DCCCLXXXIII"; // 883 
    //static String s = "CDLXXVIII"; // 478
    //static String s = "CDIV"; // 404
    static String s = "CDXIV"; // 414
    static String[] key = {"I", "V", "X", "L", "C", "D", "M"};
    static int[] value = {1, 5, 10, 50, 100, 500, 1000};

    public static int romanToInt(String s) {

       String[] sArr = s.split("");
       int n = sArr.length, sum = 0;
       int[] sIntArr = new int[n];
       for (int i = 0; i < n; i++) {
           if (sArr[i].contains(key[0])) {
            sIntArr[i] = value[0]; 
           }
           else if (sArr[i].contains(key[1])) {
            sIntArr[i] = value[1]; 
           }
           else if (sArr[i].contains(key[2])) {
            sIntArr[i] = value[2]; 
           }
           else if (sArr[i].contains(key[3])) {
            sIntArr[i] = value[3]; 
           }
           else if (sArr[i].contains(key[4])) {
            sIntArr[i] = value[4]; 
           }
           else if (sArr[i].contains(key[5])) {
            sIntArr[i] = value[5]; 
           }
           else if (sArr[i].contains(key[6])) {
            sIntArr[i] = value[6]; 
        }
       }
        if (n == 1) {
           return sIntArr[0];
        }
        int i = 0;
        while (i < n - 1) {
            if (sIntArr[i] < sIntArr[i + 1]) {
                sum += sIntArr[i + 1] - sIntArr[i];
                i++; i++;
               }
            else {
                sum += sIntArr[i];
                i++;
            }
       }
       if (sIntArr[n - 2] >= sIntArr[n - 1]) {
           sum += sIntArr[n - 1];
       }
       return sum;
    }

    public static void main(String[] args) {

        int roman = romanToInt(s);
        System.out.println(roman);

    }

}


