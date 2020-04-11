# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:51:30 2019
"""
# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D,BatchNormalization,Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
#Imports for collecting metrics
import keras_metrics as km
import tensorflow as tf

from keras.callbacks import ModelCheckpoint
#import tensorflow.keras as keras

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(BatchNormalization())
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2),strides = (2,2)))
classifier.add(Dropout(0.2))
# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(MaxPooling2D(pool_size = (2, 2),strides = (2,2)))
classifier.add(Dropout(0.5))
### Adding a 3rd convolutional layer
#classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
#classifier.add(BatchNormalization())
#classifier.add(MaxPooling2D(pool_size = (2, 2),strides = (2,2)))
#classifier.add(Dropout(0.2))
## Adding a 4th convolutional layer
#classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
##classifier.add(BatchNormalization())
#classifier.add(MaxPooling2D(pool_size = (2, 2)))
#classifier.add(Dropout(0.2))
# Step 3 - Flattening
classifier.add(Flatten())


# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(Dropout(0.2))
#classifier.add(Dense(output_dim =1, activation = 'sigmoid'))# binary 
classifier.add(Dense(output_dim =3, activation = 'softmax')) # catgorical 
# SET METRICS 

precision = km.categorical_precision()
recall = km.categorical_recall()
f1= km.categorical_f1_score()

# Compiling the CNN
#classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy',precision,recall,f1])
# # checkpoint
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]



    
# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator()
#                                    rescale = 1./255,
#                                   shear_range = 0.2,
#                                   zoom_range = 0.2,
#                                   horizontal_flip = True,
#                                   validation_split = 0.7)

test_datagen = ImageDataGenerator()#rescale = 1./255)

seed =7
training_set = train_datagen.flow_from_directory('training',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical',
                                                 shuffle =True,
                                                 seed =seed)#     seed =seed)#,save_to_dir = 'generatedimages') #categorical,binary

test_set = test_datagen.flow_from_directory('test',
                                            target_size = (64, 64),
                                            batch_size =32,
                                            class_mode = 'categorical',
                                            shuffle =False)#,   seed =seed)#categorical,binary
with tf.Session() as s:
    s.run(tf.global_variables_initializer())
    classifier.fit_generator(training_set,
                         samples_per_epoch = 150,
                         nb_epoch =30,
                         validation_data = test_set,
                         nb_val_samples = 60,
                         shuffle =True,
                         callbacks=callbacks_list,
                         verbose = 2)

