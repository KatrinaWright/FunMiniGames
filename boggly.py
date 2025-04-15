import tkinter as tk
from itertools import product
import random

class Boggle:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.chains = []
        self.numbers = self.generate_numbers()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.frame, width=200, height=200)
        self.canvas.pack()
        self.draw_grid()

        self.label = tk.Label(self.master, text="Chains found:")
        self.label.pack()

        self.listbox = tk.Listbox(self.master)
        self.listbox.pack()
        self.listbox.bind('<<ListboxSelect>>', self.select_chain)

        self.find_all_chains()

    def generate_numbers(self):
        numbers = {}
        for i, j in product(range(4), repeat=2):
            numbers[i, j] = str(random.randint(1, 9))
        return numbers

    def draw_grid(self):
        for i, j in product(range(4), repeat=2):
            x, y = j*50, i*50
            self.canvas.create_text(x+25, y+25, text=self.numbers[i, j])

    def find_all_chains(self):
        for i, j in product(range(4), repeat=2):
            chains = self.find_chains(i, j)
            for chain in chains:
                if chain not in self.chains:
                    self.chains.append(chain)
                    self.listbox.insert(tk.END, ' -> '.join(self.numbers[x, y] for x, y in chain))

    def find_chains(self, i, j, chain=None, current_sum=0):
        if chain is None:
            chain = []
        if (i, j) in chain:
            return []
        chain.append((i, j))
        current_sum += int(self.numbers[i, j])
        if current_sum == 15:
            return [chain]
        if current_sum > 15:
            return []
        chains = []
        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if (x, y) in self.numbers:
                chains.extend(self.find_chains(x, y, chain[:], current_sum))
        return chains

    def select_chain(self, event):
        selected = self.listbox.curselection()
        if selected:
            chain = self.chains[selected[0]]
            self.canvas.delete("all")
            self.draw_grid()
            for i, (i, j) in enumerate(chain):
                x, y = j*50, i*50
                self.canvas.create_rectangle(x, y, x+50, y+50, outline='green')
            for i in range(len(chain)-1):
                x1, y1 = chain[i][1]*50+25, chain[i][0]*50+25
                x2, y2 = chain[i+1][1]*50+25, chain[i+1][0]*50+25
                self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)

root = tk.Tk()
my_game = Boggle(root)
root.mainloop()