import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# Function to draw the selected type of graph
def draw_graph():
    x_values = [float(x_entry.get()) for x_entry in x_entries]
    y_values = [float(y_entry.get()) for y_entry in y_entries]
    
    selected_graph = graph_type.get()
    
    plt.figure(figsize=(6, 4))
    
    if selected_graph == "Line Plot":
        plt.plot(x_values, y_values, marker='o')
    elif selected_graph == "Scatter Plot":
        plt.scatter(x_values, y_values)
    elif selected_graph == "Bar Plot":
        plt.bar(x_values, y_values)
    elif selected_graph == "Histogram":
        plt.hist(y_values, bins=10)
    
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title(selected_graph)
    plt.show()  # Display the plot in a Matplotlib window

# Create the main window
root = tk.Tk()
root.title("Graph Plotter")

# Create frames
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10, side=tk.LEFT)

# Create X and Y input labels and entry fields
x_label = ttk.Label(input_frame, text="X Values:")
x_label.grid(row=0, column=0, sticky=tk.W)

y_label = ttk.Label(input_frame, text="Y Values:")
y_label.grid(row=1, column=0, sticky=tk.W)

x_entries = []
y_entries = []

for i in range(5):
    x_entry = ttk.Entry(input_frame)
    x_entry.grid(row=0, column=i+1, padx=5, pady=5)
    x_entries.append(x_entry)

    y_entry = ttk.Entry(input_frame)
    y_entry.grid(row=1, column=i+1, padx=5, pady=5)
    y_entries.append(y_entry)

# Create a combo box for selecting graph type
graph_type_label = ttk.Label(input_frame, text="Select Graph Type:")
graph_type_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)

graph_type = ttk.Combobox(input_frame, values=["Line Plot", "Scatter Plot", "Bar Plot", "Histogram"])
graph_type.grid(row=2, column=2, columnspan=4, padx=5, pady=5)
graph_type.set("Line Plot")

# Create a button to draw the graph
draw_button = ttk.Button(input_frame, text="Draw Graph", command=draw_graph)
draw_button.grid(row=3, columnspan=6, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()