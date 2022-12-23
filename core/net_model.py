import numpy as np
import os,glob,json

#importing the required libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout,Input
from tensorflow.keras.layers import Dense,BatchNormalization
from tensorflow.keras import regularizers
from numpy.fft import fft, ifft,fftshift,ifftshift

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Test messages
#logger.debug("Harmless debug Message")
#logger.info("Just an information")
#logger.warning("Its a Warning")
#logger.error("Did you try to divide by zero")
#logger.critical("Internet is down")

class Netmodel:
	model_id = 232313123
	model_descriptor_file = 'model_descriptor_' + str(model_id) +'.json'
	model_descriptor_handle = open(model_descriptor_file)
	model_descriptor = json.load(model_descriptor_handle)
	model = None

	def __init__():
		#adding model convolution layer
		self.model = Sequential()
		self.model.add(Conv2D(50,(1,7),activation='relu',input_shape=(2,128,1)))
		self.model.add(BatchNormalization())
		self.model.add(MaxPool2D(pool_size=(2, 2),strides=1,padding="same"))

		self.model.add(Conv2D(50,(2,7),activation='relu'))
		self.model.add(BatchNormalization())
		self.model.add(MaxPool2D(pool_size=(2, 2),strides=1,padding="same"))

		self.model.add(Flatten())

		self.model.add(Dense(256,kernel_regularizer=regularizers.L2(l2=1e-4) ))
		self.model.add(Dropout(0.5))
		self.model.add(Dense(80,kernel_regularizer=regularizers.L2(l2=1e-4) ))
		self.model.add(Dropout(0.5))

		#adding output layer
		self.model.add(Dense(16,activation='softmax' ))
		#compiling the model
		self.model.compile(loss='sparse_categorical_crossentropy',optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),metrics=['accuracy'])

		return (self.model_descriptor,self.model)

	def predict(x_pred):
		return model.predict(x_pred)

	def train_model(x_train,y_train,x_test,x_test,save_weights=False,**kwargs):
		#fitting the model
		self.model.fit(x_train,y_train,epochs=5,validation_data=(x_test, x_test),)
		if save_weights:
			save_file = core.__getsave_model(self.model_id)
			logger.info("Trained Model saved to :" + save_file)
			self.model.save_weights(save_file)
	
	def load_model(weight_location=None):
		#if none weight_location,load latest saved weight
		if weight_location:
			self.model.load_weights(weight_location)
		else:
			self.model.load_weights(core.__getlatest_model(self.model_id))

	def list_saved_models():
		return core.__listsave_model(self.model_id)

	def get_model():
		return self.model


