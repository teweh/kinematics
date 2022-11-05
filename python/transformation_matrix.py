import numpy as np
from numpy import pi
from math import cos, sin, radians

def trig(r, degree=False):
  if (degree==True):
    r = radians(angle)
  return cos(r), sin(r)

def tf_matrix(rotation, translation):
  xC, xS = trig(rotation[0])
  yC, yS = trig(rotation[1])
  zC, zS = trig(rotation[2])
  dX = translation[0]
  dY = translation[1]
  dZ = translation[2]
  Translate_matrix = np.array([[1, 0, 0, dX],
                               [0, 1, 0, dY],
                               [0, 0, 1, dZ],
                               [0, 0, 0, 1]])

  Rotate_X_matrix = np.array([[1, 0,  0,   0],
                              [0, xC, -xS, 0],
                              [0, xS, xC,  0],
                              [0, 0,  0,   1]])

  Rotate_Y_matrix = np.array([[yC,  0, yS, 0],
                              [0,   1, 0,  0],
                              [-yS, 0, yC, 0],
                              [0,   0, 0,  1]])

  Rotate_Z_matrix = np.array([[zC, -zS, 0, 0],
                              [zS, zC,  0, 0],
                              [0,  0,   1, 0],
                              [0,  0,   0, 1]])
  rotate_x = np.dot(Rotate_X_matrix, Translate_matrix)
  rotate_xy = np.dot(Rotate_Y_matrix, rotate_x)
  rotate_xyz = np.dot(Rotate_Z_matrix, rotate_xy)
  return rotate_xyz

# Unit vector x
vector_x=[1,0,0]

# Unit vector y
vector_y=[0,1,0]

# Unit vector z
vector_z=[0,0,1]

print(pi)

rotation_x=[pi/2, 0,    0]

rotation_y=[0,    -pi/2, 0]

rotation_z=[0,    0,    pi/2]


print(vector_x)
# apply rotation and translation
print(tf_matrix(rotation_y, vector_x))

# transform a vector
vector_z.append(1)
print(np.dot(tf_matrix(rotation_y, vector_x), vector_z))
