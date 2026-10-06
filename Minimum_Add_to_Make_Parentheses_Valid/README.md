# Minimum_Add_to_Make_Parentheses_Valid

Can you solve this real interview question? Minimum Add to Make Parentheses Valid - A parentheses string is valid if and only if:

 * It is the empty string,
 * It can be written as AB (A concatenated with B), where A and B are valid strings, or
 * It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

 * For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

 

Example 1:


Input: s = "())"
Output: 1


Example 2:


Input: s = "((("
Output: 3


 

Constraints:

 * 1 <= s.length <= 1000
 * s[i] is either '(' or ')'.

---

## Metadata

- Language: python3
- Difficulty: Medium
- Acceptance: 74.2
- Tags: 
- URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=daily-question&envId=2026-10-06

## Files

- Minimum_Add_to_Make_Parentheses_Valid.py
