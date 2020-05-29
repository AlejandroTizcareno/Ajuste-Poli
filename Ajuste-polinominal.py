import numpy as np

def polyfit2(x,y,n):

  def inv(A):
    return np.linalg.inv(A)
  def trans(A):
    return A.getT()
  def prod(A,B):
    return np.dot(A,B)

  xlen = len(x)
  ylen = len(y)
  one = np.ones((xlen,n+1),dtype=int)
  c1=one[:,[1]]
  xT=np.matrix(x)
  yT=np.matrix(y)
  c2=xT.getT()
  c3=np.power(c2,2)
  A=np.hstack([c1,c2,c3])
  ajuste = prod(prod(inv(prod(trans(A),A)),trans(A)),trans(yT))
  print(ajuste)

x=[1.0,2.0,3.0,4.0,5.0]
y=[5.0,4.0,3.0,2.0,1.0]

polyfit2(x,y,2)