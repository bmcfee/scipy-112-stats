import numpy as np
import scipy
import os



def test_stats_beta():
    thresholds = np.linspace(0, 1, 101)
    beta_parameters = (2, 18)

    beta_cdf = np.load(os.path.join("tests", 'beta_cdf.npy'))

    outs = scipy.stats.beta.cdf(thresholds, beta_parameters[0], beta_parameters[1])

    assert np.all(outs == beta_cdf), outs - beta_cdf
