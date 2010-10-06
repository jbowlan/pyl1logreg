import scipy as sp
import scipy.linalg as la
import numpy as np
import pylab

# demo of least squares, ridge regression, LARS, logistic-regression (IRLS), and
# l1 - reg logistic regression

# these are written for simplicity, and not heavily optimized

"""
y - response variable - shape(y) = (1,N)
x - input variables - shape(x) = (p-1, N)
b - predictor variables - shape(b)= (1,p)
"""

def lin_ls(y, x):
    """
    linear least squares: min_b |y - dot(b.T,x)|^2    
    the algorithm for this involves a cholesky decomposition of dot(x.T,x)
    to find inv(dot(x.T,x))
    """
    
    
    
    
    return b




def lin_wls(y, x, w, gam):
    """
    weighted linear least squares
    
    
    """
    return b

def lin_ls_l2(y, x, gam):
    return b
    
def lr_irls(y, x):
    """
    binary logistic regression (unregularized)
    solved using Iteratively Reweighted Least Squares (IRLS)    
    """

    return b

def lr_irls_l2(y, x, gam):
    return b


def lin_lars(y, x, gam):
    """
    solution of l1-regularized linear regression problem with LARS
    """
    
    return b


