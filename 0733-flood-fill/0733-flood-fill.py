class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIR = [0,1,0,-1,0]
        old_col, m, n = image[sr][sc], len(image), len(image[0])
        if old_col != color:
            q = collections.deque([(sr,sc)])
            while q:
                r,c = q.popleft()
                image[r][c] = color
                for i in range(4):
                    nr = r + DIR[i]
                    nc = c + DIR[i+1]
                    if 0<= nr < m and 0<= nc <n and image[nr][nc] == old_col:
                        q.append((nr,nc))
        return image