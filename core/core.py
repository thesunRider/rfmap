
import logging
import sys,json,re
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

def core__getsave_model(model_id):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	return os.path.join(models_dir,"model_"+str(model_id),"weights", str(model_id) +'#'+ timestr +'.hd5')

def core__listsave_model(model_id):
	return  [s[:-6]for s in glob.glob( join(models_dir ,"model_"+str(model_id),"weights", str(model_id)+'*.hd5.index') )]


def core__getlatest_model(model_id):
	file_list = glob.glob( models_dir ,"model_"+str(model_id),"weights", str(model_id)+'*.hd5.index') 
	date_ary = []
	for x in file_list:
		file_stamp = core____extract_timestamp(x)
		date_ary.append(datetime.datetime.strptime(file_stamp, "%Y%m%d-%H%M%S"))

	assert date_ary #if no model file was found then raise assertion error
	return  join( models_dir ,"model_"+str(model_id),"weights", str(model_id) +'#'+ str(sorted(date_ary)[-1].strftime("%Y%m%d-%H%M%S"))+'.hd5') 


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

	np.savez_compressed(join(captures_dir,file_save_format),signal_sample)

def core_getcaptures():
	f = open(capture_config_file)
	loaded_captures = json.loads(f.read())
	f.close()
	return loaded_captures