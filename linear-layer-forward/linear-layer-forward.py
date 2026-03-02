def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    x_len = len(X)
    input_dim = len(W)
    output_dim = len(W[0])
    Y = [[0 for _ in range(output_dim)] for _ in range(x_len)]
    for i in range(x_len):
        for j in range(output_dim):
            for k in range(input_dim):
                Y[i][j] += X[i][k] * W[k][j]
            Y[i][j] += b[j]
            
    return Y