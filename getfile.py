import numpy as np

from numpy import loadtxt
from numpy import savetxt

from pathlib import Path

#Supported formats: .dat and .txt
def write_array(filename, data):
  filename = Path(filename)
  name = "data.dat"
  return savetxt(name, data)

#Supported formats: .dat and .txt
def read_array(filename):
  filename = Path(filename)
  data = loadtxt(filename)
  return data
  
