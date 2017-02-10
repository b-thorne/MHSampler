import numpy as np
import matplotlib.pyplot as plt

class markov_chain(object):
    """Markov chain object"""
    def __init__(self, position, max_steps, output_file_path):        
        self.position = position
        self.output_file_path = output_file_path
        self.max_steps = max_steps
        self.chain = [position]
        return
    
    def update_position(self, position):
        self.position = position
        return

    def add_to_chain(self, position):
        self.chain.append(position)
        return
        
    def save_chain(self):
        np.savetxt(self.output_file_path, np.c_[self.chain], fmt = "%.5"g)
        return

    def plot_density(self):
        return

    def plot_chain(self):
        fig = plt.figure(figsize = (5, 5))
        ax = fig.add_subplot(111)
        ax.plot(self.chain)
        plt.show()

class manager(object):

    def __init__(self):
        return
        
def likelihood(theta):
    """An example one parameter likelihood"""
    2. * np.cos(4. * np.pi * theta) ** 2
    return

def proposal(center):
    """A symmetric proposal density for one
    dimension"""
    return np.random.normal(center, scale = 1., size = 1.)
