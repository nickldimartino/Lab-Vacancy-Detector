Created by Benjamin Abraham, Alay Bhammar, Nicholas DiMartino, and Yu-Heng Hsia

The website for the porject is here: http://www.ecs.umass.edu/sdp/sdp21/team09/
If this URL does not work, naviagte to the ECE UMass Amherst website. From here, go to Undergraduate Students -> Senior Design Project. Finally, go to Teams -> Team 9: Lab Capacity Detector. 

The Lab Vacancy Detector is a camera system that uses object detection to determine if a person has entered or exited a room.  This information is then sent to Firebase for an Android app to receive.  People can view a room's vacancy and enter a queue to save a seat in the respective room.

Open CV must be installed in a virtual environment. Once installed run "workon cv" to get into the virtual environment.

The code uses a Raspberry Pi camera which has the capability to detect different objects. However, only people will be detected for this project.

An LED display is situated outside the door showing people the queue and capacity.

Command to run the code after Open CV is installed:

python real_time_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel
