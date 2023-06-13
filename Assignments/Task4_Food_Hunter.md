## Task 4: Overview
On the **Food-5K** dataset, we will attempt to visualize various interpretability techniques. You are free to use any other dataset you want. The goal of this work is to train a model (from scratch or from a pretrained one) for use on your new dataset xAI task. 
The Food-5K dataset's default task is classification. For the interpretability techniques, you can write your own code or use online resources.

This script should do two things:
1. Outputs the probability of the input image containing food
2. Localizes the food in the image

### Prerequisites
Before you begin, make sure you have the needed dependencies installed. More may be required depending on your use case, but below are few useful dependencies to have installed in your environment.

- Python 3.x
- PyTorch/Tensorflow
- torchvision
- matplotlib
- NumPy

### Dataset Preparation
To use the Food-5K dataset, follow these steps:

1. Download the [Food-5K dataset](http://mmspg.epfl.ch/food-image-datasets), a food vs not-food model is trained by fine-tuning InceptionV3 in Keras. Alternatively, download the dataset from the Kaggle website: Food-5K dataset.
2. Extract the dataset archive into a directory of your choice.
3. Organize the dataset into two main folders: train and test. Within each folder, create subfolders for each class/category of food. For example, if your dataset has 10 categories of food, you should have 10 subfolders within the train and test folders.
4. The Food-5K dataset has 2 classes, those being Food and Not Food. So you need to make two subfolders in each train and test.
5. Split your dataset into training and testing sets. Generally, an 70-30 split is recommended. Ensure that the distribution of classes is maintained in both sets.
* Class Activation Map (CAM) is technique that could be implemented here for food localization [http://cnnlocalization.csail.mit.edu].

### Objective
Use the dataset to train a model. The model may be made from scratch or pretrained model from here: [https://s3-us-west-2.amazonaws.com/models-a-c-ozbek/model_food.h5] Put the model file in the same level folder of the script. The dataset choice is left upto your discretion. 
The idea is to showcase the activation map around the region of food present in the image. In simple terms, showcase the predictive performance of the model for food category or objective of your choice.


#### Useful resources
- https://github.com/jacobgil/pytorch-grad-cam
- https://pytorch.org/vision/stable/models.html
- https://www.kaggle.com/datasets/trolukovich/food5k-image-dataset
