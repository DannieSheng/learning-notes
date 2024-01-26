# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.stats import norm
import numpy as np
import math

def get_p_pool(X1, X2, N1, N2):
    p_pool = (X1+X2)/(N1+N2)
    return p_pool

def get_SE_pool(p_pool, N1, N2):
    SE_pool = np.sqrt(p_pool*(1-p_pool)*(1/N1+1/N2))
    return SE_pool


def get_z_star(alpha):
    z_star = -norm.ppf(alpha/2)
    return z_star

def get_beta(z_star, s, d_min, N):
    SE = s/np.sqrt(N)
    beta = norm.cdf(z_star * SE, loc=d_min, scale=SE)
    return beta

def get_required_size(s, d_min, Ns=np.arange(1, 20001), alpha=0.05, beta=0.2):
    for N in Ns:
        if get_beta(get_z_star(alpha), s, d_min, N) < beta:
            return N
        else:
            continue
  
p_pool     = 0.1
s          = np.sqrt(p_pool*(1-p_pool)*(1/1 + 1/1))
d_min      = 0.02
required_N = get_required_size(s, d_min, Ns=np.arange(1, 20001), alpha=0.05, beta=0.2)

s_= 0.0119 #0.00515 # measured when N = 5000
N = 5000
s = s_ * np.sqrt(N)
d_min = 0.02

required_N = get_required_size(s=s, d_min=d_min, Ns=np.arange(1, 20001))





N      = 5000
alpha  = 0.05
beta   = 0.2
SE1    = 0.0202
SE2    = 0.0549
SE3    = 0.0156
d_min1 = 0.01
d_min2 = 0.01
d_min3 = 0.0075

# not using bonferroni Correction

required_N_1 = get_required_size(s=SE1 * np.sqrt(N), d_min=d_min1, Ns=np.arange(10, 400000,100), alpha=alpha, beta=beta)

required_N_2 = get_required_size(s=SE2 * np.sqrt(N), d_min=d_min2, Ns=np.arange(10, 400000,100), alpha=alpha, beta=beta)

required_N_3 = get_required_size(s=SE3 * np.sqrt(N), d_min=d_min3, Ns=np.arange(10, 400000,100), alpha=alpha, beta=beta)

# using Bonferroni Correction
alpha_indi = alpha/3
required_N_1 = get_required_size(s=SE1 * np.sqrt(N), d_min=d_min1, Ns=np.arange(10, 320000,100), alpha=alpha_indi, beta=beta)

required_N_2 = get_required_size(s=SE2 * np.sqrt(N), d_min=d_min2, Ns=np.arange(10, 320000,100), alpha=alpha_indi, beta=beta)

required_N_3 = get_required_size(s=SE3 * np.sqrt(N), d_min=d_min3, Ns=np.arange(10, 320000,100), alpha=alpha_indi, beta=beta)


#### lesson 4 example
alpha = 0.05
beta  = 0.2
d_min = 0.02
N     = 5000

# by pageview
SE = 0.00515
required_n1 = get_required_size(s=SE*np.sqrt(N), d_min=d_min, Ns=np.arange(1, 15000), alpha=alpha, beta=beta)

# by cookie
SE = 0.0119
required_n2 = get_required_size(s=SE*np.sqrt(N), d_min=d_min, Ns=np.arange(1, 15000), alpha=alpha, beta=beta)

SE    = 0.0628
N     = 1000
d_min = 0.01
required_n2_ = get_required_size(s=SE*np.sqrt(N), d_min=d_min, Ns=np.arange(1, 350000, 10), alpha=alpha, beta=beta)




