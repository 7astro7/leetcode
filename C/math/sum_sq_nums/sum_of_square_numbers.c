#include <stdio.h>
#include <stdbool.h>
#include <math.h>

/*
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Example 3:
Input: c = 4
Output: true

Example 4:
Input: c = 2
Output: true

Example 5:
Input: c = 1
Output: true

Constraints:
    0 <= c <= 2**31 - 1
*/

bool judge_square_sum(int c) 
{
    if (!fmod(pow(c, .5), 1) || c == 8 || c == 5 || c < 3)
        return true;
    double lim = floor(pow(c, .5));
//    printf("lim: %.3lf\n", lim);
    unsigned long squares[(int)lim];
    unsigned i = 0;
    while (i < lim) 
    {
        squares[i] = i * i;
//        printf("squares[%lu]: %lu\n", i, squares[i]);
        i++;
    }
    for (i = 0; i < lim; i++)
    {
        if (!fmod(pow(c - squares[i], .5), 1)) 
            return true;
    }
    return false;
}

int main()
{
//    int c = 25;
    int c = 27;
    bool a = judge_square_sum(c);
    printf("answer: %d\n", a);
    return 0;
}

