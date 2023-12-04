import numpy as np
from scipy.linalg import expm, kron
import plotly.graph_objects as go

# Define Pauli and Hadamard matrices
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, -1j], [1j, 0]])
pauli_z = np.array([[1, 0], [0, -1]])
hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Define the CNOT gate
def cnot(control, target, num_qubits):
    """Create a CNOT gate for a specified control and target qubit in a system with num_qubits."""
    mask = 1 << target | 1 << control
    gate = np.eye(2**num_qubits)
    for i in range(2**num_qubits):
        if i & mask == 1 << control:
            i_swapped = i ^ (1 << target)
            gate[i, i], gate[i, i_swapped] = 0, 1
    return gate

# Function to apply a gate to the system
def apply_gate(gate, state):
    return gate @ state

# Initial state |000⟩
initial_state = np.array([1] + [0]*7)

# Create a complex initial state using Hadamard and CNOT gates
state = apply_gate(cnot(1, 2, 3), apply_gate(cnot(0, 1, 3), apply_gate(kron(hadamard, kron(hadamard, hadamard)), initial_state)))

# Time evolution with combined Pauli gates
time_points = np.linspace(0, 4*np.pi, 100)
evolved_states = [apply_gate(kron(expm(-1j * pauli_x * t), kron(expm(-1j * pauli_y * t), expm(-1j * pauli_z * t))), state) for t in time_points]

# Probabilities of all possible states
prob_states = np.abs(evolved_states)**2

# Plotting
fig = go.Figure()
for idx in range(8):
    label = f'|{"{:03b}".format(idx)}⟩'
    fig.add_trace(go.Scatter(x=time_points, y=prob_states[:, idx], mode='lines', name=label))

fig.update_layout(title='Three-Qubit State Probabilities Over Time',
                  xaxis_title='Time',
                  yaxis_title='Probability',
                  legend_title='States')
fig.show()

