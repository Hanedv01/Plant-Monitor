Author: Hannes Tjulin

Student ID: ht222pt
# Tutorial on how to make a Plant Monitor
Short project overview

How much time it might take to do (approximation)

This is a tutorial on how to make a plant monitor that both monitors long-term developments in a plant’s climate and can alert when it is time to water the plant. Following this guide should take no more than two hours, provided that all materials are at hand.

# Objective
Why you chose the project

What purpose does it serve

What insights you think it will give

My girlfriend has a large collection of houseplants. While she does not need reminders to water them, I do when she is away. In addition, she has read up on optimal conditions for her plants, but quantifying anything other than temperature requires specialized measuring equipment which we do not have. From these twin needs of long-term measurements and short-term alerts, the idea of this project was born. 

My hope is that the work done in researching and preparing this will enable me to do other projects within IoT. There is also room for improvement in this device, such as making it portable, which I might tackle in some spare time. 

# Material
List of material

What the different things (sensors, wires, controllers) do - short specifications

Where you bought them and how much they cost

The following materials are required to make this plant monitor in its most basic form. 

| Material | Price |
| ----------- | ----------- |
| [Raspberry Pi Pico WH](https://www.electrokit.com/raspberry-pi-pico-wh) | 109 |
| [USB Cable A M – micro B M](https://www.electrokit.com/usb-kabel-a-hane-micro-b-5p-hane-1.8m) | 39 |
| [Breadboard](https://www.electrokit.com/kopplingsdack-840-anslutningar) | 69 |
| [Jumper Cables M-M (x)](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane) | 29 |
| [Jumper Cables M-F (x)](https://www.electrokit.com/labbsladd-20-pin-15cm-hona/hane) | 29 |
| [JST-PH Cable](https://www.electrokit.com/kabel-med-jst-ph-4-pol-hona-/-0.64mm-stift-200mm) | 24 |
| [Adafruit STEMMA Soil Sensor](https://www.electrokit.com/jordfuktighetssensor-kapacitiv-i2c) | 115 |
| [DHT 11 Humidity and Temperature Sensor](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) |49|
| [Photoresistor Module](https://www.electrokit.com/ljussensor) | 39 |
| **TOTAL** | **463** |



  Computer setup
How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a beginner should be able to understand.

Chosen IDE

How the code is uploaded

Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.

This section contains two guides. First, how to update the firmware on the Raspberry Pi Pico. This is necessary for the Raspberry Pi to be able to run Python code. 

1. Install [Python]( https://www.python.org/downloads/) and [VS Code](https://code.visualstudio.com/download) on your computer if you don’t have them already.
2. Open VS Code and install the Pymakr extension. This is done by opening the tab “Extensions” in the left side menu (can also be done with Ctrl+Shift+X), searching for “Pymakr” and clicking “Install”.
3. Update the firmware:
	1. Download the [firmware](https://micropython.org/download/RPI_PICO_W/). Select the latest edition from “Releases”.
	2. Carefully insert the USB-Cable into the Raspberry Pi Pico. It cannot be inserted fully, a small gap will be left. 
	3. Hold down the BOOTSEL button on the Raspberry Pi while inserting the USB Cable into your computer. 
	4. A new drive called RPI-RP2 should open on your computer. Copy/paste the firmware that you downloaded into this drive. Wait until the drive closes down by itself. You should be ready to code now!

All of the steps above are required regardless of what device you want to create with your Raspberry Pi. What follows are the steps specific to this project.

# Putting everything together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

Circuit diagram (can be hand drawn)

*Electrical calculations

# Platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.
Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

Describe platform in terms of functionality

*Explain and elaborate what made you choose this platform

# The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

# Transmitting the data / connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

How often is the data sent?

Which wireless protocols did you use (WiFi, LoRa, etc …)?

Which transport protocols were used (MQTT, webhook, etc …)

*Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.

# Presenting the data

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

Provide visual examples on how the dashboard looks. Pictures needed.

How often is data saved in the database.

*Explain your choice of database.

*Automation/triggers of the data.

# Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

Show final results of the project

Pictures

*Video presentation
