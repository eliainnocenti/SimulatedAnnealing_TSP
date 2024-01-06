import matplotlib.pyplot as plt
import numpy as np
from matrix1 import matrix1

def plot_graph(incidence_matrix):
    # Ottieni il numero di nodi dalla dimensione della matrice di incidenza
    num_nodes = len(incidence_matrix)

    # Crea una figura per il grafico e una griglia per la tabella
    fig, (ax_graph, ax_table) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 1]})

    # Crea un dizionario per tenere traccia delle posizioni dei nodi
    node_positions = {}

    # Calcola la posizione di ciascun nodo sul cerchio
    for node in range(num_nodes):
        angle = 2 * np.pi * node / num_nodes
        x = np.cos(angle)
        y = np.sin(angle)
        node_positions[node] = (x, y)

    # Disegna gli archi
    for i in range(num_nodes):
        for j in range(num_nodes):
            if incidence_matrix[i][j] != 0:
                ax_graph.arrow(node_positions[i][0], node_positions[i][1],
                               node_positions[j][0] - node_positions[i][0],
                               node_positions[j][1] - node_positions[i][1],
                               head_width=0.1, head_length=0.1,
                               length_includes_head=True, fc='black', ec='black')

    # Disegna i nodi
    for node, position in node_positions.items():
        ax_graph.add_patch(plt.Circle(position, 0.1, color='white', ec='black'))
        ax_graph.text(position[0], position[1], str(node), ha='center', va='center')

    # Imposta i limiti dell'asse per centrare il grafico
    ax_graph.set_xlim(-1.5, 1.5)
    ax_graph.set_ylim(-1.5, 1.5)
    ax_graph.set_aspect('equal')
    ax_graph.axis('off')

    # Mostra la matrice di incidenza come tabella
    ax_table.table(cellText=incidence_matrix, loc='center', cellLoc='center', colLabels=np.arange(num_nodes),
                   rowLabels=np.arange(num_nodes), colColours=['lightgray'] * num_nodes, rowColours=['lightgray'] * num_nodes)
    ax_table.axis('off')

    # Imposta il titolo della tabella
    ax_table.set_title('Matrice di Incidenza')

    # Mostra il grafico
    plt.show()

# Esempio di matrice di incidenza
# Sostituisci questa con la tua matrice
incidence_matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

plot_graph(matrix1)
