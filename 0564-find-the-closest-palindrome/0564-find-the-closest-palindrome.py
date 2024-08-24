class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        N, n = len(n), int(n)
        def reflect(first_half):
            """if n is odd length reflect('12') = '121', otherwise reflect('12') = '1221'"""
            l = str(first_half)
            return l + l[: -(N % 2) or None][::-1]

        if N == 1:
            return str(n - 1)
        elif log10(n).is_integer() or log10(n - 1).is_integer():
            return (N - 1) * "9"
        elif log10(n + 1).is_integer():
            return "1" + "0" * (N - 1) + "1"

        left_half = int(str(n)[: (N + 1) // 2])
        left_half_uppered = left_half + 1
        left_half_lowered = left_half - 1

        return min(
            map(reflect, (left_half_lowered, left_half, left_half_uppered,)),
            key=lambda num: abs(n - int(num)) or float("inf"),
        )
        