
import logging
import sys,json,re
import time,glob,datetime,os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

config_file = 'config.json'
config_file_handle = open(config_file)
config = json.load(config_file_handle)

def core__getsave_model(model_id):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	return config['weight_path'] + str(model_id) +'#'+ timestr +'.hd5'

def core__listsave_model(model_id):
	return  [s[:-6]for s in glob.glob(config['weight_path'] + str(model_id)+'*.hd5.index')]


def core__getlatest_model(model_id):
	file_list = glob.glob(config['weight_path'] + str(model_id)+'*.hd5.index') #__listsave_model(model_id)
	date_ary = []
	for x in file_list:
		file_stamp = core____extract_timestamp(x)
		date_ary.append(datetime.datetime.strptime(file_stamp, "%Y%m%d-%H%M%S"))

	assert date_ary #if no model file was found then raise assertion error
	return config['weight_path'] + str(model_id) +'#'+ str(sorted(date_ary)[-1].strftime("%Y%m%d-%H%M%S"))+'.hd5'


def core____extract_timestamp(filename):
    return re.findall(re.escape('#')+"(.*)"+re.escape('.hd5'),filename)[0]



