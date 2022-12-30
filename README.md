
<p align="center">
<a href="" rel="noopener">
<a href="https://ibb.co/wWpqpCK"><img src="https://i.ibb.co/YkfSf8t/icon.jpg" alt="icon" border="0"></a>
</p>

<h1 align="center">RFMap</h1>


<div align="center">

[![Hackathon](https://img.shields.io/badge/hackathon-sainya_ranakshetram-orange.svg)](https://sainya-ranakshetram.in/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/thesunRider/rfmap.svg)](https://github.com/thesunRider/rfmap/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/thesunRider/rfmap.svg)](https://github.com/thesunRider/rfmap/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Software helping in Fingerprinting RF Signals, the software works leveraging modern AI methods to classify and analyse RF (Radio Frequency) signals.

<br>
The package is written modular so as to be able to add new AI 'plugins' into the package's classification methods. All Research credits goes to the authors who created the implemented AI papers.

</p>

## 📝 Table of Contents

- [Problem Statement](docs/Problem_Statement.md)

- [Idea / Solution](#idea)

- [Objectives](#objectives)

- [Future Scope](#future_scope)

- [Setting up a local environment](#getting_started)

- [Usage](#usage)

- [Technology Stack](#tech_stack)

- [Contributing](docs/Contribution.md)

- [Authors](#authors)

- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

Every radio signal transmission can be uniquely characterized due to randomness inmanufacturing process, origin and type of components etc. This process of radiofingerprinting is a process that identifies any other radio transmitter by the "fingerprint"that characterizes its signal transmission and is hard to imitate. An electronicfingerprint makes it possible to identify a wireless device by its radio transmissioncharacteristics. Radio fingerprinting is commonly used to prevent cloning.

Identifying from which device a signal originates is the key to authenticating wit the said device. In modern days the security measures implemented on the software layer are easily spoofed using various cyber profiling mechanics. All the techniques involved in recognizing the source device happens at the software layer,which can be manipulated by third party to create counterfeit devices. Thus a technology to recognize devices at a hardware level is required. The technology should be able to detect unique electronic hardware features of the source device and should be able to classify it accordingly.

The Implemented software is able to classify and create hardware related fingerprints of device RF traffic from an existing group of pre recognized transmitters. 

RF Fingerprinting is the key to reducing the chances of counterfeit authentication of devices. This will help in creating secure communication channels.


## 💡 Idea and Implementation <a name = "idea"></a>

RF Fingerprintng was implemented by analysing hardware imperfections of the transmitter and classifying them, We were able to predict IQ imbalances of different transmitters with an accuracy of 92%. 

Since the package was made to be modular (Plugin type architecture) three classifiers were added to the package to fingerprint transmitters. Adding further classifiers would be very easy due to the programming architecture.

The application Itself consists of three sections:
1. Capture
2. Database
3. Analysis

The Capture section is able to directly interface with SDR's (Software Defined Radio) to gather IQ samples or can open IQ samples captured to sigmf-files. This captured data is saved to the package's database. This database of captures can be viewed and edited from the Database section,furthermore from here we load the data to the memory that we need to analyse. The Analysis section consists of all the Classifier plugins, here you give the starting and ending indexes of the data that you wanted to analyse. And the probabilities of prediction will appear as a bar chart on this section,based on the bar chart a unique fingerprint will be generated for the data under study.

We have implemented 3 Classifier plugins for the package:

1. [Similarity Based IQ CNN Classifier](docs/Model_Doc_1.md)
2. SVM Based IQ Fingerprinting.
3. CNN Based Modulation Recognition.

Please take a look at the notes of the Classifers to learn more.
Each classifier is able to generate a unique fingerprint for a device under study, the fingerprint generation is as follows:

Suppose there are x labelled predictions of the classifier, a weighted hexadecimal shift of all the predicted possibilities rounded to the nearest one's position is generated.

```
ie. if the predicted probabilities are P = [1,53,25,18,3]
Sum(P) = 100
new_P = round P to nearest 5
     -> new_P = [0,50,25,20,0]
Convert Each element of P to hexadecimal and append the string together
fingerprint_array = [0x0,0x32,0x19,0x14,0x00]
We shift these bits in groups,thus the generated fingerprint is:
fingerprint = 0032191400
```

## ⛓️ Objectives Achieved<a name = "objectives"></a>

- [x] Create an Application that can identify and classify RF signals based on hardware imperfections < Problem Statement >
- [x] Store Fingerprints in database with timestamp < Problem Statement >
- [x] Load IQ samples from files
- [x] Platform Independent GUI, and package Installation

All the core problem statement needs have been implemented.

## 🚀 Future Scope <a name = "future_scope"></a>

- [ ] Directly Interface application with SDR
- [ ] Train classifiers within Application itself
- [ ] Detailed passive Analysis on captured RF Signal
- [ ] Implement Repeating Preamble Extractor
- [ ] Combine Multiple classification Fingerprints into single unique fingerprint
- [ ] GUI Improvements for Analysis progress monitoring
- [ ] Dockerise Application

 Due to modular architecture additional features can be implemented easily.
 
## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Usage](#Usage) on how to start using the package.

### Prerequisites

The package requires Python 3.8.5 or above, For installing dependencies:

```
pip3 install -r requirements.txt
```

Since the app runs on Tkinter for GUI ,and the dependencies are platform independent ,the package can run cross platform.

## 🎈 Usage <a name="usage"></a>

The package can be started by running:

```
cd gui/
python3 main.py
```


## ✅ Tested on

> Windows 10 Home ver: 10.0.19044 Build:19044
> Kali Linux ver: 6.0.0.1-amd-64

Tested as of 30-12-2022

## ⛏️ Built With <a name = "tech_stack"></a>

- [Tensorflow](https://www.tensorflow.org/) - AI
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI Framework
- [h5py](https://www.h5py.org/) - SDR API and HDF5 interface

## ✍️ Authors <a name = "authors"></a>

- [@thesunRider](https://github.com/thesunRider) - Idea & Initial work


## 🎉 Acknowledgments <a name = "acknowledgments"></a>

- [Aswin vishnu](https://www.instagram.com/vishnuaaswinam/) - AI models, Dataset filtering

## 🎓 References
-  [Radio Frequency Fingerprint Extraction of Radio Emitter Based on I/Q Imbalance](https://doi.org/10.1016/j.procs.2017.03.092)
-  [ORACLE: Optimized Radio clAssification through Convolutional neuraL nEtworks](https://doi.org/10.1109/INFOCOM.2019.8737463)
-  K. Sankhe, M. Belgiovine,F. Zhou, L. Angioloni, F. Restuccia, S. D’Oro, T. Melodia, S. Ioannidis, and K. R. Chowdhury, "No Radio Left Behind: Radio Fingerprinting Through Deep Learning of Physical-Layer Hardware Impairments,” IEEE Transactions on Cognitive Communications and Networking, Special Issue on Evolution of Cognitive Radio to AI-enabled Radio and Networks, 2019.
- [Convolutional Radio Modulation RecognitionNetworks](https://arxiv.org/abs/1602.04105)