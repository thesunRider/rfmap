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

sys.path.insert(1,os.path.dirname(os.path.abspath('..')))
from rfmap.core import core

capture_figure = None
capture_canvas=None
current_workspace = {"id":None,'iq_data':np.array([]),'label':None,'signal':None,'sample_rate':0,'sample_count':0,'sample_duration':0,'sample_frequency':0,'timestamp':None,'add_data':{}}

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
	core.core_savecapture(current_workspace)
	messagebox.showinfo("showinfo", "Saved and Loaded as Current Capture :" +current_workspace["label"] +" \n You can view the capture from Database section" )


def clear_db_treeview():

def populate_db_treeview():
	core.core_getcaptures()	

app = gui.MainApp()

#Initialize gui callbacks
app.chck_record.trace('w',change_rcrd_state)
app.button_load_file.configure(command=file_open_dialg)
app.button_load_start.configure(command=file_loadiq_data)
app.button_savetodb.configure(command=save_current_workspace)

#fill ui data
app.chck_record.set('file')
plot_psd_home()

app.tree_db.insert('', tk.END, text='Captures', iid=0, open=False)
app.tree_db.insert('', tk.END, text='Models', iid=1, open=False)


app.tree_db.insert('', tk.END, text='John Doe', iid=5, open=False)
app.tree_db.insert('', tk.END, text='Jane Doe', iid=6, open=False)

app.tree_db.move(5, 0, 0)
app.tree_db.move(6, 0, 1)

sv_ttk.set_theme("light")
app.mainwindow.mainloop()

