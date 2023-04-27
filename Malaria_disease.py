
# Import libraries
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Conv2D
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

# re-size all the images to this
IMAGE_SIZE = [224, 224]

train_path = 'Dataset/train'
test_path = 'Dataset/test'
val_path = 'Dataset/val'





# Import the Vgg 19 library as shown below and add preprocessing layer to the front of VGG
# Here we will be using imagenet weights

vgg19 = VGG19(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

vgg19.summary()

# don't train existing weights
for layer in vgg19.layers:
    layer.trainable = False


# Getting number of output classes
folders = glob('Dataset/train/*')
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
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

# test_datagen = ImageDataGenerator(rescale = 1./255)
val_datagen = ImageDataGenerator(rescale = 1./255)


# Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory(train_path,
                                                 target_size = (224, 224),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')



training_set











val_set = val_datagen.flow_from_directory(val_path,
                                            target_size = (224, 224),
                                            batch_size = 32,
                                            class_mode = 'categorical')


# fit the model
# Run the cell. It will take some time to execute
r = model.fit_generator(
  training_set,
  validation_data=val_set,
  epochs=20,
  steps_per_epoch=len(training_set),
  validation_steps=len(val_set)
)





# Test dataset
test_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)

test_set = test_datagen.flow_from_directory(
    test_path,
    target_size = (224, 224),
    batch_size = 32,
    class_mode = 'categorical'
)


class_names = list(training_set.class_indices.keys())
class_names








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





# plt.figure(figsize=(15, 8))
# plt.subplot(1, 2, 1)
# plt.plot(range(50), accuracy, label='Training Accuracy')
# plt.plot(range(50), val_accuracy, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Validation Accuracy')

# plt.subplot(1, 2, 2)
# plt.plot(range(50), loss, label='Training Loss')
# plt.plot(range(50), val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()


CLASS_NAMES = ["Parasitized", "Uninfected"]


import tensorflow as tf
from PIL import Image


# def predict(model, img):
    
#     # converting images into array
# #     img_array = np.array(img.convert('RGB'))
#     img_array = tf.keras.preprocessing.image.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)
  
#     # making the prediction
#     predictions = model.predict(img_array)
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]

#     confidence = round(100 * (np.max(predictions[0])), 2)
#     return predicted_class, confidence



# def predict(model, img):
    
#     # converting images into array
#     img_array = tf.keras.preprocessing.image.img_to_array(img)
#     img_array = np.expand_dims(img_array, 0)
  
#     # making the prediction
#     predictions = model.predict(img_array)
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]

#     confidence = round(100 * (np.max(predictions[0])), 2)
#     return predicted_class, confidence



# plt.figure(figsize=(17, 17))
# counter =0
# for images, labels in test_set:
#     for i in range(12):
#         ax = plt.subplot(3, 4, i + 1)
#         plt.imshow(images[i])
        
#         predicted_class, confidence = predict(model, images[i])
#         actual_class = class_names[int(labels[i][0])]
        
#         plt.title(f"Actual: {actual_class},\n Predicted: {predicted_class}.\n Confidence: {confidence}%")
        
#         plt.axis("off")
        
        
#     break











import os
[i for i in (os.listdir("saved_models") + [0])]
# int(float('5.0'))


os.listdir("saved_models")


import os
model_version = max([int(i) for i in os.listdir("saved_models") if i != '.DS_Store'] + [0])+1
model_version


# Create new directory with model version
model_dir = os.path.join("saved_models", str(model_version))
os.makedirs(model_dir, exist_ok=True)


# Save model inside new directory
model.save(os.path.join(model_dir, "model_vgg19.h5"))









# save it as a h5 file


# from tensorflow.keras.models import load_model

# model.save('model_vgg19.h5')

















