def canWalkFromTopToBottom(dayAt):
            grid = [[0] * col for _ in range(row)]  # Create grid in the `dayAt` th date
            for i in range(dayAt):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # Mark as water

            bfs = deque([])
            for c in range(col):
                if grid[0][c] == 0:  # Add all valid start cells in the top row
                    bfs.append((0, c))
                    grid[0][c] = 1  # Mark as visited

            while bfs:
                r, c = bfs.popleft()
                if r == row - 1: return True  # Reach to bottom -> Return Valid
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == col or grid[nr][nc] == 1: continue
                    grid[nr][nc] = 1  # Mark as visited
                    bfs.append((nr, nc))
            return False

        left, right = 1, len(cells)

        ans = 0