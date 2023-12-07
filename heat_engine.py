import matplotlib.pyplot as plt

def calculate_efficiency(heat_input, heat_output):
    """
    Calculate the efficiency of a heat engine.

    Parameters:
    heat_input (float): Heat input to the engine (in Joules).
    heat_output (float): Heat output or work done by the engine (in Joules).

    Returns:
    float: Efficiency of the engine (as a percentage).
    """
    # Efficiency: e = (heat input - heat output) / heat input
    efficiency = (heat_input - heat_output) / heat_input
    return efficiency * 100

def plot_heat_engine(heat_input, heat_output):
    """
    Plot a basic diagram of a heat engine.

    Parameters:
    heat_input (float): Heat input to the engine (in Joules).
    heat_output (float): Heat output or work done by the engine (in Joules).
    """
    # Labels for the plot
    labels = ['Heat Input (Q_in)', 'Work Done (W)', 'Heat Output (Q_out)']
    sizes = [heat_input, heat_output, heat_input - heat_output]
    colors = ['gold', 'lightgreen', 'lightcoral']
    explode = (0.1, 0, 0)

    # Plotting
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Heat Engine Diagram")
    plt.show()

# Example values for a heat engine
heat_input = 500  # Heat input in Joules
heat_output = 300  # Heat output or work done in Joules

# Calculate the efficiency
efficiency = calculate_efficiency(heat_input, heat_output)

# Plotting the heat engine
plot_heat_engine(heat_input, heat_output)

efficiency
