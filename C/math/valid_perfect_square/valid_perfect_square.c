#include <stdio.h>
#include <stdbool.h>
#include <math.h>

/*
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
    1 <= num <= 2^31 - 1
*/

bool is_perfect_square(int num) 
{
    double sq_rt = pow(num, .5);
    double remainder = fmod(sq_rt, 1);
    if (remainder == 0) 
        return true;
    return false;
}

int main()
{
    int num = 46225;
    bool a = is_perfect_square(num);
    printf("answer: %d\n", a);
    return 0;
}

