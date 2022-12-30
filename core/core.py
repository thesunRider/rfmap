
import logging
import sys,json,re,uuid
import time,glob,datetime,os
from os.path import dirname,abspath,join
import numpy as np


rf_map_dir = dirname(dirname(abspath(__file__)))
models_dir = join(dirname(abspath(__file__)),"models")
captures_dir = join(rf_map_dir,"captures")

capture_config_file = join(captures_dir,"config.json")

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def core_getmodel(model_id):
	avail_models = core_listavailable_models()
	for x in avail_models:
		if x["model_id"] == model_id:
			return x


def core_listavailable_models():
	id_ary = []
	jsons = glob.glob(join(models_dir,"model_*","descriptor.json"))
	for x in jsons:
		with open(x) as k:
			read_data = json.loads(k.read())
			id_ary.append(read_data)

	return id_ary


def core__get_model_weight_json(model_id):
	return join(models_dir,"model_"+str(model_id),"weights","config.json")

def core_list_weight_dict(model_id):
	weight_config_file = core__get_model_weight_json(model_id)
	f = open(weight_config_file)
	load_weights = json.loads(f.read())
	f.close()
	return load_weights["weights"]

def file_name_from_weight(model_id,weight_id):
	loaded_dict = weight_dict_from_weight(model_id,weight_id)
	return os.path.join(models_dir,"model_"+str(model_id),"weights", str(weight_id) +'#'+ loaded_dict["timestamp"] +'.hd5')


def weight_dict_from_weight(model_id,weight_id):
	all_weights_model = core_list_weight_dict(model_id)
	for x in all_weights_model:
		if x["weight_id"] == weight_id:
			return x

def core_getlabels(model_id, model_weight_id):
	return weight_dict_from_weight(model_id, model_weight_id)["y_label"]

def core__get_new_save_model(model_id):
	weight_config_file = core__get_model_weight_json(model_id)
	f = open(weight_config_file)
	load_weights = json.loads(f.read())
	uid_weight = str(uuid.uuid4())
	timestr = time.strftime("%Y%m%d-%H%M%S")
	new_weight = {"model_id":model_id,"weight_id":uid_weight,'timestamp': timestr,"y_label":[]}
	load_weights['weights'].append(new_weight)
	f.close()

	with open(weight_config_file, "w") as jsonFile:
		json.dump(load_weights, jsonFile)

	return os.path.join(models_dir,"model_"+str(model_id),"weights", str(uid_weight) +'#'+ timestr +'.hd5')

def core__listsave_model(model_id):
	all_weights_model = core_list_weight_dict(model_id)
	data_ary = []
	for x in all_weights_model:
		data_ary.append((x["timestamp"],x["weight_id"]))

	return  data_ary

def core_savefingerpint(capture_id,model_id,weight_id,fingerprint):
	all_captures = core_getcaptures()
	for x in range(0,len(all_captures['captures'])):
		if all_captures['captures'][x]["id"] == capture_id:
			if all_captures['captures'][x]["add_data"] is None:
				all_captures['captures'][x]["add_data"] = {}

			all_captures['captures'][x]["add_data"].update({'model_analysed':core_getmodel(model_id)["shortname"],"weight_used":weight_dict_from_weight(model_id,weight_id)["timestamp"],"fingerprint":fingerprint})

	with open(capture_config_file, "w") as jsonFile:
			json.dump(all_captures, jsonFile)



def core__getlatest_model(model_id):
	all_weights_model = core_list_weight_dict(model_id)
	date_ary = []
	last_date = 0
	cur_latest_element = None
	for x in all_weights_model:
		file_stamp = x["timestamp"]
		cur_weight_date = datetime.datetime.strptime(file_stamp, "%Y%m%d-%H%M%S")
		if cur_weight_date > last_date:
			cur_latest_element = x
			last_date = cur_weight_date


	assert date_ary #if no model file was found then raise assertion error
	return  join( models_dir ,"model_"+str(model_id),"weights", str(cur_latest_element["weight_id"]) +'#'+ str(cur_latest_element["timestamp"])+'.hd5') 

def core_generatefingerprint(results):
	results = np.array(results)
	values = np.array([])

	for i in range(0,results.shape[1]):
		values = np.append(values,[results[:, i].mean()])

	values = np.round(values*100,-1).astype(int)
	total = "".join([hex(x)[2:].zfill(2) for x in values])
	
	return total 

def core____extract_timestamp(filename):
    return re.findall(re.escape('#')+"(.*)"+re.escape('.hd5'),filename)[0]

def core_savecapture(workspace):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	file_save_format =  workspace["id"] + "_" + workspace["label"] +"#" +timestr+".npz"
	signal_sample = None
	workspace["timestamp"] = timestr
	if workspace["signal"]:
		signal = workspace["signal"]
		signal_sample = signal.read_samples().view(np.complex128).flatten()
		loaded_captures = core_getcaptures()
		workspace.pop('iq_data')
		workspace.pop('signal')
		loaded_captures["captures"].append(workspace)

		with open(capture_config_file, "w") as jsonFile:
			json.dump(loaded_captures, jsonFile)

	np.savez_compressed(join(captures_dir,file_save_format),signal_sample=signal_sample)


def core_get_capture_data(id_in):
	data_ret = core_getcapture(id_in)
	file_in = glob.glob(join(captures_dir,data_ret["id"] + "_" + data_ret["label"] +"#*.npz"))
	assert file_in
	return np.load(file_in[0])["signal_sample"]

def core_load_capture(id_in):
	data_ret = core_getcapture(id_in)
	assert data_ret
	data_ret["saved"] = 1
	return data_ret

def core_getcaptures():
	f = open(capture_config_file)
	loaded_captures = json.loads(f.read())
	f.close()
	return loaded_captures

def core_iqdata_toreal(iq_data,freq_carrier,sample_rate):
	sample_count = len(iq_data) 
	time = np.linspace(0, sample_count / sample_rate, sample_count)
	return iq_data.real * np.cos(2*np.pi*freq_carrier*time) -  iq_data.imag * np.sin(2*np.pi*freq_carrier*time)

def core_getcapture(id_in):
	all_captures = core_getcaptures()
	for x in all_captures["captures"]:
		if x["id"] == id_in:
			if x["add_data"]:
				x.update(x["add_data"])
				x.pop("add_data")
			else:
				x.pop("add_data")

			return x 