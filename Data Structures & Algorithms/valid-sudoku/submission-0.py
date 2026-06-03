class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                rowMarker = (r, 'row', num)
                colMarker = (c, 'col', num)
                boxMarker = (r//3, c//3, 'box', num)

                if rowMarker in seen or colMarker in seen or boxMarker in seen:
                    return False

                seen.add(rowMarker)
                seen.add(colMarker)
                seen.add(boxMarker)
        return True
