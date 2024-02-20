import numpy as np
import scipy

def test_stats_beta():
    thresholds = np.linspace(0, 1, 11)
    beta_parameters = (2, 18)

    outs = scipy.stats.beta.cdf(thresholds, beta_parameters[0], beta_parameters[1])

    assert False, outs


def test_stats_boltzmann():

    x = np.arange(20)
    prior = scipy.stats.boltzmann.pmf(x, 2, len(x))

    assert False, prior
