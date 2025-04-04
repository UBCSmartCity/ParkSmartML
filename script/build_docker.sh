sudo docker run -it --ipc=host --privileged --device=/dev/bus/usb -v /dev/bus/usb:/dev/bus/usb -v /home/smartcity/ParkSmartML:/app/ParkSmartML --name parksmart2 parksmart-image bash
