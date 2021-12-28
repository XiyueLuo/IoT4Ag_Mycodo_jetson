# Mycodo Jetson Nano

This is a repo for adapting Mycodo to run on Jetson Nano. Tested on Jetpack 4.6.1

Clone the repo to `/home` and rename the foldor to Mycodo. The code is setup to find its components at `~/Mycodo`.

Install dependancy:
```
sudo apt-get update
sudo apt-get install gawk curl nano unzip
sudo apt-get install python3-pip
pip3 install six wemo==1.0.4
```

Install the Mycodo:
```
cd Mycodo
sudo /bin/bash ~/Mycodo/install/setup.sh
```
