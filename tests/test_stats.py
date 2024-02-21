import numpy as np
import scipy

def test_stats_beta():
    thresholds = np.linspace(0, 1, 101)
    beta_parameters = (2, 18)

    outs = scipy.stats.beta.cdf(thresholds, beta_parameters[0], beta_parameters[1])

    assert False, outs
