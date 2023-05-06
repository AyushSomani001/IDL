# Network Visualization Practice Notebooks

Here are some notebooks compiled to help users better utilize the library's capabilities:

| Notebook     |      Description      |   |
|:----------|:-------------|------:|
| [QuickTour](https://github.com/AyushSomani001/IDL/torch-cam/QuickTour.ipynb) | An overview of TorchCAM's primary features | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/frgfm/notebooks/blob/main/torch-cam/quicktour.ipynb) |
| [LatencyBenchmark](https://github.com/frgfm/notebooks/blob/main/torch-cam/latency_benchmark.ipynb) | How to Measure a CAM Method's Latency | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/frgfm/notebooks/blob/main/torch-cam/latency_benchmark.ipynb) |


# Research Papers - To Read


| Paper Title   |   Conference/Journal |   Author  | Description    |   
|:----------|:----------|:------|:------|
| [Towards Robust Interpretability with Self-Explaining Neural Networks!](https://proceedings.neurips.cc/paper_files/paper/2018/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf) | NeurIPS 2018 | D. Alvarez-Melis and T.S. Jaakkola | Proposes self-explaining neural networks, which learn to provide interpretable explanations for their predictions by incorporating explicit explanatory factors into the model architecture. | 
| [Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper_files/paper/2018/file/294a8ed24b1ad22ec2e7efea049b8737-Paper.pdf) | NeurIPS 2018 | Adebayo et al. | Highlights the limitations of saliency methods and proposes sanity checks to ensure that the explanations provided by these methods are meaningful and reliable.|
| [On the (In)fidelity and Sensitivity of Explanations](https://proceedings.neurips.cc/paper_files/paper/2019/file/a7471fdc77b3435276507cc8f2dc2569-Paper.pdf) | NeurIPS 2019 | Yeh at al. | Introduces two metrics, fidelity and sensitivity, to evaluate the quality of explanations provided by various interpretability methods, including saliency and CAMs.|
|[Invariant Risk Minimization](https://arxiv.org/abs/1907.02893) | arXiv 2019| Arjovsky et al. | Introduces Invariant Risk Minimization, a learning framework that encourages models to rely on features that are invariant across different environments, leading to more robust and interpretable predictions|
| [Explanation by Progressive Exaggeration](https://openreview.net/forum?id=H1xFWgrFPS) | ICLR 2020 | Singla et al. | A new method which iteratively exaggerates the most important features in the input to generate more robust and interpretable explanations. [GitHub](https://github.com/batmanlab/Explanation_by_Progressive_Exaggeration)|
| [Relevance-CAM: Your Model Already Knows Where to Look!](https://openaccess.thecvf.com/content/CVPR2021/papers/Lee_Relevance-CAM_Your_Model_Already_Knows_Where_To_Look_CVPR_2021_paper.pdf) | CVPR 2021 | Lee et al.  |  | 
| [Neural Prototype Trees for Interpretable Fine-Grained Image Recognition](https://openaccess.thecvf.com/content/CVPR2021/papers/Nauta_Neural_Prototype_Trees_for_Interpretable_Fine-Grained_Image_Recognition_CVPR_2021_paper.pdf) | CVPR 2021 | Nauta et al. |  |  
| [Concept-Monitor: Understanding DNN training through individual neurons](https://arxiv.org/pdf/2304.13346.pdf)| arXiv April 2023 | Khan et al.| |

<details open>
  <summary><strong>Recent and Interesting Archived Papers on Chat-GPT for Research:</strong></summary>
     [1] <a href="https://arxiv.org/pdf/2304.11567.pdf">Differentiate ChatGPT-generated and Human-written Medical Texts</a> | Liao et al. (2023)
    <br/>
    [2] <a href="https://arxiv.org/pdf/2304.08979.pdf">In ChatGPT We Trust? Measuring and Characterizing the Reliability of ChatGPT</a> | Shen et al. (2023)
    <br/>
    [3] <a href="https://arxiv.org/pdf/2304.05335.pdf"> Toxicity in CHATGPT: Analyzing Persona-assigned Language Models </a> | Deshpande et al. (2023)
   <br/> 
</details>


<details open>
  <summary><strong>Intriguing Model Improvement Application Paper:</strong></summary>
     [1] <a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Choe_Attention-Based_Dropout_Layer_for_Weakly_Supervised_Object_Localization_CVPR_2019_paper.pdf">Attention-based Dropout Layer for Weakly Supervised Object Localization</a> | Junsuk Choe, Hyunjung Shim (CVPR 2019) | <img src="https://edent.github.io/SuperTinyIcons/images/svg/github.svg" width="16" /> <a href="https://github.com/junsukchoe/ADL">GitHub</a> |
    <br/>
</details>

# References - Research Papers


| Paper     |      Description      | Author  |
|:----------|:-------------|------:|
| [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html) | Introduces `Grad-CAM`, a method that generalizes CAMs and provides better visual explanations for deep networks! | Selvaraju et al. (2016) |
| [Axiomatic Attribution for Deep Networks](http://proceedings.mlr.press/v70/sundararajan17a.html)| Presents `Integrated Gradients`, a technique that attributes the output of a deep network to its input features, providing a more comprehensive understanding of the model's decision-making process. | Sundararajan et al. (2017)|


# Resources

[1] Gildenblat, Jacob and contributors. “[PyTorch Library for CAM Methods](https://github.com/jacobgil/pytorch-grad-cam).” GitHub, Oct. 2021.

[2] Fernandez, François-Guillaume and contributor. “[TorchCAM: Class Activation Explorer](https://github.com/frgfm/torch-cam).” GitHub, Mar. 2020.

[3] Ozbek, Ahmet Can. “[Food-hunter: Food Hunting With CNNs](https://github.com/a-ozbek/food-hunter).” GitHub, Sept. 2018.
