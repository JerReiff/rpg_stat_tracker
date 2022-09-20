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
6. Run the script ```src/stat_tracker/db/build_db.sh``` to build the database. This script will ask for your database password.
7. Create an "app" on your discord account and add a bot to it on the developer portal. Guides may frequently change, so you'll have to google this one. The process is relatively straightforward. As of September 19, 2022, these are the permissions the bot will need:
![Screenshot_20220919_213039](https://user-images.githubusercontent.com/54644679/191147597-f72adcf6-bf3b-4acb-8d5e-969b0d0e833f.png)
8. Copy your bot access token to the ```discord_token``` field of ```.env```
9. Run the app!<br>
```python3 src/stat_tracker/stat_tracker.py```
