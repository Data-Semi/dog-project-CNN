﻿[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Keras Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"
[image4]: ./dogbreed_webapp/webappSnap.PNG "Web Application Example"


## Project Overview  
This is a Convolutional Neural Networks (CNN) project in the Data-Scientist Nanodegree.  
I have learned how to build a pipeline that can be used within a web app to process real-world, user-supplied images.    
Given an image of a dog, this algorithm will identify an estimate of the canine’s breed.  If supplied an image of a human, the code will identify the resembling dog breed.   
I choose to use ResNet-50 for transfer learning in this project.

The libraries I used are Numpy, Tensorflow, OpenCV, Flask, PIL.      
Please refer to the [dogbreed_webapp/requirements.txt](https://github.com/Data-Semi/dog-project-CNN/blob/master/dogbreed_webapp/requirements.txt) file for detail.  

Files in the repository:  
I have folked from udacity/dog-project, and added below files and folder.  
+ [dog_app_report_20200406.ipynb](https://github.com/Data-Semi/dog-project-CNN/blob/master/dog_app_report_20200406.ipynb)  
+ [dog_app_report_20200406.html](https://github.com/Data-Semi/dog-project-CNN/blob/master/dog_app_report_20200406.html)  
+ [dogbreed_webapp](https://github.com/Data-Semi/dog-project-CNN/tree/master/dogbreed_webapp)  
[dogbreed_webapp](https://github.com/Data-Semi/dog-project-CNN/tree/master/dogbreed_webapp) folder includes an web application which have same algorithm with above Jupyter notebooks.  
The web program will be action as below.  
Drag&Drop a image file on the web page (index.html), it will give an answer as below.  
- if a dog is detected in the image, return the predicted breed.  
- if a human is detected in the image, return the resembling dog breed.  
- if neither is detected in the image, provide output that indicates an error.  
You can use the web application here: https://cnn-resnet50-dogbreed-detector.herokuapp.com/    
About the web application,please refer to this readme file. [dogbreed_webapp\Readme.rm](https://github.com/Data-Semi/dog-project-CNN/blob/master/dogbreed_webapp/Readme.rm)   
 
![Web Application Example][image4]  

For more information overall this project , please refer to folked original [README_folked.md](https://github.com/Data-Semi/dog-project-CNN/blob/master/README_folked.md)  
