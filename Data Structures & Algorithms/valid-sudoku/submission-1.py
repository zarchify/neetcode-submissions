class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValidRow(h: int) -> bool:
            seen = set()
            for item in board[h]:
                if item in seen:
                    return False
                if item != ".":
                    seen.add(item)
            return True
        def isValidColumn(w: int) -> bool:
            seen = set()
            for i in range(9):
                item = board[i][w]
                if item in seen:
                    return False
                if item != ".":
                    seen.add(item)
            return True
        def isValidSquare(w: int, h: int) -> bool:
            seen = set()
            for i in range(3):
                for j in range(3):
                    item = board[h+i][w+j]
                    if item in seen:
                        return False
                    if item != ".":
                        seen.add(item)
            return True
        

        for i in range(9):
            if not isValidColumn(i) or not isValidRow(i):
                return False
        for i in range(3):
            for j in range(3):
                if not isValidSquare(j * 3, i * 3):
                    return False
        return True


            

        