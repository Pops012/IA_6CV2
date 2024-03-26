import heapq

def calcQueens(size):
    board = [-1] * size
    priority_queue = [(0, board, 0)]
    while priority_queue:
        cost, board, current = heapq.heappop(priority_queue)
        if current == size:
            return board
        for i in range(size):
            board[current] = i
            if noConflicts(board, current):
                new_cost = heuristic(board)
                heapq.heappush(priority_queue, (new_cost, board.copy(), current + 1))
    return board

def heuristic(board):
    h = 0
    size = len(board)
    for i in range(size):
        for j in range(i+1, size):
            if noConflicts(board, i) and noConflicts(board, j):
                h += 1
    return h

def noConflicts(board, current):
    for i in range(current):
        if board[i] == board[current] or abs(board[i] - board[current]) == current - i:
            return False
    return True

def printBoard(board):
    size = len(board)
    for row in board:
        line = '. ' * row + 'Q ' + '. ' * (size - row - 1)
        print(line)
    print("\n")

size = 7
board = calcQueens(size)
if board is not None:
    printBoard(board)
else:
    print("No solution found")
