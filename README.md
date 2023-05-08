# Interpretable DL Playground
This is a repository that contains a comprehensive resource for AI practitioners and enthusiasts to explore and practice interpretable deep learning techniques, featuring a curated collection of modules, a relevant book "[Interpretability in Deep Learning](https://link.springer.com/book/10.1007/978-3-031-20639-9)" (Springer 2023), and intuitive explanations. 

While we do recommend basic deep learning knowledge, we've also included fundamental concepts for the convenience of our readers. Our goal is to help you understand the most prevalent and common practices of explainable AI and provide intuitive explanations of the techniques without delving too much into the mathematics at the beginning of each chapter. 

### About the Repository
Are you tired of black-box deep learning models that are difficult to interpret and explain? Look no further! 
Our repository aims to contain a curated collection of practice modules (shall be expanded over time) for interpretable AI and trustworthy model development.

Whether you're an AI practitioner or simply interested in learning more about interpretable deep learning techniques, our repository is the perfect resource for you to start. But that's not all! We've also included resources for you to further your understanding of the topic. We attempt to expand the practice modules over time in complex topics to help you apply the techniques in a hands-on manner, so you can see the benefits of interpretable AI for yourself.


### Research Papers - To Read


| Paper Title   |   Conference/Journal |   Author  | Description    |   
|:----------|:----------|:------|:------|
| [Towards Robust Interpretability with Self-Explaining Neural Networks!](https://proceedings.neurips.cc/paper_files/paper/2018/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf) | NeurIPS 2018 | D. Alvarez-Melis and T.S. Jaakkola | Proposes self-explaining neural networks, which learn to provide interpretable explanations for their predictions by incorporating explicit explanatory factors into the model architecture. | 
| [Sanity Checks for Saliency Maps](https://proceedings.neurips.cc/paper_files/paper/2018/file/294a8ed24b1ad22ec2e7efea049b8737-Paper.pdf) | NeurIPS 2018 | Adebayo et al. | Highlights the limitations of saliency methods and proposes sanity checks to ensure that the explanations provided by these methods are meaningful and reliable.|
| [On the (In)fidelity and Sensitivity of Explanations](https://proceedings.neurips.cc/paper_files/paper/2019/file/a7471fdc77b3435276507cc8f2dc2569-Paper.pdf) | NeurIPS 2019 | Yeh at al. | Introduces two metrics, fidelity and sensitivity, to evaluate the quality of explanations provided by various interpretability methods, including saliency and CAMs.|
|[Invariant Risk Minimization](https://arxiv.org/abs/1907.02893) | arXiv 2019| Arjovsky et al. | Introduces Invariant Risk Minimization, a learning framework that encourages models to rely on features that are invariant across different environments, leading to more robust and interpretable predictions|
| [Explanation by Progressive Exaggeration](https://openreview.net/forum?id=H1xFWgrFPS) | ICLR 2020 | Singla et al. | A new method which iteratively exaggerates the most important features in the input to generate more robust and interpretable explanations. [GitHub](https://github.com/batmanlab/Explanation_by_Progressive_Exaggeration)|
| [Relevance-CAM: Your Model Already Knows Where to Look!](https://openaccess.thecvf.com/content/CVPR2021/papers/Lee_Relevance-CAM_Your_Model_Already_Knows_Where_To_Look_CVPR_2021_paper.pdf) | CVPR 2021 | Lee et al.  | A method to generate class-discriminative visual explanations using pre-trained deep neural networks without additional training or modification. | 
| [Neural Prototype Trees for Interpretable Fine-Grained Image Recognition](https://openaccess.thecvf.com/content/CVPR2021/papers/Nauta_Neural_Prototype_Trees_for_Interpretable_Fine-Grained_Image_Recognition_CVPR_2021_paper.pdf) | CVPR 2021 | Nauta et al. | A hierarchical approach for interpretable fine-grained image recognition that combines neural networks with decision trees. |  
| [Concept-Monitor: Understanding DNN training through individual neurons](https://arxiv.org/pdf/2304.13346.pdf)| arXiv April 2023 | Khan et al.| A framework for demystifying black-box training processes using a unified embedding space and concept diversity metric, enabling interpretable visualization, improved training performance, and application to various training paradigms. |

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

## Citation
If you wish to cite the book "Interpretability in Deep Learning", feel free to use this [BibTeX](http://www.bibtex.org/) reference:

```bibtex
@book{somani2023interpretability,
  title={Interpretability in Deep Learning},
  author={Somani, Ayush and Horsch, Alexander and Prasad, Dilip K},
  year={2023},
  publisher={Springer Nature}
}
```

<img align="right" src="https://media.springernature.com/full/springer-static/cover-hires/book/978-3-031-20639-9?as=webp" width="150" alt="Book Cover" title="Interpretability in Deep Learning">


### Contributing

Feeling like extending the range of possibilities of interpretable methods to make AI more trustable? Or perhaps submitting a paper implementation? Any sort of contribution is greatly appreciated!

