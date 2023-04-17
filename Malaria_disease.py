#!/usr/bin/env python
# coding: utf-8


# Import libraries
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten, Conv2D
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt


# re-size all the images to this
IMAGE_SIZE = [224, 224]

train_path = 'Dataset/Train'
test_path = 'Dataset/Test'

# Import the Vgg 19 library as shown below and add preprocessing layer to the front of VGG
# Here we will be using imagenet weights
vgg19 = VGG19(input_shape=IMAGE_SIZE +
              [3], weights='imagenet', include_top=False)

vgg19.summary()

# don't train existing weights
for layer in vgg19.layers:
    layer.trainable = False

# Getting number of output classes
folders = glob('Dataset/Train/*')
folders

# our layers - you can add more if you want
x = Flatten()(vgg19.output)

# len(folders) is our output layer
# I am taking softmax and not sigmoid, because I am having two nodes, I could use sigmoid for one node.
prediction = Dense(len(folders), activation='softmax')(x)

# create a model object
model = Model(inputs=vgg19.input, outputs=prediction)

# view the structure of the model
model.summary()

# tell the model what cost and optimization method to use
# Note: Using 'categorical_crossentropy' beucase I have two nodes, for one node I could use 'binary_crossentropy'
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Use the Image Data Generator to import the images from the dataset
# Applying image augmentation in training data, to increase data set, with variations of the image.

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory(train_path,
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')

training_set

test_set = test_datagen.flow_from_directory(test_path,
                                            target_size=(224, 224),
                                            batch_size=32,
                                            class_mode='categorical')


# fit the model
# Run the cell. It will take some time to execute
r = model.fit_generator(
    training_set,
    validation_data=test_set,
    epochs=50,
    steps_per_epoch=len(training_set),
    validation_steps=len(test_set)
)

scores = model.evaluate(test_set)
scores

r.params

r.history.keys()

loss = r.history['loss']
val_loss = r.history['val_loss']

accuracy = r.history['accuracy']
val_accuracy = r.history['val_accuracy']

# plot the loss
plt.plot(loss, label='train loss')
plt.plot(val_loss, label='val loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')

# plot the accuracy
plt.plot(accuracy, label='train acc')
plt.plot(val_accuracy, label='val acc')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')


# save it as a h5 file

model.save('Malaria_model_vgg19.h5')
