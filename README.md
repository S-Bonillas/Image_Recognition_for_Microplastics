![app_image](https://www.tetratech.com/wp-content/uploads/2023/10/Evaluating-the-Risk-of-Microplastics-in-Coastal-Waters-One-Water.jpg)

# Indisposable: Microplastic Detection and Avoidance
![MIT](https://img.shields.io/badge/License-MIT-C7F9CC)
![contributors](https://img.shields.io/badge/Contributors-5-38A3A5)


## Description
 Using Machine Learning, Image Recognition, and Computer Vision to detect microplastics in water samples.


 ## Table of Contents
- [Installation](#installation)
- [Data](#data)
- [License](#license)
- [Dashboard](#dashboard)
- [Presentation](#presentation)
- [Contact](#contact)


## Installation
The following need to be installed to successfully run the model and aPI.  

|Google Colab | Flask API|
| :-----------|:---------|
| tensorflow  |tensorflow|
| drive       | Flask    |
| numpy       | numpy    |
| os          | os       |
|skimage.color| Pillow   |
| matplotlib  |          |
| sklearn     |          |
| MobileNetV2 |          |

A copy of Google Colab notebook is saved in the Github in the P4_MicroPystics.ipynb file. 
- H5 and TR versions are also available on the Github.

# Data

## Source Data
- #### [Microplastic Dataset for Computer Vision, MOHAMADREZA MOMENI](https://www.kaggle.com/datasets/imtkaggleteam/microplastic-dataset-for-computer-vision)
- #### [Organisation for Economic CO-Operation and Development](https://stats.oecd.org/viewhtml.aspx?datasetcode=PLASTIC_WASTE_5&lang=en)

# Results and evaluation
With 781 image samples of microplastics and 781 control samples, our model reached an accuracy of 70.9% with 59.0% loss.

Our model utilized Transfer Learning by using MobileNetV2.  The model iteself is Sequential, with four Dense Layers, combiled using Adam. And cooked for 50 epochs.  The layers are arranged a such:
* Layer 1: 256 nodes, relu activation
* Layer 2: 128 nodes, elu activation
* Layer 3: 64 nodes, leaky_relu activation
* Layer 4: 1 node, sigmoid activation

![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/ac5aa13a-3489-405c-acdc-cf960f4e3be1)

![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/e1ec5bd1-ae92-4284-a023-bc4f846e0a7c)

![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/3008ef38-4c1c-412b-a4bd-e4fb4e0be80e)

![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/968221cb-cdb9-4d6b-9f7b-c2ebf7665bf9)

The model is decently reliable in finding microplastics, however it is prone to false positives.  Additional image data would be needed for more accurate predictions. 

![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/513c759b-f789-4370-80e9-1a9e2360a545)
![image](https://github.com/S-Bonillas/P4_Indispensible_ML_for_Microplastics/assets/137961214/c49e2556-f7bf-4253-8aea-2b4f2e48b2a0)


## License
MIT

## Dashboard
#### [Tableu Dashboard](https://public.tableau.com/app/profile/aspen.jack/viz/GlobalPlasticPollution2000-2019/FatesbyLocation)

## Presentation
#### [Microplastic Slides](https://docs.google.com/presentation/d/1sRxoyioXgtXuvYpZf2QyY2WqkmBYswgg-BXrIF9GpOc/edit#slide=id.gf1b017c262_0_97)

## Contact
If there are any questions or concerns, we can be reached at:
##### [github: aspenjack](https://github.com/aspenjack)
##### [github: arpitas0690](https://github.com/arpitas0690)
##### [github: S-Bonillas](https://github.com/S-Bonillas)
##### [github: Sequoiabm](https://github.com/Sequoiabm)
##### [github: velvetklr](https://github.com/velvetklr)


