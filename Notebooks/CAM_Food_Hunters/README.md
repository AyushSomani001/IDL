This script does two things:</br>
[1]	Outputs the probability of the input image containing food </br>
[2] Localizes the food in the image </br>




By using Food-5K dataset (http://mmspg.epfl.ch/food-image-datasets), a food vs not-food model is trained by fine-tuning InceptionV3 in Keras

[http://cnnlocalization.csail.mit.edu] The technique here is implemented for food localization. (Class Activation Mapping)


You can download the model from here: [https://s3-us-west-2.amazonaws.com/models-a-c-ozbek/model_food.h5] Put the model file in the same level folder of the script.
