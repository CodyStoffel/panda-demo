# Panda3D Demo

A simple 3D game project created with Python and Panda3D.

## Features
Player movement
Collectible objects
Random collectible locations
Score tracking
Basic game boundaries


## Requirements
Python 3
Panda3D
WSL with WSLg or another supported graphical environment
Installation
1. Clone the repository
git clone https://github.com/CodyStoffel/panda-demo.git
2. Create a Python virtual environment
python3 -m venv .venv
4. Activate the virtual environment
source .venv/bin/activate
5. Install the required dependencies
pip install -r requirements.txt


## Running the Project

Run the provided script:

./run.sh

The run.sh file uses the following commands:

unset LD_LIBRARY_PATH
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 \
MESA_LOADER_DRIVER_OVERRIDE=d3d12 \
python main.py


The run.sh configuration helps Panda3D run correctly in WSL using the Mesa D3D12 graphics driver.
