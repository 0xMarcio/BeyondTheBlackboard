import matplotlib.pyplot as plt

def plot_nuclear_reaction(reactants, products):
    """
    Plot a simple representation of a nuclear reaction.

    Parameters:
    reactants (dict): Dictionary containing reactants with their respective quantities.
    products (dict): Dictionary containing products with their respective quantities.
    """
    # Labels and values for reactants and products
    reactant_labels = list(reactants.keys())
    reactant_values = list(reactants.values())
    product_labels = list(products.keys())
    product_values = list(products.values())

    # Creating subplots for reactants and products
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plotting the reactants
    ax1.bar(reactant_labels, reactant_values, color='blue')
    ax1.set_title('Reactants')
    ax1.set_ylabel('Quantity')
    ax1.set_xlabel('Elements/Particles')

    # Plotting the products
    ax2.bar(product_labels, product_values, color='green')
    ax2.set_title('Products')
    ax2.set_ylabel('Quantity')
    ax2.set_xlabel('Elements/Particles')

    plt.suptitle('Nuclear Reaction Representation')
    plt.show()

# Example nuclear reaction: Uranium-235 fission
reactants = {'Uranium-235': 1, 'Neutron': 1}
products = {'Krypton-92': 1, 'Barium-141': 1, 'Neutrons': 3}

# Plotting the nuclear reaction
plot_nuclear_reaction(reactants, products)
