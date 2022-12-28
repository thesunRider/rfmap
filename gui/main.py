import gui
import sv_ttk,os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
import sigmf
import sys
import numpy as np
from sigmf import SigMFFile, sigmffile
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import uuid
from tkinter import messagebox
import importlib

sys.path.insert(1,os.path.dirname(os.path.abspath('..')))
from rfmap.core import core

selected_model_tag = None
selected_db_tag = None
selected_weight_tag = None

capture_figure = None
capture_canvas = None

current_workspace = {"id":None,'iq_data':np.array([]),'label':None,'signal':None,'sample_rate':0,'sample_count':0,'sample_duration':0,'sample_frequency':0,'timestamp':None,'add_data':{},"saved":0}

def disableChildren(parent):
	for child in parent.winfo_children():
		wtype = child.winfo_class()
		if wtype not in ('Frame','Labelframe'):
			child.configure(state='disable')
		else:
			disableChildren(child)

def enableChildren(parent):
	for child in parent.winfo_children():
		wtype = child.winfo_class()
		print (wtype)
		if wtype not in ('Frame','Labelframe'):
			child.configure(state='normal')
		else:
			enableChildren(child)

def clear_workspace():
	global current_workspace,capture_figure
	for i in current_workspace:
		current_workspace[i] = None

	app.input_centre_frequency.set("")
	app.input_sample_rate.set("")
	app.input_signal_duration.set("")
	app.input_signal_label.set("")
	if capture_figure:
		plt.clf()


def change_rcrd_state(var_object,blank,mode):
	if app.chck_record.get() == 'file':
		enableChildren(app.lblframe_file)
		disableChildren(app.lblframe_sdr)
		clear_workspace()
	else:
		enableChildren(app.lblframe_sdr)
		disableChildren(app.lblframe_file)
		clear_workspace()

def plot_psd_home():#signal_sample,sampling_rate,signal_frequency):
	global capture_figure,capture_plot,capture_canvas
	 # the figure that will contain the plot
	capture_figure = Figure(
				 dpi = 100,facecolor='#fafafa')


	capture_plot = capture_figure.add_subplot(111)
	capture_canvas = FigureCanvasTkAgg(capture_figure,
							   master = app.space_spectrogram)  
	capture_canvas.draw()
	capture_canvas.get_tk_widget().pack(fill="both",side="top")


	toolbar = NavigationToolbar2Tk(capture_canvas,
								   app.space_spectrogram)
	toolbar.update()
	capture_canvas.get_tk_widget().pack()

def file_loadiq_data():
	global current_workspace,capture_plot
	filename = app.input_path_text.get()
	current_workspace["signal"] = sigmffile.fromfile(filename)
	current_workspace["saved"] = 0

	signal = current_workspace["signal"]
	sample_rate = signal.get_global_field(SigMFFile.SAMPLE_RATE_KEY)
	sample_count = signal.sample_count
	signal_duration = sample_count / sample_rate
	signal_sample = signal.read_samples().view(np.complex128).flatten()
	signal_frequency = signal.get_captures()[0]["frequency"]

	app.input_centre_frequency.set(signal_frequency)
	app.input_sample_rate.set(sample_rate)
	app.input_signal_duration.set(signal_duration)
	
	capture_plot.clear()
	capture_plot.psd(signal_sample, Fs=sample_rate,Fc=signal_frequency)
	capture_canvas.draw()

def file_open_dialg():
	filename = fd.askopenfilename(filetypes=[("sigmf-meta","*.sigmf-meta")])
	if os.path.exists(filename):
		app.input_path_text.set(filename)

		filename = app.input_path_text.get()
		signal = sigmffile.fromfile(filename)
		sample_rate = signal.get_global_field(SigMFFile.SAMPLE_RATE_KEY)
		sample_count = signal.sample_count
		signal_duration = sample_count / sample_rate
		signal_frequency = signal.get_captures()[0]["frequency"]

		filename_w_ext = os.path.basename(filename)
		filename_only, file_extension = os.path.splitext(filename_w_ext)

		app.input_signal_label.set(filename_only)
		app.input_centre_frequency.set(signal_frequency)
		app.input_sample_rate.set(sample_rate)
		app.input_signal_duration.set(signal_duration)
		signal = None


def save_current_workspace():
	global current_workspace

	current_workspace["id"] = str(uuid.uuid4())
	current_workspace["label"] = app.input_centre_frequency.get()
	current_workspace["sample_rate"] = app.input_sample_rate.get()
	current_workspace["sample_count"] = float(app.input_signal_duration.get()) * float(app.input_sample_rate.get())
	current_workspace["sample_duration"] = app.input_signal_duration.get()
	current_workspace["signal_frequency"] = app.input_centre_frequency.get()
	current_workspace["label"] = app.input_signal_label.get()
	current_workspace["saved"] = 1
	core.core_savecapture(current_workspace)
	messagebox.showinfo("showinfo", "Saved and Loaded as Current Capture :" +current_workspace["label"] +" \n You can view the capture from Database section" )

def tab_changed(event):
	global selected_db_tag
	if app.main_tab.index(app.main_tab.select()) == 1:
		populate_db_treeview()
	else:
		selected_db_tag = None

	if app.main_tab.index(app.main_tab.select()) == 2:
		populate_analysis_models()
	else:
		selected_model_tag = None

def populate_weights(event):
	global selected_model_tag
	app.tree_weights.delete(*app.tree_weights.get_children())
	selection = app.tree_analyze.selection()
	tag = app.tree_analyze.item(selection)['tags']
	if tag:
		id_in = tag[0]
		all_id_details = core.core__listsave_model(id_in)
		if all_id_details:
			selected_model_tag = id_in

		for x in all_id_details:
			data_timestamp = x[0]
			app.tree_weights.insert('', tk.END, values=(data_timestamp,),tags=x[1])

def populate_analysis_models():
	app.tree_analyze.delete(*app.tree_analyze.get_children())
	avail_models = core.core_listavailable_models()
	for x in avail_models:
		model_id = x['model_id']
		model_name = x['shortname']
		app.tree_analyze.insert('', tk.END, values=(model_name),tags=model_id)


def populate_properties(event):
	global selected_db_tag
	app.tree_properties.delete(*app.tree_properties.get_children())
	selection = app.tree_db.selection()
	tag = app.tree_db.item(selection)['tags']
	if tag:
		id_in = tag[0]
		all_id_details = core.core_getcapture(id_in)
		if all_id_details:
			selected_db_tag = id_in

		for key, value in all_id_details.items():
			app.tree_properties.insert('', tk.END, values=(key,value))



def populate_db_treeview():
	app.tree_db.delete(*app.tree_db.get_children())

	app.tree_db.insert('', tk.END, text='Captures', iid=0, open=False)
	app.tree_db.insert('', tk.END, text='Models', iid=1, open=False)


	core_cap = core.core_getcaptures()
	for count,x in enumerate(core_cap["captures"]):
		app.tree_db.insert('', tk.END, text=x["label"], iid=count+2, open=False,tags=x["id"])
		app.tree_db.move(count+2, 0, count)

def load_to_workspace():
	global current_workspace
	if selected_db_tag:
		current_workspace = core.core_load_capture(selected_db_tag)
		app.statusvar1.set("Loaded :" + current_workspace["label"])
	else:
		app.statusvar1.set("Select a DB to Load")

def load_AI_weights():
	global selected_weight_tag
	selection = app.tree_weights.selection()
	tag = app.tree_weights.item(selection)['tags']
	if tag:
		app.statusvar1.set("Weight Loaded")
		selected_weight_tag = tag[0]

def get_data():

	if current_workspace["saved"] == 1:
		loaded_data = core.core_get_capture_data(current_workspace["id"])
		return loaded_data

	if current_workspace["signal"] is not None:
		loaded_data = current_workspace["signal"].read_samples().view(np.complex128).flatten()
		return loaded_data


def start_analysis():
	assert selected_weight_tag
	assert selected_model_tag

	app.statusvar1.set("Please wait Loading data")
	data_ary = get_data()
	importing_module_name = "rfmap.core.models.model_" + str(selected_model_tag) + ".model_" + str(selected_model_tag)
	app.statusvar1.set("Please wait Loading module")
	imp = importlib.import_module(importing_module_name)
	model = getattr(imp, "Model_AI")
	model_ai = model()
	model_ai.load_weight(core.file_name_from_weight(selected_model_tag,selected_weight_tag))

	app.statusvar1.set("Starting analysis")
	data_trimmed = data_ary[app.data_start.get():app.data_end.get()]
	print(data_trimmed)
	prediction_results = model_ai.predict(data_trimmed)
	print(prediction_results)


app = gui.MainApp()

#Initialize gui callbacks
app.chck_record.trace('w',change_rcrd_state)
app.button_load_file.configure(command=file_open_dialg)
app.button_load_start.configure(command=file_loadiq_data)
app.button_savetodb.configure(command=save_current_workspace)
app.load_capture_active.configure(command=load_to_workspace)
app.load_weight.configure(command=load_AI_weights)
app.analyse_start.configure(command=start_analysis)
app.mainwindow.bind("<<NotebookTabChanged>>", tab_changed)
app.tree_db.bind("<<TreeviewSelect>>",populate_properties)
app.tree_analyze.bind("<<TreeviewSelect>>",populate_weights)

app.scroll_db_tree.configure(command=app.tree_db.yview)
app.tree_db.configure(xscrollcommand=app.scroll_db_tree.set)

app.scroll_properties.configure(command=app.tree_properties.yview)
app.tree_properties.configure(xscrollcommand=app.scroll_properties.set)


app.scroll_prop_x.configure(command=app.tree_properties.xview)
app.tree_properties.configure(yscrollcommand=app.scroll_prop_x.set)


#fill ui data
app.chck_record.set('file')
plot_psd_home()

app.tree_analyze['columns'] = ('model_name',)
app.tree_analyze.heading('model_name', text='Model')

app.tree_weights['columns'] = ('timestamp')
app.tree_weights.heading('timestamp', text='Timestamp')

app.tree_properties['columns'] = ('prop_name','prop_value')
app.tree_properties.heading('prop_name', text='Property Name')
app.tree_properties.heading('prop_value', text='Property Value')


sv_ttk.set_theme("light")
app.mainwindow.mainloop()

