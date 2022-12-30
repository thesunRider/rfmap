# Technique 1 - Similarity Based IQ CNN Classifier 

> Paper: [ORACLE: Optimized Radio clAssification through Convolutional neuraL nEtworks](https://doi.org/10.1109/INFOCOM.2019.8737463)
> Authors: Kunal Sankhe, Mauro Belgiovine, Fan Zhou, Shamnaz Riyaz, Stratis Ioannidis, and Kaushik Chowdhury Electrical and Computer Engineering Department, Northeastern University, Boston, MA, USA
> Dataset aquired from: [Link](https://genesys-lab.org/oracle) K. Sankhe, M. Belgiovine,F. Zhou, L. Angioloni, F. Restuccia, S. D’Oro, T. Melodia, S. Ioannidis, and K. R. Chowdhury, "No Radio Left Behind: Radio Fingerprinting Through Deep Learning of Physical-Layer Hardware Impairments,” IEEE Transactions on Cognitive Communications and Networking, Special Issue on Evolution of Cognitive Radio to AI-enabled Radio and Networks, 2019.



The authors propose a CNN framework for RF fingerprinting called ORACLE (Optimized Radio clAssification through Convolutional neuraL nEtworks). This work provides one of the most extensive evaluations where they demonstrate up to 99% classification accuracy on more than 100 consumer-of-the-shelf (COTS) WiFi devices. They also demonstrate similar results on 16 bit-similar USRP X310 SDRs. Other key contributions of this work include the study of hardware-driven features occurring in the transmit chain that causes IQ sample variation. They study both static and
dynamic channel environment. 

In the case of the dynamic channel, they explore how feedback-driven transmitter-side modifications that use channel estimation at the receiver can increase the differentiability for the CNN classifier. Essentially, introducing perturbations/imperfections on the transmitter-side to aid classification while minimizing the impact on bit error rates.

Specifically, in the context of studying the effects of hardware driven RF impairments, the authors focus on IQ imbalance and DC offset. They use MATLAB Communications System Toolbox to generate IEEE 802.11a standard compliant packets. The transmitter in this case was a USRP X310 and the receiver was a USRP B210. They also use an external database which consisted of raw IQ collected from 140 devices which included phones, tablets, laptops, and drones belonging to 122
manufacturers. 

For the case of static channel, the authors used the following architecture;

> Input: Raw IQ with length 128. This was formatted into two-dimensional real value tensor of size 2X128
   Network: Two convolutional layers and two fully connected ayers each with 256 and 80 neurons.
   Kernels: 1st layer consists of 50 1x7 filters, second layer consists 50 2x7 filters
   Activation Function: Each convolution layer is followed by ReLU activation
   Output: A softmax is used in the last layer for classification. 

![[cnn_model_oracle_architecture.png]]
  
This architecture provided a median classification accuracy of 99% when up to 100 different devices were used and the performance dropped slightly to 96% for 140 devices. For the dataset collected using 16 X310 radios, the accuracy was close to 98.6%. 
![[Matrixes.png]]
The authors clearly highlight the challenge put forth by dynamic channels and propose introducing controlled impairments to the transmitter as a solution to alleviate it. While this may work in a setting where one can make such impairments to the transmit chain, in many commercial and tactical applications this is not an option at the physical layer. It can be further argued at that point one is not exactly exploiting the "unique" RF fingerprint of the device but rather assigning the device an artificial tag/id/fingerprint. This is certainly an interesting area of research that may have its application and
advantages.

The steps involved in classification are as follows:
1. Create the CNN network as per above
2. Get Raw IQ Samples ,reshape and get prediction results

ORACLE trains CNN using IQ samples collected from an experimental setup of USRP SDRs, as shown in Fig. 3, with a fixed USRP B210 as the receiver. All transmitters are bit-similar USRP X310 radios that emit IEEE 802.11a standards-compliant frames generated via a MATLAB WLAN System toolbox. The data frames generated contain random payload but have the same address fields, and are then streamed to the selected SDR for over-the-air wireless transmission. The receiver SDR samples the incoming signals at 5 MS/s sampling rate at the center frequency of 2.45 GHz for WiFi. Overall, we collect over 20 million samples for each radio. We conduct the experiments in a more open area which has fewer reflections as shown in Fig.4. The transmitter-receiver separation distance is increased from 2 ft to 62 ft with an interval of 6 ft.  

![Exp-Setup](http://www.genesys-lab.org/sites/default/files/Exp_setup.jpg)

Fig. 3: Experimental setup for data collection using SDR

![Environment](http://www.genesys-lab.org/sites/default/files/KRI_ORACLE_Environement.png)Fig 4.Experimental environment: open area with much less reflections