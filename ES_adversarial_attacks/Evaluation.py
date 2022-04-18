import numpy as np


class Evaluate:
    def worst_eval(self, minimize=True):
        """ Return worst possible evaluation
            That will be the initial value of the best evaluation in the ES
        """
        return np.inf if minimize else -np.inf

    def evaluate(self):
        pass


class Ackley(Evaluate):
    """ Evaluate a solution on Ackley problem
    """
    def __init__(self, a = 20, b = 0.2, c = 2*np.pi, minimize=True):
        self.a = a
        self.b = b
        self.c = c
        self.optimum = 0
        
    def evaluate(self, x):
        dim = len(x)
        term1 = -1. * self.a * np.exp(-1. * self.b * np.sqrt((1./dim) * sum(map(lambda i: i**2, x))))
        term2 = -1. * np.exp((1./dim) * (sum(map(lambda j: np.cos(self.c * j), x))))
        
        return (term1 + term2 + self.a + np.exp(1))


class Rastringin:
    """ Evaluate a solution on Rastringin problem
    """
    def __init__(self, a = 10, minimize=True):
        self.a = a
        self.optimum = 0
        
    def evaluate(self, x):
        y = self.a * len(x) + sum(map(lambda i: i**2 - self.a * np.cos(2*np.pi*i), x))
        return y


class ClassifierCrossentropy(Evaluate):
    """ Generic image classifier evaluator using cross entropy
    """
    def __init__(self, model, true_label, minimize=True, targeted=False):
        self.model = model
        self.true_label = int(true_label)
        self.minimize = minimize
        self.targeted = targeted

    def worst_eval(self):
        if not self.targeted:
            return 0
        else:
            return np.inf if self.minimize else -np.inf

    def evaluate_ind(self, noise, input_):
        """ if targeted attack, use crossentropy (-log(pred)) on target
            if untargeted attack, use negative crossentropy (log(pred)) on target
            opposite of above if minimize is False
        """
        # feasible input space contraint
        # if np.min(input_) < 0 or np.max(input_) > 1:
        #     return np.inf if self.targeted else 0
        # prediction
        predictions = self.model(np.expand_dims(noise + input_, axis=0))[0].numpy()
        # return loss
        if self.minimize:
            loss_sign = (-1 if self.targeted else 1)
        else:
            loss_sign = (1 if self.targeted else -1)
        return loss_sign * np.log(predictions[self.true_label])

    def evaluate(self, batch):
        """ if targeted attack, use crossentropy (-log(pred)) on target
            if untargeted attack, use negative crossentropy (log(pred)) on target
            opposite of above if minimize is False
        """
        # feasible input space contraint
        # if np.min(input_) < 0 or np.max(input_) > 1:
        #     return np.inf if self.targeted else 0
        # prediction
        predictions = self.model(batch).numpy()
        # return loss
        if self.minimize:
            loss_sign = (-1 if self.targeted else 1)
        else:
            loss_sign = (1 if self.targeted else -1)
        return loss_sign * np.log(predictions[:, self.true_label])