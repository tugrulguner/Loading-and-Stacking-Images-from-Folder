import cv2
import numpy as np
import glob

def imreadandresffold(path, fileextension, sizeh, sizew, operation):
  if operation is 'all':
    imdata= np.stack([cv2.resize(cv2.imread(file), (sizeh,sizew), interpolation = cv2.INTER_NEAREST) for file in glob.glob(path+'/*.'+ fileextension)])
  if operation is 'specific':
    imdata= np.stack([cv2.resize(cv2.imread(file), (sizeh,sizew), interpolation = cv2.INTER_NEAREST) for file in glob.glob(path+'/'+ specific + '.' + fileextension)])
  return imdata
