Reads image files in any given folder path in stacked form as 4 dimensional data where first dimension corresponds to the samples and remaining for image size and color channel. It can help you put resulting data directly to Deep Learning architecture as training dataset.

I write this function especially to be able to read https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia dataset. 

For example, in training folder, there are 2 folders NORMAL and PNEUMONIA. I read all jpeg files using 'all' in my function. However, there are bacteria and virus related images in PNEUMONIA folder. In order to collect all bacteria related ones, I use 'person\*\_bacteria\_\*' and for virus related ones, I use 'person\*\_virus\_\*' as string for operation variable in the function. 
