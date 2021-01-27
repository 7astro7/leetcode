
class palindromeNumber {

    // Determine whether an integer is a palindrome. An integer is a palindrome 
    // when it reads the same backward as forward.

    //Follow up: Could you solve it without converting the integer to a string?
    //Constraints: -2**31 <= x <= 2**31 - 1

    //static int num = 999;
    //static int num = 39128;
    //static int num = 9999;
    //static int num = 121;
    //static int num = -121;
    //static int num = 10;
    static int num = -101;
    
    public static boolean isPalindrome(int x) {

        boolean negative = x / 1 < 0, tooBig = x > Integer.MAX_VALUE, tooSmall = x < Integer.MIN_VALUE;
        if (negative || tooBig || tooSmall) { // x / 1 is an easy way to check for pos. via double-negative 
            return false;
        }
        String[] xSplitString = ("" + x).split("");
        int n = xSplitString.length;
        int[] xSplit = new int[n];
        for (int i = 0; i < n; i++) {
            xSplit[i] = Integer.parseInt(xSplitString[i]);
        }
        for (int i = 0; i < n; i++) {
            int oppo = xSplit[n - i - 1];
            System.out.println(oppo);
            if (oppo != xSplit[i]) {
                return false;
            }
        }
        return true;
    } 

    public static void main(String[] args) {

        boolean answer = isPalindrome(num);
        System.out.println(answer);
    }

}

