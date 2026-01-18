for c in range(n):
                preSumRow[r][c + 1] = preSumRow[r][c] + grid[r][c]
                preSumCol[c][r + 1] = preSumCol[c][r] + grid[r][c]

        def getSumRow(row, l, r):  # row, l, r inclusive
            return preSumRow[row][r + 1] - preSumRow[row][l]

        def getSumCol(col, l, r):  # row, l, r inclusive
            return preSumCol[col][r + 1] - preSumCol[col][l]

        def test(k):

            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    diag, antiDiag = 0, 0
                    for d in range(k):