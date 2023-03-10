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
        self.input_centre_frequency = tk.IntVar()
        self.input_centrefrequency.configure(
            textvariable=self.input_centre_frequency)
        self.input_centrefrequency.grid(column=1, padx=5, pady=5, row=0)
        label9 = ttk.Label(labelframe8)
        label9.configure(text='Sample Rate (sps):')
        label9.grid(column=0, row=1)
        self.input_samplerate = ttk.Entry(labelframe8)
        self.input_sample_rate = tk.IntVar()
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
        self.input_signal_duration = tk.IntVar()
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
        frame20 = ttk.Frame(frame12)
        frame20.configure(height=200, width=200)
        frame16 = ttk.Frame(frame20)
        self.tree_db = ttk.Treeview(frame16)
        self.tree_db.configure(selectmode="browse", show="tree")
        self.tree_db.pack(expand="true", fill="both", side="left")
        self.scroll_db_tree = ttk.Scrollbar(frame16)
        self.scroll_db_tree.configure(orient="vertical")
        self.scroll_db_tree.pack(fill="y", side="left")
        frame16.pack(fill="both", side="left")
        frame14 = ttk.Frame(frame20)
        self.scroll_properties = ttk.Scrollbar(frame14)
        self.scroll_properties.configure(orient="vertical")
        self.scroll_properties.pack(fill="y", side="right")
        self.tree_properties = ttk.Treeview(frame14)
        self.tree_properties.configure(selectmode="browse", show="headings")
        self.tree_properties.pack(expand="true", fill="both", side="top")
        self.scroll_prop_x = ttk.Scrollbar(frame14)
        self.scroll_prop_x.configure(orient="horizontal")
        self.scroll_prop_x.pack(fill="x", side="top")
        frame14.pack(expand="true", fill="both", side="left")
        frame15 = ttk.Frame(frame20)
        frame15.configure(height=200, width=200)
        self.load_capture_active = ttk.Button(frame15)
        self.load_capture_active.configure(text='Load As Active')
        self.load_capture_active.pack(fill="x", padx=5, pady=5, side="top")
        button25 = ttk.Button(frame15)
        button25.configure(text='Delete')
        button25.pack(fill="x", padx=5, pady=5, side="top")
        self.start_analysis = ttk.Button(frame15)
        self.start_analysis.configure(text='Analyze')
        self.start_analysis.pack(fill="x", padx=5, pady=5, side="top")
        frame15.pack(side="top")
        frame20.pack(expand="true", fill="both", side="top")
        frame22 = ttk.Frame(frame12)
        frame22.configure(height=200, width=200)
        scrollbar16 = ttk.Scrollbar(frame22)
        scrollbar16.configure(orient="vertical")
        scrollbar16.pack(fill="y", side="right")
        frame22.pack(expand="true", fill="both", side="top")
        frame12.pack(fill="both", side="top")
        self.main_tab.add(
            frame12,
            compound="top",
            state="normal",
            text='Database')
        frame23 = ttk.Frame(self.main_tab)
        frame23.configure(height=200, width=200)
        frame24 = ttk.Frame(frame23)
        frame24.configure(height=200, width=200)
        self.tree_analyze = ttk.Treeview(frame24)
        self.tree_analyze.configure(selectmode="extended", show="headings")
        self.tree_analyze.pack(fill="y", side="left")
        self.tree_weights = ttk.Treeview(frame24)
        self.tree_weights.configure(selectmode="browse", show="headings")
        self.tree_weights.pack(fill="y", side="left")
        frame27 = ttk.Frame(frame24)
        frame27.configure(height=200, width=200)
        frame29 = ttk.Frame(frame27)
        frame29.configure(height=200, width=200)
        self.load_weight = ttk.Button(frame29)
        self.load_weight.configure(text='Load Weight')
        self.load_weight.pack(padx=10, pady=10, side="left")
        self.analyse_start = ttk.Button(frame29)
        self.analyse_start.configure(text='Analyse')
        self.analyse_start.pack(side="left")
        frame29.pack(side="top")
        labelframe9 = ttk.Labelframe(frame27)
        labelframe9.configure(height=200, text='Capture Parameters', width=200)
        label17 = ttk.Label(labelframe9)
        label17.configure(text='Dataset name:')
        label17.grid(column=0, padx=5, pady=5, row=0)
        label18 = ttk.Label(labelframe9)
        label18.configure(text='None')
        label18.grid(column=1, padx=5, pady=5, row=0)
        label19 = ttk.Label(labelframe9)
        label19.configure(text='Data Start:')
        label19.grid(column=0, padx=5, pady=5, row=1)
        entry8 = ttk.Entry(labelframe9)
        self.data_start = tk.IntVar(value=0)
        entry8.configure(textvariable=self.data_start)
        _text_ = '0'
        entry8.delete("0", "end")
        entry8.insert("0", _text_)
        entry8.grid(column=1, row=1)
        label20 = ttk.Label(labelframe9)
        label20.configure(text='Data End:')
        label20.grid(column=0, row=2)
        entry9 = ttk.Entry(labelframe9)
        self.data_end = tk.IntVar(value=-1)
        entry9.configure(textvariable=self.data_end)
        _text_ = '-1'
        entry9.delete("0", "end")
        entry9.insert("0", _text_)
        entry9.grid(column=1, padx=5, pady=5, row=2)
        labelframe9.pack(padx=5, side="top")
        frame27.pack(anchor="ne", side="left")
        frame24.pack(fill="x", side="top")
        self.predict_chart = ttk.Frame(frame23)
        self.predict_chart.configure(height=200, width=200)
        self.predict_chart.pack(fill="x", side="top")
        frame26 = ttk.Frame(frame23)
        frame26.configure(height=200, width=200)
        label21 = ttk.Label(frame26)
        label21.configure(text='Fingerprint: ')
        label21.pack(pady=0, side="top")
        self.fingerprint_input = ttk.Entry(frame26)
        self.finger_string = tk.StringVar()
        self.fingerprint_input.configure(textvariable=self.finger_string)
        self.fingerprint_input.pack(pady=0, side="top")
        self.save_fingerprint = ttk.Button(frame26)
        self.save_fingerprint.configure(text='Save Fingerprint to Capture')
        self.save_fingerprint.pack(pady=10, side="top")
        frame26.pack(pady=5, side="bottom")
        frame23.pack(side="top")
        self.main_tab.add(
            frame23,
            compound="top",
            state="normal",
            text='Analyse')
        self.main_tab.pack(fill="both", side="top")
        label14 = ttk.Label(self.root)
        self.statusvar1 = tk.StringVar(value='No Data Active')
        label14.configure(
            relief="sunken",
            text='No Data Active',
            textvariable=self.statusvar1)
        label14.pack(expand="false", fill="x", side="bottom")

        # Main widget
        self.mainwindow = self.root
