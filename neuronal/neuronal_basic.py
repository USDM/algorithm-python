import numpy as np

# Función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación
def sigmoid_derivative(x):
    return x * (1 - x)

# Conjunto de datos de entrenamiento (compuerta lógica XOR)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Inicialización de pesos y bias de la capa oculta y la capa de salida
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
bias_hidden = np.zeros((1, hidden_neurons))


weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))
bias_output = np.zeros((1, output_neurons))

# Entrenamiento de la red neuronal
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # Capa de entrada a capa oculta
    hidden_layer_input = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    # Capa oculta a capa de salida
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = sigmoid(output_layer_input)

    # Cálculo del error
    error = targets - output_layer_output

    # Backpropagation y ajuste de pesos
    d_output = error * sigmoid_derivative(output_layer_output)
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# Prueba de la red neuronal
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
test_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights_input_hidden) + bias_hidden), weights_hidden_output) + bias_output)

print(test_output)
