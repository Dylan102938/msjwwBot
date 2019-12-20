# msjwwBot

Automatic bot for posting #msjww19 on Instagram

# How to run on MacOS
1. Check if Python is installed on your machine. Open a terminal window and type
```bash
python --version
```
If you receive an error, type
```bash
python3 --version
```
If you receive an error for both, install python from the link below. If a python version is displayed, skip the next step.

2. Install Python
https://www.python.org/ftp/python/3.7.6/python-3.7.6-macosx10.9.pkg

3. Change directory to Desktop.
```bash
cd Desktop
```

4. Clone this repository.
```bash
git clone https://github.com/Dylan102938/msjwwBot.git
```

5. Change directory to msjwwBot
```bash
cd msjwwBot
```

6. Install the instabot library.
```bash
pip install instabot
```
Alternatively, if that doesn't work, run
```bash
pip3 install instabot
```

7. If you used pip3, type the below command with python3 as opposed to python.
```bash
python runbot.py
```

8. Follow the instructions on screen to log into a bot Instagram account.

# How to run on Winwdows
1. Install Conda from the following link: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

2. Type Miniconda into your Windows search bar located on the bottom left corner of your screen. Press enter. You should see a black, command-prompt like display.

3. Create a conda virtual environment.
```bash
conda update conda
conda create -n msjww python=3.6 pip
```

4. Activate your environment.
```bash
conda activate msjww
```

5. Download this repository as a zip file. It should be located on the top right corner of the page and will show up after you click the green "Clone or Download" button.

6. Unzip the folder.

7. In your Conda terminal, change directory to the folder path. For example, if I am in C:/Users/xxx/ and my folder is located in Downloads, I would run
```bash
cd Downloads/msjwwBot
```

8. In your Conda terminal, install instabot.
```bash
pip install instabot
```

9. Run the bot file and follow the instructions on screen.
```bash
python runbotwindows.py
```
