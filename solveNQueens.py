class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        def isSafe(r,c,board):
            for i in range(r-1,-1,-1):
                if board[i][c]=="Q":
                    return False
            row,col=r-1,c-1
            while row>-1 and col>-1:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            row,col=r-1,c+1
            while row>-1 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True
        def backtrack(row,n,board,res):
            if row==n:
                res.append(["".join(row) for row in board])
                return
            for col in range(n):
                if isSafe(row,col,board):
                    board[row][col]="Q"
                    backtrack(row+1,n,board,res)
                    board[row][col]="."
        backtrack(0,n,board,res)
        return res
