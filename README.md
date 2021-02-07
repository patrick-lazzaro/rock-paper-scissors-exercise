# rock-paper-scissors-exercise

PREREQUISITES
Anaconda 3.7+
Python 3.7+
Pip

INSTALLATION

Fork this remote repository under your own control, then download your remote copy onto your local computer. 

Then navigate there from the command line:
cd rock-paper-scissors-exercise

Use Anaconda to create and activate a virtual envirnoment, perhaps called "my-first-env":
conda create -n my-first-env python = 3.8
conda activate my-first-env

From inside the virtual envirnoment, install package dependencies:
pip install -r requirements.txt

SETUP

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired plyaer name:
PLAYER_NAME = "John Snow"

USAGE 

Run the game script:
python game.py