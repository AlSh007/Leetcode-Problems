class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]