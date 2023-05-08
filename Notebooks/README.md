# Network Visualization Practice Notebooks

Here are some notebooks compiled to help users better utilize the library's capabilities:

| Notebook     |      Description      |   |
|:----------|:-------------|------:|
| [QuickTour](Torch-CAM/QuickTour.ipynb) | An overview of TorchCAM's primary features | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/AyushSomani001/IDL/Notebooks/Torch-CAM/QuickTour.ipynb) |
| [Grad-CAMs](Grad-CAMs.ipynb) | Visualizing and interpreting CNN model activations for object localization and model fine-tuning. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://github.com/AyushSomani001/IDL/Notebooks/Grad-CAMs.ipynb) |
| [CNN-Explainer](CNN_explainer.ipynb) | An interactive visualization system designed to help learn about CNNs | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/AyushSomani001/IDL/Notebooks/CNN_explainer.ipynb) |


# References - Research Papers


| Paper     |      Description      | Author  |
|:----------|:-------------|------:|
|[Learning deep features for discriminative localization.](https://openaccess.thecvf.com/content_cvpr_2016/papers/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf)| Introduces `CAM` by using global average pooling in convolutional neural networks to enable class-specific discriminative localization without requiring bounding box annotations during training. | Zhou et al. (2016) | 
| [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html) | Introduces `Grad-CAM`, a method that generalizes CAMs and provides better visual explanations for deep networks! | Selvaraju et al. (2016) |
| [Axiomatic Attribution for Deep Networks](http://proceedings.mlr.press/v70/sundararajan17a.html)| Presents `Integrated Gradients`, a technique that attributes the output of a deep network to its input features, providing a more comprehensive understanding of the model's decision-making process. | Sundararajan et al. (2017)|


# Resources

[1] Gildenblat, Jacob and contributors. “[PyTorch Library for CAM Methods](https://github.com/jacobgil/pytorch-grad-cam).” GitHub, Oct. 2021.

[2] Fernandez, François-Guillaume and contributor. “[TorchCAM: Class Activation Explorer](https://github.com/frgfm/torch-cam).” GitHub, Mar. 2020.

[3] Ozbek, Ahmet Can. “[Food-hunter: Food Hunting With CNNs](https://github.com/a-ozbek/food-hunter).” GitHub, Sept. 2018.
