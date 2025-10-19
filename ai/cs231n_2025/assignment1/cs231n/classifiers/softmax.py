from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    # compute the loss and the gradient
    num_classes = W.shape[1]
    num_train = X.shape[0]
    for i in range(num_train):
        scores = X[i].dot(W)

        # compute the probabilities in numerically stable way
        scores -= np.max(scores)
        p = np.exp(scores)
        p /= p.sum()  # normalize
        logp = np.log(p)

        loss -= logp[y[i]]  # negative log probability is the loss
        for j in range(num_classes):
          dW[:, j] += X[i] * (p[j] - (j == y[i]))
  
    # normalized hinge loss plus regularization
    loss = loss / num_train + reg * np.sum(W * W)
    dW /= num_train
    dW += 2 * reg * W

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    N = X.shape[0]

    scores = X.dot(W)
    scores -= np.reshape(np.max(scores, axis=1), (-1, 1))
    p = np.exp(scores)
    p /= p.sum(axis=1, keepdims=True)
    loss = -np.log(p[np.arange(N), y])
    loss = loss.mean() + reg * np.sum(W*W)

    dscores = p.copy()
    dscores[np.arange(N), y] -= 1
    dscores /= N

    dW = X.T @ dscores + 2 * reg * W

    return loss, dW
