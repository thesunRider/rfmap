
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

- [Dependencies / Limitations](#limitations)

- [Future Scope](#future_scope)

- [Setting up a local environment](#getting_started)

- [Usage](#usage)

- [Technology Stack](#tech_stack)

- [Contributing](docs/Contribution.md)

- [Authors](#authors)

- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

Identifying from which device a signal originates is the key to authenticating wit the said device. In modern days the security measures implemented on the software layer are easily spoofed using various cyber profiling mechanics. All the techniques involved in recognizing the source device happens at the software layer,which can be manipulated by third party to create counterfeit devices. Thus a technology to recognize devices at a hardware level is required. The technology should be able to detect unique electronic hardware features of the source device and should be able to classify it accordingly.

The Implemented software is able to classify and create hardware related fingerprints of device RF traffic from an existing group of pre recognized transmitters. 

RF Fingerprinting is the key to reducing the chances of counterfeit authentication of devices. This will help in creating secure communication channels.


## 💡 Idea / Solution <a name = "idea"></a>

This section is used to describe potential solutions.

Once the ideal, reality, and consequences sections have been

completed, and understood, it becomes easier to provide a solution for solving the problem.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- What are the dependencies of your project?

- Describe each limitation in detailed but concise terms

- Explain why each limitation exists

- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.

- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if

appropriate, describe how these limitations could point to the need for further research.

## 🚀 Future Scope <a name = "future_scope"></a>

Write about what you could not develop during the course of the Hackathon; and about what your project can achieve

in the future.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development

and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```

Give examples

```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```

Give the example

```

And repeat

```

until finished

```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

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