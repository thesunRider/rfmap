#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class MainApp:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.title("RFMap by Suryasaradhi v1.0")
        self.head_label = ttk.Label(self.root)
        self.head_label.configure(text='RFMap')
        self.head_label.pack(side="top")
        self.main_tab = ttk.Notebook(self.root)
        frame1 = ttk.Frame(self.main_tab)
        frame1.configure(height=200, width=200)
        frame6 = ttk.Frame(frame1)
        frame6.configure(height=200, width=200)
        labelframe2 = ttk.Labelframe(frame6)
        labelframe2.configure(height=200, padding=5, text='Record', width=200)
        self.label_recordfrom = ttk.Label(labelframe2)
        self.label_recordfrom.configure(text='Record from:\n')
        self.label_recordfrom.pack(side="left")
        self.recrd_sdr = ttk.Radiobutton(labelframe2)
        self.chck_record = tk.StringVar(value='sdr')
        self.recrd_sdr.configure(
            text='Record from SDR',
            value="sdr",
            variable=self.chck_record)
        self.recrd_sdr.pack(side="top")
        self.recrd_file = ttk.Radiobutton(labelframe2)
        self.recrd_file.configure(
            text='Record from File',
            value="file",
            variable=self.chck_record)
        self.recrd_file.pack(side="top")
        labelframe2.pack(padx=10, pady=10, side="left")
        self.lblframe_sdr = ttk.Labelframe(frame6)
        self.lblframe_sdr.configure(padding=5, text='SDR')
        label3 = ttk.Label(self.lblframe_sdr)
        label3.configure(text='Device:')
        label3.pack(side="left")
        self.comobobox1_device = ttk.Combobox(self.lblframe_sdr)
        self.comobobox1_device.configure(
            state="normal", values='No_Device_Found')
        self.comobobox1_device.pack(side="left")
        self.lblframe_sdr.pack(fill="y", padx=10, pady=10, side="left")
        self.lblframe_file = ttk.Labelframe(frame6)
        self.lblframe_file.configure(padding=5, text='File')
        label4 = ttk.Label(self.lblframe_file)
        label4.configure(text='File(.sigmf):')
        label4.pack(side="left")
        self.input_fileload = ttk.Entry(self.lblframe_file)
        self.input_path_text = tk.StringVar(value='<file path>')
        self.input_fileload.configure(textvariable=self.input_path_text)
        _text_ = '<file path>'
        self.input_fileload.delete("0", "end")
        self.input_fileload.insert("0", _text_)
        self.input_fileload.pack(side="left")
        self.button_load_file = ttk.Button(self.lblframe_file)
        self.button_load_file.configure(text='Load File')
        self.button_load_file.pack(padx=5, side="left")
        self.lblframe_file.pack(fill="y", padx=10, pady=10, side="left")
        frame6.pack(side="top")
        frame7 = ttk.Frame(frame1)
        frame7.configure(height=200, width=200)
        labelframe5 = ttk.Labelframe(frame7)
        labelframe5.configure(height=200, text='Capture Data', width=200)
        frame10 = ttk.Frame(labelframe5)
        frame10.configure(height=200, width=200)
        labelframe6 = ttk.Labelframe(frame10)
        labelframe6.configure(
            height=200,
            padding=10,
            text='Controls',
            width=200)
        self.button_load_start = ttk.Button(labelframe6)
        self.button_load_start.configure(text='Load/Start')
        self.button_load_start.grid(column=0, padx=5, pady=4, row=0)
        self.button_stop = ttk.Button(labelframe6)
        self.button_stop.configure(text='Stop')
        self.button_stop.grid(column=1, row=0)
        self.button_savetodb = ttk.Button(labelframe6)
        self.button_savetodb.configure(text='Save/Use Active')
        self.button_savetodb.grid(column=0, row=2)
        self.button_clear = ttk.Button(labelframe6)
        self.button_clear.configure(text='Clear')
        self.button_clear.grid(column=1, row=2)
        labelframe6.pack(fill="both", padx=10, pady=10, side="left")
        labelframe8 = ttk.Labelframe(frame10)
        labelframe8.configure(padding=10, text='Parameters')
        label7 = ttk.Label(labelframe8)
        label7.configure(text='Centre Frequency (hz):')
        label7.grid(column=0, padx=5, pady=5, row=0)
        self.input_centrefrequency = ttk.Entry(labelframe8)
        self.input_centre_frequency = tk.StringVar()
        self.input_centrefrequency.configure(
            textvariable=self.input_centre_frequency)
        self.input_centrefrequency.grid(column=1, padx=5, pady=5, row=0)
        label9 = ttk.Label(labelframe8)
        label9.configure(text='Sample Rate (sps):')
        label9.grid(column=0, row=1)
        self.input_samplerate = ttk.Entry(labelframe8)
        self.input_sample_rate = tk.StringVar()
        self.input_samplerate.configure(textvariable=self.input_sample_rate)
        self.input_samplerate.grid(column=1, row=1)
        label10 = ttk.Label(labelframe8)
        label10.configure(text='Signal Label:')
        label10.grid(column=2, row=0)
        label11 = ttk.Label(labelframe8)
        label11.configure(text='Signal Duration (s):')
        label11.grid(column=2, row=1)
        entry5 = ttk.Entry(labelframe8)
        self.input_signal_label = tk.StringVar()
        entry5.configure(textvariable=self.input_signal_label)
        entry5.grid(column=3, row=0)
        entry6 = ttk.Entry(labelframe8)
        self.input_signal_duration = tk.StringVar()
        entry6.configure(textvariable=self.input_signal_duration)
        entry6.grid(column=3, padx=5, pady=5, row=1)
        button23 = ttk.Button(labelframe8)
        button23.configure(text='+', width=2)
        button23.grid(column=4, padx=5, row=0, rowspan=2)
        labelframe8.pack(fill="both", padx=10, pady=10, side="left")
        frame10.pack(fill="both", side="top")
        self.space_spectrogram = ttk.Frame(labelframe5)
        self.space_spectrogram.configure(height=200, width=200)
        self.space_spectrogram.pack(fill="both", side="top")
        labelframe5.pack(fill="both", padx=5, pady=5, side="top")
        frame7.pack(fill="both", side="top")
        frame1.pack(side="top")
        self.main_tab.add(
            frame1,
            compound="top",
            state="normal",
            text='Capture')
        frame12 = ttk.Frame(self.main_tab)
        frame12.configure(height=200, width=200)
        self.tree_db = ttk.Treeview(frame12)
        self.tree_db.configure(selectmode="extended")
        self.tree_db.pack(fill="both", side="left")
        scrollbar7 = ttk.Scrollbar(frame12)
        scrollbar7.configure(orient="vertical")
        scrollbar7.pack(fill="y", side="left")
        frame12.pack(side="top")
        self.main_tab.add(
            frame12,
            compound="top",
            state="normal",
            text='Database')
        self.main_tab.pack(fill="both", side="top")

        # Main widget
        self.mainwindow = self.root
