import numpy as np
import os,glob,json

import core


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
		
class Model1:
	model_id = 232313123
	model_descriptor_file = 'model_descriptor_' + str(model_id) +'.json'
	model_descriptor_handle = open(model_descriptor_file)
	model_descriptor = json.load(model_descriptor_handle)
	model = None

	def __init__(self):
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
		self.model.compile(loss='sparse_categorical_crossentropy',optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=1e-4),metrics=['accuracy'])

	#_PREDICT IS RAW IQ DATA TIME SERIES ARRAY [1+1j,1+2j.....] 
	def predict(self,x_pred):
		return self.model.predict(_reshapedata(x_pred))

	#HERE the input data needs to be in new shape
	def train_model(self,x_train,y_train,x_test,y_test):
		#fitting the model
		self.model.fit(x_train,y_train,epochs=5,validation_data=(x_test, x_test))
	
	def save_weights():
		save_file = core.core__getsave_model(self.model_id)
		logger.debug("Trained Model saved to :" + save_file)
		self.model.save_weights(save_file)
	
	def load_weight(self,weight_location=None):
		#if none weight_location,load latest saved weight
		if weight_location:
			logger.debug("Loading: "+weight_location )
			self.model.load_weights(weight_location)
			logger.info(weight_location +" Loaded")
		else:
			latest_model = core.core__getlatest_model(self.model_id)
			logger.debug("Loading: "+latest_model )
			self.model.load_weights(latest_model)
			logger.info(latest_model +" Loaded")

	def list_saved_models(self):
		val = core.core__listsave_model(self.model_id)
		return val

	def get_model(self):
		return (self.model_descriptor,self.model)

	def _reshapedata(self,data_in):
		data_blnc = pd.DataFrame({'real':data_in.real,'img':data_in.imag,'blnc':np.repeat(0,len(data_in.real))})
		size_blnc = len(data_blnc)
		rem = size_blnc%128
		return data_blnc.iloc[:,:-1].values[:size_blnc-rem].reshape((size_blnc//128,2,128))


