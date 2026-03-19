# CS565600 Deep Learning  

course link : https://nthu-datalab.github.io/ml/


## Competitions:  
### 1. DataLab Cup 1: Text Feature Engineering  

In this competition, you are provided with a supervised dataset $X$ consisting of the raw content of news articles and the binary popularity (where 1 means "popular" and 
−1 means "unpopular", calculated based on the number of shares in online social networking services) of these articles as labels. Your goal is to learn a function $f$ from $X$ that is able to predict the popularity of an unseen news article. [[link]](https://nthu-datalab.github.io/ml/competitions/Comp_01_Text-Feature-Engineering/01_Text_Feature_Engineering.html) 

### 2. DataLab Cup 2: CNN for Object Detection  
In this competition, you have to train a model that recognizes objects in an image. Your goal is to output bounding boxes for objects. [[link]](https://nthu-datalab.github.io/ml/competitions/Comp_02_Object-Detection/02_Object_Detection.html) 

### 3. DataLab Cup 3: Reverse Image Caption  

In this work, we are interested in translating text in the form of single-sentence human-written descriptions directly into image pixels. For example, "this flower has petals that are yellow and has a ruffled stamen" and "this pink and yellow flower has a beautiful yellow center with many stamens". You have to develop a novel deep architecture and GAN formulation to effectively translate visual concepts from characters to pixels.

More specifically, given a set of texts, your task is to generate reasonable images with size 64x64x3 to illustrate the corresponding texts. Here we use Oxford-102 flower dataset and its paired texts as our training dataset [[link]](https://nthu-datalab.github.io/ml/competitions/Comp_03_Reverse-Image-Caption/03_Reverse-Image-Caption.html) 

## Labs:  
  
* Lab02: Exploratory Data Analysis (EDA) and Visualizing Data    [[link]](https://nthu-datalab.github.io/ml/labs/02_EDA_PCA/02_EDA_PCA.html)  
* Lab03: Decision Trees & Random Forests  [[link]](https://nthu-datalab.github.io/ml/labs/03_Decision-Tree_Random-Forest/03_Decision-Tree_Random-Forest.html)
* Lab04-1: Perceptron, Adaline, and Optimization [[link]](https://nthu-datalab.github.io/ml/labs/04-1_Perceptron_Adaline/04-1_Perceptron_Adaline.html)  
* Lab04-2: Linear, Polynomial, and Decision Tree Regression  [[link]](https://nthu-datalab.github.io/ml/labs/04-2_Regression/04-2_Regression.html) 
* Lab05: Regularization [[link]](https://nthu-datalab.github.io/ml/labs/05_Regularization/05_Regularization.html)
* Lab06: Logistic Regression and Evaluation Metrics [[link]](https://nthu-datalab.github.io/ml/labs/06_Logistic-Regression_Metrics/06_Logistic-Regression_Metrics.html) 
* Lab10: Neural Network - Word2Vec [[link]](https://nthu-datalab.github.io/ml/labs/10_Word2Vec/10_Word2Vec.html) 
* Lab11-1: Convolution Neural Networks [[link]](https://nthu-datalab.github.io/ml/labs/11-1_CNN/11-1_CNN.html) 
* Lab11-2: Visualization & Style Transfer  [[link]](https://nthu-datalab.github.io/ml/labs/11-2_Visualization_Style-Transfer/11-2_Visualization_Style-Transfer.html) 

* Lab12-1: Seq2Seq Learning & Neural Machine Translation [[link]](https://nthu-datalab.github.io/ml/labs/12-1_Seq2Seq-Learning_Neural-Machine-Translation/12-1_Seq2Seq-Learning_Neural-Machine-Translation.html) 
* Lab12-2: Image Captioning [[link]](https://nthu-datalab.github.io/ml/labs/12-2_Image-Caption/12-2_Image-Caption.html) 
* Lab13-3: Diffusion  [[link]](https://nthu-datalab.github.io/ml/labs/13-3_Diffusion/13_3_Diffusion.html) 
* Lab14: Q-Learning  [[link]](https://nthu-datalab.github.io/ml/labs/14_Q-Learning/14_Q-Learning.html)  
* Lab15: Deep Reinforcement Learning [[link]](https://nthu-datalab.github.io/ml/labs/15_Deep-Reinforcement-Learning/15_Deep_Reinforcement_Learning.html) 


## Environmental setup
Most of the code can be run in the environment specified by "dl5_py312_requirements.txt", Lab14 uses "dl4_py309_requirements.txt", and some evaluation code in Competition 2 and 3 requires "dl5_py310_requirements.txt".