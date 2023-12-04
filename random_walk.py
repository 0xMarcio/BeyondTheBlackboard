import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Parameters
num_steps = 100
x = np.zeros(num_steps)
y = np.zeros(num_steps)

# Generate random walk data
np.random.seed(0)
for i in range(1, num_steps):
    x[i] = x[i - 1] + np.random.normal()
    y[i] = y[i - 1] + np.random.normal()

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Create an animation frame
frames = [go.Frame(data=[go.Scatter(x=x[:k], y=y[:k], mode='lines+markers')], name=f'frame{k}',) for k in range(1, num_steps)]

# Create the initial plot
scatter_trace = go.Scatter(x=x[:1], y=y[:1], mode='lines+markers')
fig.add_trace(scatter_trace)

# Define layout
layout = go.Layout(title="Random Walk Animation",
                   xaxis=dict(range=[min(x), max(x)]),
                   yaxis=dict(range=[min(y), max(y)]),
                   showlegend=False)

# Add animation frames to the figure
fig.frames = frames

# Set up animation settings
animation_settings = go.layout.Updatemenu(type="buttons", showactive=False, buttons=[
    go.layout.updatemenu.Button(label="Play",
                                method="animate",
                                args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)]),
    go.layout.updatemenu.Button(label="Pause",
                                method="animate",
                                args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')]),
])

layout.updatemenus = [animation_settings]

# Set layout and display the figure
fig.update_layout(layout)
fig.show()
