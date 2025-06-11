import random
from matematicas import Matematicas

class MLP:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        for i in range(len(layers) - 1):
            # Xavier/Glorot initialization using Matematicas.sqrt
            limit = Matematicas.sqrt(6 / (layers[i] + layers[i + 1]))
            w = [[random.uniform(-limit, limit) for _ in range(layers[i])] for _ in range(layers[i + 1])]
            b = [random.uniform(-limit, limit) for _ in range(layers[i + 1])]
            self.weights.append(w)
            self.biases.append(b)

    def sigmoid(self, x):
        # Handle large inputs to avoid Matematicas.exp(x > 10) errors
        if x > 10:
            return 0.0  # exp(-x) is negligible, sigmoid ≈ 0
        if x < -10:
            return 1.0  # exp(-x) is large, sigmoid ≈ 1
        return 1 / (1 + Matematicas.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        a = inputs
        for w, b in zip(self.weights, self.biases):
            z = [sum(w[i][j] * a[j] for j in range(len(w[0]))) + b[i] for i in range(len(w))]
            a = [self.sigmoid(x) for x in z]
        return a

    @staticmethod
    def crear_mlp(layers):
        return MLP(layers)

    @staticmethod
    def entrenar_mlp(model, data, labels, epochs, lr):
        # Flatten labels if they are [[0], [1], ...] to [0, 1, ...]
        labels = [label[0] if isinstance(label, list) else label for label in labels]
        for _ in range(epochs):
            for x, y in zip(data, labels):
                # Forward pass
                activations = [x]
                z_values = []
                for w, b in zip(model.weights, model.biases):
                    z = [sum(w[i][j] * activations[-1][j] for j in range(len(w[0]))) + b[i] for i in range(len(w))]
                    a = [model.sigmoid(zi) for zi in z]
                    activations.append(a)
                    z_values.append(z)

                # Backward pass
                output = activations[-1]
                # Delta for output layer
                deltas = [(output[i] - y if i == 0 else 0) * model.sigmoid_derivative(output[i]) for i in range(len(output))]

                # Update output layer
                for i in range(len(model.weights[-1])):
                    for j in range(len(model.weights[-1][i])):
                        model.weights[-1][i][j] -= lr * deltas[i] * activations[-2][j]
                    model.biases[-1][i] -= lr * deltas[i]

                # Update hidden layers
                for l in range(len(model.weights) - 2, -1, -1):
                    new_deltas = []
                    for i in range(len(model.weights[l])):
                        error = sum(model.weights[l + 1][k][i] * deltas[k] for k in range(len(model.weights[l + 1])))
                        delta = error * model.sigmoid_derivative(activations[l + 1][i])
                        new_deltas.append(delta)
                        for j in range(len(model.weights[l][i])):
                            model.weights[l][i][j] -= lr * delta * activations[l][j]
                        model.biases[l][i] -= lr * delta
                    deltas = new_deltas

    @staticmethod
    def predecir_mlp(model, inputs):
        return model.forward(inputs)

@staticmethod
def kmeans(points, k, max_iters=100):
    if not points or k < 1 or k > len(points):
        raise ValueError("Parámetros inválidos para K-means")
    centroids = points[:k]
    clusters = [[] for _ in range(k)]
    for _ in range(max_iters):
        clusters = [[] for _ in range(k)]
        for p in points:
            distances = [sum((p[j] - c[j])**2 for j in range(len(p))) for c in centroids]
            cluster_idx = distances.index(min(distances))
            clusters[cluster_idx].append(p)
        new_centroids = []
        for cluster in clusters:
            if not cluster:
                new_centroids.append(points[0])
                continue
            n = len(cluster)
            new_centroid = [sum(p[j] for p in cluster) / n for j in range(len(cluster[0]))]
            new_centroids.append(new_centroid)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters