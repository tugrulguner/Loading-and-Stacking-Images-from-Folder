Function 'imreadandresffold(path, fileextension, sizeh, sizew, operation)' in 'imageloadandresize.py' above reads image files in any given folder path in stacked form as 4 dimensional data where first dimension corresponds to the total sample and remaining to the image sizes and color channel. It can help you to put resulting data directly into any Deep Learning architecture as training dataset. Images are normalized during the process.

I write this function especially to be able to read https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia dataset. 

For example, in training folder, there are 2 folders NORMAL and PNEUMONIA. I read all jpeg files using 'all' in my function. However, there are bacteria and virus related images in PNEUMONIA folder. In order to collect all bacteria related ones, I use 'person\*\_bacteria\_\*' and for virus related ones, I use 'person\*\_virus\_\*' as string for operation variable in the function. 

Example use:

imdatanorm = imreadandresffold(path, 'jpeg', 128, 128, 'all') *** Reads all jpeg files   
imdatapne_bac = imreadandresffold(path, 'jpeg', 128, 128, 'person\*\_bacteria\_\*') *** Reads bacteria related jpeg files  
imdatapne_vir = imreadandresffold(path, 'jpeg', 128, 128, 'person\*\_virus\_\*') *** Reads virus related jpeg files  

Resizing the image file reading in folder is essential to be able to stack them. Otherwise, it is not possible to stack them in array format, that's why we have resize option in this function.
