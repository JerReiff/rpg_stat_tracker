# rpg_stat_tracker
Discord bot app that tracks basic rpg character stats in a database

# Setup

Setup is largely a manual process at this point... sorry...
1. Clone this repo
2. In the root of the repo, create a venv and activate it:
```
python3 -m venv rpg_stat_tracker_venv
. rpg_stat_tracker_venv/bin/activate
```
3. Install the python requirements:<br>
```pip install -r src/stat_tracker/requirements.txt```
4. Install mysql:<br>
```sudo apt install mysql```<br>
or<br>
```sudo pacman -S mysql```<br>
5. Create a copy of the ```.env.default``` file and name it ```.env```. **Place your mysql credentials in this file. For added security, modify the permissions of this file so only you may access it**
