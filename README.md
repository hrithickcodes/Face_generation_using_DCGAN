## Face Generation using DCGAN

Generative modeling is an unsupervised learning task in machine learning that involves automatically discovering and learning the patterns in input data in such a way that the model can be used to generate new examples which are not in the original dataset. DCGAN, or Deep Convolutional GAN, is such a network architechture that is capable of generating RGB images of size 64x64. The idea of Deep Convolutional generative adversarial network was proposed in this [paper](https://arxiv.org/abs/1511.06434v1). 

## DCGAN Architecture
The network architecture is shown in the below figure.

<img src="https://gluon.mxnet.io/_images/dcgan.png" width="1000" height="233"/>

The Network hyperparameters are,

    Face_images_for_training = 60000
    IMAGE_HEIGHT = 64
    IMAGE_WIDTH = 64
    IMAGE_CHANNEL = 3
    NOISE_SIZE = 100
    DISCRIMINATOR_LEARNING_RATE = 0.0002
    GENERATOR_LEARNING_RATE = 0.0002
    BATCH_SIZE = 128
    EPOCHS = 150
    BETA1 = 0.5
    WEIGHT_INIT_STDDEV = 0.02
    EPSILON = 0.00001


## Results

This project uses DCGAN to generate fake face images of celebrities, the model was trained on the [CelebFaces Attributes dataset](https://www.kaggle.com/jessicali9530/celeba-dataset). The below GIF shows how the generator learns to generate a fake face over time.

<img src="https://github.com/Therickysen08/Face_generation_using_DCGAN/blob/main/GIF/FaceGan.gif" width="120" height="120" />

The model was trained for 150 epochs and then it was able to generate decent fake face images, some of them are given below.

<img src="https://github.com/Therickysen08/Face_generation_using_DCGAN/blob/main/generated_faces/fake_faces.jpg" width="400" height="400"/>


