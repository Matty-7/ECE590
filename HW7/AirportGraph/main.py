import tkinter as tk
from tkinter import ttk
import sys

#
# GUI for selecting the start and end point for graph traversal algorithm
# between the 40 airports, and selecting one of the three algorithms to be executed:
# Breadth First Search, Depth First Search, or Dijkstra's Shortest Path
#
class AirportGraphAlgoMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.to_label = None
        self.master = master
        self.pack()

        # a list of all 20 airports
        self.states = ["ATL", "AUS", "BOS", "BWI", "DCA","DEN",
                       "DFW", "DTW", "EWR", "IAD", "IAH", "JFK",
                       "LAS", "LAX", "MDW", "MIA", "MSP", "PDX",
                       "PHL", "RDU", "SAN", "SEA", "SFO", "SLC"]

        # a list of 3 algorithms for user to select
        self.algo_choices = ["BFS", "DFS", "Dijkstra"]

        self.create_widgets()

    def create_widgets(self):
        self.from_label = tk.Label(self, text="From:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5)
        self.from_view = ttk.Combobox(self, values=self.states)
        self.from_view.grid(row=0, column=1, padx=5, pady=5)

        self.to_label = tk.Label(self, text="To:")
        self.to_label.grid(row=1, column=0, padx=5, pady=5)
        self.to_view = ttk.Combobox(self, values=self.states)
        self.to_view.grid(row=1, column=1, padx=5, pady=5)

        self.algo_label = tk.Label(self, text="Algorithm:")
        self.algo_label.grid(row=2, column=0, padx=5, pady=5)
        self.algo_choice_view = ttk.Combobox(self, values=self.algo_choices)
        self.algo_choice_view.grid(row=2, column=1, padx=5, pady=5)

        self.run_button = tk.Button(self, text="Run", command=self.run_algorithm)
        self.run_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def run_algorithm(self):
        from_airport = self.from_view.get()
        to_airport = self.to_view.get()
        algorithm = self.algo_choice_view.get()

        if algorithm == "BFS":
            self.bfs(from_airport, to_airport)
        elif algorithm == "DFS":
            self.dfs(from_airport, to_airport)
        elif algorithm == "Dijkstra":
            self.sp(from_airport, to_airport)

    # Placeholder functions for bfs
    # replace the body with a call to your algorithm implementation
    def bfs(self, from_airport, to_airport):
        print(f"BFS selected: from {from_airport} to {to_airport}")

    # Placeholder functions for bfs
    # replace the body with a call to your algorithm implementation
    def dfs(self, from_airport, to_airport):
        print(f"DFS selected: from {from_airport} to {to_airport}")

    # Placeholder functions for bfs
    # replace the body with a call to your algorithm implementation
    def sp(self, from_airport, to_airport):
        print(f"Dijkstra SP selected: from {from_airport} to {to_airport}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Airports and Algorithm Selection")
    app = AirportGraphAlgoMenu(master=root)
    app.mainloop()
