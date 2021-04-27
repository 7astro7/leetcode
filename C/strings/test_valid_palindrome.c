#include <criterion/criterion.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

/*
Given a string s, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
*/

bool 
is_palindrome(char * s)
{
    bool alnum = false;
    int n = strlen(s);
    char simplified[n];
    int i, j = 0;
    for (i = 0; i < n; i++)
    {
        alnum = isalnum(s[i]);
        if (alnum)
        {
            simplified[j++] = tolower(s[i]);
        }
    }
    int new_n = j;
    i = 0;
    while (1)
    {
        if (i >= new_n)
        {
            return true;
        }
        if (simplified[i++] != simplified[j - i])
        {
            return false;
        }
    }
}

Test(test_valid_palindrome, one_char_returns_true)
{
    cr_assert(is_palindrome("G"));
}

Test(test_valid_palindrome, panama_canal_returns_true)
{
    cr_assert(is_palindrome("A man, a plan, a canal: Panama"));
}

Test(test_valid_palindrome, salmon_returns_false)
{
    cr_assert(!is_palindrome("SALMON"));
}

Test(test_valid_palindrome, hannah_returns_true)
{
      cr_assert(is_palindrome("Hannah"));
}

Test(test_valid_palindrome, matrix_returns_false)
{
      cr_assert(!is_palindrome("matrix"));
}

Test(test_valid_palindrome, 90509_returns_true)
{
      cr_assert(is_palindrome("90509"));
}

Test(test_valid_palindrome, madam_im_adam_returns_true)
{
      cr_assert(is_palindrome("Madam I'm Adam"));
}

Test(test_valid_palindrome, greek_thing_returns_true)
{
      cr_assert(is_palindrome("ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ"));
}

Test(test_valid_palindrome, mr_owl_returns_true)
{
      cr_assert(is_palindrome("Mr. Owl ate my metal worm"));
}

Test(test_valid_palindrome, mr_bowl_returns_false)
{
      cr_assert(!is_palindrome("Mr. Bowl ate my metal worm"));
}

