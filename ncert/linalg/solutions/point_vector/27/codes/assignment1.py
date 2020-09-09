# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10G1loYi0Ny3KKkHhMLC2pMVYYLDCv1kS
"""

import math
import numpy as np

F = np.array([3,4,-5])
d = np.array([5,4,3])
scalarProd = np.inner(F,d)
Fval = np.linalg.norm(F)
dval = np.linalg.norm(d)
cosOfAngle = scalarProd / (Fval*dval)
angleinRad = math.acos(cosOfAngle)
angleinDeg = math.degrees(angleinRad)
print("The angle in degrees is",angleinDeg)