import time
import csv
import matplotlib.pyplot as plt
from typing import List, Tuple
from BoardClass import BoardClass, BestFirstSearch, AStarSearch, is_solvable, generate_random_board

def run_experiment(trials: int = 1000) -> List[Tuple[int, float, int, float, int]]:
    """Runs experiments for a given number of trials and logs performance statistics."""
    results = []

    # 🔥 Print only a single status message instead of per iteration output
    print("\nSolving 8-puzzle using A* and Best-First Search and analyzing results... Loading...\n")

    for i in range(trials):
        # Generate a solvable board
        board = generate_random_board()
        while not is_solvable(board):
            board = generate_random_board()
        
        # Create independent puzzle instances for both algorithms
        puzzle_bfs = BoardClass(board)
        puzzle_astar = BoardClass(board)
        
        # Best-First Search (🔇 Silent mode)
        start_time = time.time()
        moves_bfs = BestFirstSearch(puzzle_bfs)  # ✅ Suppress prints
        time_bfs = time.time() - start_time
        
        # A* Search (🔇 Silent mode)
        start_time = time.time()
        moves_astar = AStarSearch(puzzle_astar)  # ✅ Suppress prints
        time_astar = time.time() - start_time
        
        # Store results
        results.append((i+1, time_bfs, moves_bfs, time_astar, moves_astar))
    
    # Save results to CSV
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Trial", "Time BFS", "Moves BFS", "Time A*", "Moves A*"])
        writer.writerows(results)
    
    return results

def generate_graphs(results: List[Tuple[int, float, int, float, int]]) -> None:
    """Generates performance comparison graphs for runtime and moves count."""
    trials = [row[0] for row in results]
    time_bfs = [row[1] for row in results]
    moves_bfs = [row[2] for row in results]
    time_astar = [row[3] for row in results]
    moves_astar = [row[4] for row in results]
    
    # Runtime comparison
    plt.figure()
    plt.plot(trials, time_bfs, label="Best-First Search", linestyle='--', marker='o', markersize=2)
    plt.plot(trials, time_astar, label="A* Search", linestyle='-', marker='x', markersize=2)
    plt.xlabel("Trial")
    plt.ylabel("Time (seconds)")
    plt.title("Time Comparison: Best-First Search vs A* Search")
    plt.legend()
    plt.grid(True)
    plt.savefig("runtime_comparison.png")
    
    # Moves comparison
    plt.figure()
    plt.plot(trials, moves_bfs, label="Best-First Search", linestyle='--', marker='o', markersize=2)
    plt.plot(trials, moves_astar, label="A* Search", linestyle='-', marker='x', markersize=2)
    plt.xlabel("Trial")
    plt.ylabel("Moves to Solve")
    plt.title("Move Count Comparison: Best-First Search vs A* Search")
    plt.legend()
    plt.grid(True)
    plt.savefig("moves_comparison.png")

def main() -> None:
    print("\nRunning experiments on 1000 solvable 8-puzzle boards...")
    results = run_experiment(1000)
    print("\nGenerating graphs and saving results...\n")
    generate_graphs(results)
    print("Done! Results saved to results.csv and graphs generated.")

if __name__ == "__main__":
    main()