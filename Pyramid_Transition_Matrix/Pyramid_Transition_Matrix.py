class Solution(object):

    def pyramidTransition(self, bottom, allowed):
        f = collections.defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            for i in itertools.product(*(f[a][b] for a, b in zip(bottom, bottom
[1:]))):
                if pyramid(i): return True
            return False
        return pyramid(bottom)