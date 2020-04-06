[//]: # (Image References)

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
+ [dog_app.ipynb](https://github.com/Data-Semi/dog-project-CNN/blob/master/dog_app.ipynb)  
+ [dog_app.html](https://github.com/Data-Semi/dog-project-CNN/blob/master/dog_app.html)  
+ [dogbreed_webapp](https://github.com/Data-Semi/dog-project-CNN/tree/master/dogbreed_webapp)  
[dogbreed_webapp](https://github.com/Data-Semi/dog-project-CNN/tree/master/dogbreed_webapp) folder includes a web application which has the same algorithm with above Jupyter notebooks.  
The web program can be used as below.  
Drag&Drop an image file on the web page (index.html), it will give an answer as below.  
- if a dog is detected in the image, return the predicted breed.  
- if a human is detected in the image, return the resembling dog breed.  
- if neither is detected in the image, provide an output that indicates an error.  
You can use the web application here: https://cnn-resnet50-dogbreed-detector.herokuapp.com/    
About the web application, please refer to this readme file. [dogbreed_webapp\Readme.rm](https://github.com/Data-Semi/dog-project-CNN/blob/master/dogbreed_webapp/Readme.rm)   
 
![Web Application Example][image4]  

## More insights for this project
The output is better than I expected, the accuracy is 80%! I think I can improve my algorithm with below 3 points.  

+ Use image augmentation to get better accuracy.  
+ Pre process the image to make it more clear before any other process.  
+ Skip dog_detectorto judge there is a dog or not, just use the result of Resnet50_predict_breed to see the top probability is larger than 50% or not. For example, if Resnet50_predict_breed returns a breed and the probability is larger than 50%,than return as a dog breed, else return there is no dog inside the image file.  
For more information overall this project , please refer to folked original [README_folked.md](https://github.com/Data-Semi/dog-project-CNN/blob/master/README_folked.md)  
