import tkinter as tk
from tkinter import ttk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Vizualizare Sortare - Selection Sort")

        # Configurare interfață
        self.array = []
        self.speed = 0.1
        self.max_elements = 50

        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.pack()

        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Număr elemente:").grid(row=0, column=0)
        self.num_elements = tk.IntVar(value=20)
        self.num_elements_slider = ttk.Scale(control_frame, from_=5, to=self.max_elements, variable=self.num_elements, orient="horizontal")
        self.num_elements_slider.grid(row=0, column=1, padx=5)

        ttk.Label(control_frame, text="Viteză:").grid(row=1, column=0)
        self.speed_var = tk.DoubleVar(value=0.1)
        self.speed_slider = ttk.Scale(control_frame, from_=0.01, to=1.0, variable=self.speed_var, orient="horizontal")
        self.speed_slider.grid(row=1, column=1, padx=5)

        ttk.Button(control_frame, text="Generare valori aleatorii", command=self.generate_array).grid(row=2, column=0, pady=5)
        ttk.Button(control_frame, text="Începe Sortare", command=self.start_sorting).grid(row=2, column=1, pady=5)
        ttk.Button(control_frame, text="Reset", command=self.reset).grid(row=2, column=2, pady=5)

        self.generate_array()

    def generate_array(self):
        self.array = [random.randint(1, 100) for _ in range(self.num_elements.get())]
        self.draw_array()

    def draw_array(self, color_map=None):
        self.canvas.delete("all")
        canvas_width = 800
        canvas_height = 400
        bar_width = canvas_width / len(self.array)
        max_height = max(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - (value / max_height * canvas_height)
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            color = color_map[i] if color_map else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        self.root.update()

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            # Evidențierea elementului curent și a minimului curent
            color_map = ["green" if x == i else "yellow" if x == min_idx else "blue" for x in range(len(self.array))]
            self.draw_array(color_map)
            time.sleep(self.speed_var.get())

            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
                # Evidențierea comparației curente
                color_map = ["green" if x == i else "yellow" if x == min_idx else "red" if x == j else "blue" for x in range(len(self.array))]
                self.draw_array(color_map)
                time.sleep(self.speed_var.get())

            # Schimbă elementele
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

        # Evidențiere finală
        self.draw_array(["green" for _ in range(len(self.array))])

    def start_sorting(self):
        self.selection_sort()

    def reset(self):
        self.generate_array()

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
