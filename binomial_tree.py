from math import exp, sqrt
import numpy as np

def binomial_tree(s, k, t, v, rf, cp, jr, am:False, n=100):
  """Price option with binomial trees and Cox, Ross and Rubinstein (1979) formula"""
  #Cálculos iniciais
  h=t/n
  if jr==1:
    u=exp((rf-0.5*v**2)*h+v*sqrt(h))
    d=exp((rf-0.5*v**2)*h-v*sqrt(h))
  else:
    u=exp(v*sqrt(h))
    d=exp(-v*sqrt(h))
  
  drift=exp(rf*h)
  q=(drift-d)/(u-d)
  
  #Process the terminal stock price
  stkval = np.zeros((n+1,n+1))
  optval = np.zeros((n+1,n+1))
  stkval[0,0] = s

  for i in range(1, n+1):
    stkval[i,0] = stkval[i-1,0]*u
    for j in range (1, n+1):
      stkval[i,j] = stkval[i-1,j-1]*d
  
  #Backward recursion for option price
  # REVER ESSA PARTE
  for j in range(n + 1):
    optval[n,j] = max(0,cp*(stkval[n,j]-k))
    for i in range(n-1,-1,-1):
      for j in range(i+1):
        optval[i,j] = (q*optval[i+1,j]+(1-q)*optval[i+1,j+1])/drift
        if am:
          optval[i,j] = max(optval[i,j],cp*(stkval[i,j]-k))
  return optval[0,0]
