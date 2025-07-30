from typing import List, Optional
from BoardClass import BoardClass, BestFirstSearch, AStarSearch, is_solvable, generate_random_board

def get_user_board() -> Optional[List[List[int]]]:
    """Prompts the user to enter a custom board configuration."""
    print("Enter your custom 8-puzzle board row by row (use space between numbers, 0 represents the empty tile):")
    board = []
    for i in range(3):
        row_input = input(f"Row {i+1}: ").replace(",", " ")  # Allow both comma and space-separated input
        row = list(map(int, row_input.split()))
        if len(row) != 3:
            print("Invalid row length. Please enter exactly 3 numbers.")
            return None
        board.append(row)
    return board

def format_board(board: List[List[int]]) -> str:
    """Formats the board in a structured layout."""
    return "\n".join([
        "-------------",
        f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |",
        "-------------",
        f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |",
        "-------------",
        f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |",
        "-------------"
    ])

def main() -> None:
    """Main function to generate or input an 8-puzzle board and solve it."""
    choice = input("Do you want to enter a custom board? (y/n): ").strip().lower()
    if choice == 'y':
        board = None
        while board is None:
            board = get_user_board()
    else:
        board = generate_random_board()
    
    solvable = is_solvable(board)
    puzzle = BoardClass(board)
    
    manhattan_distance = puzzle.computeDistanceFromGoal()
    misplaced_tiles = puzzle.getHeuristic_MisplacedTiles()
    
    print("\nPuzzle Details:")
    print("Generated Board:")
    print(format_board(puzzle.Board))
    print(f"Manhattan Distance: {manhattan_distance}")
    print(f"Misplaced Tiles: {misplaced_tiles}")
    print(f"Is board solvable: {'YES' if solvable else 'NO'} (Even inversions: {'EVEN' if solvable else 'ODD'})")
    
    if solvable:
        algorithm_choice = input("Choose an algorithm to solve the puzzle - Best-First Search (B) or A* Search (A): ").strip().lower()
        
        if algorithm_choice == 'b':
            print("\nUsing Best-First Search to solve the puzzle...")
            solved = BestFirstSearch(puzzle)
            if solved:
                print("\nThe solved puzzle is:")
                print(format_board(BoardClass.GOAL))
            else:
                print("No solution found using Best-First Search.")
        
        elif algorithm_choice == 'a':
            print("\nUsing A* Search to solve the puzzle...")
            solved = AStarSearch(puzzle)
            if solved:
                print("\nThe solved puzzle is:")
                print(format_board(BoardClass.GOAL))
            else:
                print("No solution found using A* Search.")
        
        else:
            print("Invalid choice. Please restart and choose either 'B' for Best-First Search or 'A' for A* Search.")
    else:
        print("This board is not solvable.")

if __name__ == "__main__":
    main()