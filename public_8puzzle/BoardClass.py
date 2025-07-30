import random
import queue
import time
import csv
import heapq  # Needed for A* Search
from typing import List, Tuple, Optional

class BoardClass():
    """NxN board to solve [(N^2)-1]-puzzle"""
    
    N = 3
    GOAL = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def __init__(self, board: Optional[List[List[int]]] = None):
        self.Board: List[List[int]] = board if board else generate_random_board()
        self.X, self.Y = self.find_empty_tile()
        self.Parent: Optional[BoardClass] = None
        self.Heuristic: float = float('inf')
        self.Moves: int = 0  # Track number of moves
        
        # Initialize GoalTiles as an instance variable
        self.GoalTiles: dict[int, Tuple[int, int]] = {BoardClass.GOAL[row][col]: (row, col)
                          for row in range(BoardClass.N) for col in range(BoardClass.N)}

    def find_empty_tile(self) -> Tuple[int, int]:
        for row in range(BoardClass.N):
            for col in range(BoardClass.N):
                if self.Board[row][col] == 0:
                    return row, col
        return -1, -1

    def copyCTOR(self) -> 'BoardClass':
        """Creates a copy of the board"""
        newBoard = BoardClass([row[:] for row in self.Board])
        newBoard.X, newBoard.Y = self.X, self.Y
        newBoard.Parent = self
        newBoard.Moves = self.Moves + 1  # Increment move count
        return newBoard
    
    def createChildrenBoards(self) -> List['BoardClass']:
        """Generates all possible child boards by moving the empty tile (0)."""
        row, col = self.X, self.Y
        newChildrenBoards = []

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # (UP, DOWN, LEFT, RIGHT)
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < BoardClass.N and 0 <= new_col < BoardClass.N:
                newBoard = self.copyCTOR()
                newBoard.Board[row][col], newBoard.Board[new_row][new_col] = (
                    newBoard.Board[new_row][new_col],
                    newBoard.Board[row][col],
                )
                newBoard.X, newBoard.Y = new_row, new_col
                newChildrenBoards.append(newBoard)

        return newChildrenBoards

    def computeDistanceFromGoal(self) -> int:
        """Computes Manhattan Distance"""
        return sum(abs(row - self.GoalTiles[tile][0]) + abs(col - self.GoalTiles[tile][1])
                   for row in range(BoardClass.N) for col in range(BoardClass.N)
                   if (tile := self.Board[row][col]) != 0)

    def getHeuristic_MisplacedTiles(self) -> int:
        """Computes misplaced tiles heuristic"""
        return sum(1 for row in range(BoardClass.N) for col in range(BoardClass.N)
                   if self.Board[row][col] != 0 and self.Board[row][col] != BoardClass.GOAL[row][col])

    def __lt__(self, other: 'BoardClass') -> bool:
        """Defines comparison for priority queue (heapq) in A* Search."""
        return (self.computeDistanceFromGoal() + self.Moves) < (other.computeDistanceFromGoal() + other.Moves)


def BestFirstSearch(startingBoard: BoardClass, Verbose: bool = True) -> Tuple[int, int, int, float]:
    """Solves the 8-puzzle using Best-First Search and logs statistics"""
    
    Q = queue.PriorityQueue()
    numberOfItemsAddedToQueue = 0  
    max_queue_size = 0
    visited_count = 0

    startingBoard.Heuristic = startingBoard.getHeuristic_MisplacedTiles()
    Q.put((startingBoard.Heuristic, numberOfItemsAddedToQueue, startingBoard))
    numberOfItemsAddedToQueue += 1

    Visited = set()
    foundSolution = False
    final_moves = 0
    step_times = []  # Log execution time per step

    while not Q.empty():
        start_time = time.time()
        max_queue_size = max(max_queue_size, Q.qsize())
        _, _, currentBoard = Q.get()
        visited_count += 1
        Visited.add(tuple(map(tuple, currentBoard.Board)))
        step_times.append(time.time() - start_time)

        if currentBoard.Board == BoardClass.GOAL:
            foundSolution = True
            final_moves = currentBoard.Moves
            break

        for child in currentBoard.createChildrenBoards():
            if tuple(map(tuple, child.Board)) not in Visited:
                child.Heuristic = child.getHeuristic_MisplacedTiles()
                Q.put((child.Heuristic, numberOfItemsAddedToQueue, child))
                numberOfItemsAddedToQueue += 1

    if foundSolution:
        print(f"DONE!! 8-Puzzle solved in {final_moves} moves using Best-First Search.")

    avg_step_time = sum(step_times) / len(step_times) if step_times else 0
    return final_moves, max_queue_size, visited_count, avg_step_time


def AStarSearch(startingBoard: BoardClass, verbose: bool = True) -> Tuple[int, int, int, float]:
    """Solves the 8-puzzle using A* Search Algorithm and logs statistics."""
    
    open_list = []
    heapq.heappush(open_list, (startingBoard.computeDistanceFromGoal(), 0, startingBoard))
    closed_set = set()
    max_queue_size = 0
    visited_count = 0
    step_times = []

    while open_list:
        start_time = time.time()
        max_queue_size = max(max_queue_size, len(open_list))
        _, cost, currentBoard = heapq.heappop(open_list)
        visited_count += 1
        closed_set.add(tuple(map(tuple, currentBoard.Board)))
        step_times.append(time.time() - start_time)

        if currentBoard.Board == BoardClass.GOAL:
            print(f"DONE!! 8-Puzzle solved in {cost} moves using A* Search.")
            return cost, max_queue_size, visited_count, sum(step_times) / len(step_times) if step_times else 0

        for child in currentBoard.createChildrenBoards():
            if tuple(map(tuple, child.Board)) not in closed_set:
                heapq.heappush(open_list, (child.computeDistanceFromGoal() + cost + 1, cost + 1, child))

    return float('inf'), max_queue_size, visited_count, 0


def is_solvable(board: List[List[int]]) -> bool:
    """Check if a given board is solvable based on inversion count."""
    flat_board = [tile for row in board for tile in row if tile != 0]
    inversions = sum(1 for i in range(len(flat_board)) for j in range(i + 1, len(flat_board)) if flat_board[i] > flat_board[j])
    return inversions % 2 == 0  # Solvable if inversion count is even


def generate_random_board() -> List[List[int]]:
    """Generates a random 3x3 board, ensuring only solvable configurations."""
    while True:
        tiles = list(range(9))
        random.shuffle(tiles)
        board = [tiles[i:i+3] for i in range(0, 9, 3)]
        if is_solvable(board):
            return board
