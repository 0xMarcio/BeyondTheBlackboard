import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Parameters
num_nodes = 100
prob_edge = 0.02
infection_prob = 0.05
recovery_time = 10
num_steps = 50

# Create a random graph
G = nx.erdos_renyi_graph(num_nodes, prob_edge)
status = {node: "susceptible" for node in G.nodes}
status[0] = "infected"  # Patient zero

# SIR model in a network
def update_status(G, status, recovery_time):
    new_status = status.copy()
    for node in G.nodes:
        if status[node] == "infected":
            if np.random.rand() < infection_prob:
                for neighbor in G.neighbors(node):
                    if status[neighbor] == "susceptible":
                        new_status[neighbor] = "infected"
            new_status[node] = "recovered" if recovery_time[node] <= 0 else "infected"
            recovery_time[node] -= 1
    return new_status

# Initialize recovery times
recovery_times = {node: recovery_time for node in G.nodes}

# Animation function
def animate(i):
    global status
    status = update_status(G, status, recovery_times)
    colors = ['red' if status[node] == 'infected' else 'green' if status[node] == 'recovered' else 'gray' for node in G.nodes]
    ax.clear()
    nx.draw(G, pos, node_color=colors, node_size=50, ax=ax)
    ax.set_title(f"Step: {i+1}")

# Positioning the nodes using Fruchterman-Reingold algorithm
pos = nx.spring_layout(G)

# Create a figure
fig, ax = plt.subplots(figsize=(8, 6))

# Create and run the animation
ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=300)
plt.show()
