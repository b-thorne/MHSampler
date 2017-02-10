import numpy as np
import matplotlib.pyplot as plt

class markov_chain(object):
    """Markov chain object"""
    def __init__(self, position, output_file_path):        
        self.position = position
        self.output_file_path = output_file_path
        self.chain = [position]
        return
    
    def update_position(self, position):
        self.position = position
        return

    def add_to_chain(self):
        self.chain.append(self.position)
        return
        
    def save_chain(self):
        np.savetxt(self.output_file_path, np.c_[self.chain], fmt = "%.5g")
        return

    def plot_chain(self):
        fig = plt.figure(figsize = (5, 5))
        ax = fig.add_subplot(111)
        ax.plot(self.chain)
        plt.show()
        plt.close()
        return

    def plot_hist(self, range, nbins = 100):
        plt.hist(self.chain, range = range, bins = nbins)
        plt.show()

    
def step(markov_chain):
    """Generate a proposal step."""
    prop = proposal(markov_chain.position)
    """Check if this satisifies the acceptance 
    criteria."""
    if acceptance(markov_chain.position, prop, likelihood):
        markov_chain.update_position(prop)
    else:
        markov_chain.update_position(markov_chain.position)
    """Add this new step to the chain."""
    markov_chain.add_to_chain()
    return

def acceptance(position, proposal, likelihood):
    """Check if the proposed value should be
    accepted. Needs a proposal value and 
    likelihood. Note currently assumes a 
    summetric proposal distribution. Need to 
    update to general proposal distribution to be 
    a M-H sampler."""
    prob = np.min([1., likelihood(proposal) / likelihood(position)])
    alpha = np.random.uniform(0, 1)
    if alpha <= prob:
        return True
    else:
        return False
    
def likelihood(theta):
    """An example one parameter likelihood"""
    return 1. / np.sqrt(2. * np.pi * 5.) * np.exp(- 0.5 * (theta - 20.) ** 2 / 5. ** 2)

                  
def proposal(center):
    """A symmetric proposal density for one
    dimension"""
    return np.random.normal(center, scale = 1., size = 1)
