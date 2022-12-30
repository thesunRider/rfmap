import numpy as np
import os,glob,json

from rfmap.core import core


#importing the required libraries
from sklearn.preprocessing import normalize 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


#importing the required libraries
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, ZeroPadding2D
from tensorflow.keras.layers import Reshape, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras import metrics

from pandas import DataFrame as df

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

import random
import sys,gc


import pandas as pd

import logging
import sys
from os.path import dirname,abspath,join

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Model_AI:
	model_id = 5731286
	model_descriptor_file = join(dirname(abspath(__file__)),'descriptor.json')
	model_descriptor_handle = open(model_descriptor_file)
	model_descriptor = json.load(model_descriptor_handle)
	model = None
	model_weight_id = None
	model_output_number = 10

	def __init__(self,output_var_number = 10):
		self.model_output_number = output_var_number

		#adding model convolution layer

		dr = 0.5
		self.model = Sequential()
		self.model.add(Reshape((1, 2, 128), input_shape = (2, 128)))
		self.model.add(ZeroPadding2D((0, 2), data_format = 'channels_first'))
		self.model.add(Conv2D(256, (1, 3), padding = 'valid', activation = "relu", name="conv1", kernel_initializer='glorot_uniform', data_format="channels_first"))
		self.model.add(Dropout(dr))
		self.model.add(ZeroPadding2D((0,2), data_format = 'channels_first'))
		self.model.add(Conv2D(80, (2, 3), activation="relu", name="conv3", padding="valid", kernel_initializer="glorot_uniform", data_format="channels_first"))
		self.model.add(Dropout(dr))
		self.model.add(Flatten())   
		self.model.add(Dense(256, activation="relu", name="dense1", kernel_initializer="he_normal"))
		self.model.add(Dropout(dr))
		self.model.add(Dense(10, name="dense3", kernel_initializer="he_normal", activation = 'softmax'))
		self.model.add(Reshape([output_var_number]))

		#compiling the model
		self.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.legacy.Adam(), metrics = ['accuracy'])

	#_PREDICT IS RAW IQ DATA TIME SERIES ARRAY [1+1j,1+2j.....] 
	def predict(self,x_pred):
		return self.model.predict(self._reshapedata(x_pred))


	def prediction_to_labels(self,results):
		all_labels = core.core_getlabels(self.model_id, self.model_weight_id)
		all_labels = sorted(all_labels)
		assert (len(all_labels) - results.shape[1] == 0)

		prob_ary = {}
		for i in range(0,len(all_labels)):
			prob_ary.update({all_labels[i]:results[:, i].mean()})

		return prob_ary


	#Train model, x_in = [ [<device1 iq stream>] , [<device2 iq stream>] ...] , y_in = [dev1_label,dev2_label ....]
	def train_model(self,x_in,y_in,x_test_in,y_test_in):
		x_train,y_train = self._reshapefortrain(x_in,y_in)
		x_test,y_test = self._reshapefortrain(x_test_in,y_test_in)

		self.model.fit(x_train,y_train,epochs=5,validation_data=(x_test, y_test))
	
	def save_weights():
		save_file = core.core__get_new_save_model(self.model_id)
		logger.debug("Trained Model saved to :" + save_file)
		self.model.save_weights(save_file)
	
	def load_weight(self,model_id,weight_id):
		assert weight_id
		assert model_id

		self.model_weight_id =  weight_id
		file_model_weight = core.file_name_from_weight(model_id,weight_id)
		logger.debug("Loading: "+file_model_weight )
		self.model.load_weights(file_model_weight)
		logger.info(file_model_weight +" Loaded")

	def list_saved_models(self):
		val = core.core__listsave_model(self.model_id)
		return val

	def get_model(self):
		return (self.model_descriptor,self.model)

	def _reshapefortrain(self,x_data,y_data):
		data_ary_x = np.array([])
		data_ary_y = np.array([])
		#fitting the model
		for x in range(0,x_data.shape[0]):
			data_x = self._reshapedata(np.array(x_data[x]))
			data_y = np.repeat(y_data[x],len(data_x))
			data_ary_x = np.append(data_ary_x,data_x)
			data_ary_y = np.append(data_ary_y,data_y)

		return (data_ary_x,data_ary_y)

	def _reshapedata(self,data_in):
		assert (len(data_in.real) > 130) # the number of inputs should be greater than the sample input length 128
		data_blnc = pd.DataFrame({'real':data_in.real,'img':data_in.imag,'blnc':np.repeat(0,len(data_in.real))})
		size_blnc = len(data_blnc)
		rem = size_blnc%128
		return data_blnc.iloc[:,:-1].values[:size_blnc-rem].reshape((size_blnc//128,2,128))


