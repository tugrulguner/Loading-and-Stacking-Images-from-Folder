import cv2
import numpy as np
import glob

def imreadandresffold(path, fileextension, sizeh, sizew, operation):
  # path should be in the form of string standing for your folder path location like 'C://users/Folder/'. fileextension should be string like 'jpg', 'png', etc.
  # sizeh and sizew stand for desired height and width sizes of your images, they can be irregular sizes as raw data but you can resize them according sizeh and sizew values.
  # operation can take either 'all' or any specific string: use 'all' to take all image files specified with flieextension or use something else to select only certain files
  # satisfying your condition like if you want to select certain names 'person*_bacteria_*' which selects all the files containing person1, person2, person3, ..., etc
  # and including personx_bacteria_... Here as an example, this selects person1_bacteria_1, person2_bacteria_2, person2_bacteria_2am and so on. Only person and bacteria
  # are fixed here and places with * related to anything else.
  if operation is 'all':
    imdata= np.stack([cv2.resize(cv2.imread(file), (sizeh,sizew), interpolation = cv2.INTER_NEAREST) for file in glob.glob(path+'/*.'+ fileextension)])
  else:
    imdata= np.stack([cv2.resize(cv2.imread(file), (sizeh,sizew), interpolation = cv2.INTER_NEAREST) for file in glob.glob(path+'/'+ specific + '.' + fileextension)])
  return imdata
