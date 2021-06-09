# Welcome to CI-VTS!

## Table of Contents
1. [About CI-VTS](#about-ci-vts)
   1. [What is it?](#what-is-it)
   2. [Who is it for?](#who-is-it-for)
   
2. [The System](#the-system)
   1. [The Hard Stuff: Physical Setup](#the-hard-stuff-physical-setup)
      1. [Casing](#casing)
      2. [Camera](#camera)
      3. [Arduino](#arduino)
      4. [Circuitry](#circuitry)
   
   1. [The Soft Stuff: Installing and Running](#the-soft-stuff-installing-and-running)
      1. [Getting The Files](#getting-the-files)
      1. [Python](#python)
      2. [Dependencies](#dependencies)
      3. [Running the Program](#running-the-program)
      4. [A note on Compatibility and Platforms](#a-note-on-compatibility-and-platforms)

4. [Features](#features)
   1. [Current](#current)
   2. [Planned](#planned)
   
5. [Contributing](#contributing)
   1. [Submitting an Issue or Request](#submitting-an-issue-or-request)
   2. [Feedback and Test Cases](#feedback-and-test-cases)
   3. [Pull Requests](#pull-requests)

6. [License and Ownership](#license-and-ownership)

## About CI-VTS
### What Is It?
CI-VTS, which is short for "Ciona Intestinalis Vertical Tracking System", is a complete setup for performing vertical tracking on model micro-organisms in a submerged state. This  repository aims to give a complete overview of all its different parts and aspects, while also supplying users with instructions on how to get started.

### What Does It Do Exactly?
The main purpose of CI-VTS is to allow a user to perform light stimulus experiments on micro-   organisms in water or other liquid. Users can control an LED that emits white light into a small chamber containing a cuvette with the organisms, record their behaviour on camera, and finally view tracking data and visuals via image processing in the software application. In short: Users can create custom experiments, record them, and view the results.
## Who Is It For?
A typical user is any biology researcher or student that wishes to document the effects of light stmimulus on very small marine organisms of their choosing.
## The System
The entire system can be coarsely divided into two parts: A physical setup, and a software to interact with it. The physical setup consists of a 3D-printed casing, an industrial camera, an arduino and some control circuitry. The software is meant to interact with and control both the camera and the arduino. Each of these parts have theie own subsection here. 
### The Hard Stuff: Physical Setup
#### Casing
The casing is designed to be the "skeleton" of the physical system, as it will hold together all the other physical parts. It is also 3D-printed and therefore freely reproducible, with minimal assembly required. The CAD-files are avaialbe here on the repository. 
#### Camera
While any industrial camera could, in theory, do the trick, we have used the [DMK 33UP1300](https://www.theimagingsource.com/products/industrial-cameras/usb-3.0-monochrome/dmk33up1300/) for testing. Anyone wishing to reproduce the system should familiarize themselves with the casing design and verify dimensions.
#### Arduino
The Arduino serves to control infrared background illumination, and the stimulus LED. As with the camera, any arduino could possibly work with the system. During testing, we have used the [Arduino Nano](https://store.arduino.cc/arduino-nano) and thus recommend users that which to reproduce the system to do the same.
#### Circuitry
Wheras the Arduino supplies the signals, some minor circuitry are required to properly control the various LEDs. Refer to the schematics found here for more detailed info.
### The Soft Stuff: Installing and Running
This section details the requirements to propoerly operate the CI-VTS software application.

### Getting The Files
You can get the source files of the application as a zip archive from [here](https://github.com/simenfuglestad/CI-VTS/archive/refs/heads/main.zip) or by clicking the green button labeled "code" here on the github page. Make sure that the files are unzipped before you continue, running the program from inside a zip archive is highly unlikely to work.
#### Python
Users are required to use python3.x.x, though 3.9.x is recommended.
#### Dependencies
The following python packages are _absolutely required_:
1. [pyserial](https://pypi.org/project/pyserial/)
2. [opencv-python](https://pypi.org/project/opencv-python/)
3. [PySide6](https://pypi.org/project/PySide6/)
4. [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph) (NOTE: Development Version Required)

All of these can be installed easily via [pip](https://www.w3schools.com/python/python_pip.asp), which ships with python 3.4.x or higher. To do so, open a terminal and navigate to the directory where you unzipped the files. Then enter `pip install -r dependencies.txt` and wait for installation to finish.
#### Running the Program
With all the above steps completed, the program can be run from a terminal by navigating to the `src` folder and then entering `python __main__.py`(or sometimes `python3 __main__.py`, depending on how python was installed).
#### A Note on Compatibility and Platforms
The software has currently been tested and developed on Windows 10 and Manjaro Linux. While we always try our best to keep the application platform agnostic, Windows is currently the prioritized platform. 

## Features
### Current
1. Creating and Customizing Experiment profiles.
2. Creating and Customizing Stimulus profiles.
3. Adjust Infrared Backlight any time during or before experiments
4. Record Experiments as .avi video files
5. Live Camera View, also available during recording and experimentation
6. Movement tracking of the model organisms
7. Frame-by-frame interactive replay of recorded videos
### Planned
1. Experiment Logging
2. Custom Theming

## Contributing
We happily accept contributions of any kind, but kindly ask that the following guidelines are followed.
### Submitting an Issue or Request
If you encounter anything unexpected when running the software, feel free to submit an issue here on the github page. When submitting, please include the following:
1. Platform/Operating System
2. Expected behavior
3. Steps to Reproduce
4. Resulting behavior
5. (Optional) Any ideas you might have on what causes this

If there are features that you feel needs improving or are missing, then feel free to also submit an issue explaining your request/grievances.
### Feedback and Test Cases
Attention: Test Cases are not available yet, feel free to skip this section.

Another very useful way to contribute is to provide feedback through test cases. This mostly involves performing a series of pre-defined steps and reporting the result. A spreadsheet containing various cases can be found and filled in directly here on the github page.
### Pull Requests
If you want to contribute to the code base directly then please feel free to make a pull request using the following guidelines:
1. Only request merges to the `dev` branch
2. Preface your branch name and/or commit message with a short prefix indicating the type of change made followed by what changes were made, i.e `hotfix_issue#nr`,`feature_save_video_as_mkv`, `documentation_main_window`, etc
## License and Ownership
This project was commissioned by the [Sars International Centre for Marine Molecular Biology](https://www.uib.no/en/sarssenteret), Bergen. It is licensed under [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
