class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        all_combs = [''] if digits else []
        for digit in digits:
            current_comb = list()
            for letter in interpret_digit[digit]:
                for comb in all_combs:
                    current_comb.append(comb + letter)
            all_combs = current_comb
        return all_combs