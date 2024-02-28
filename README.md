# instagram-unfollow-checker
A simple tool for checking who unfollowed you on instagram. Scans through the json files that can be downloaded from Instagram using lists and a dictionary to print common elements.


## Usage

Inside the account section of your Instagram settings you will find the option to download your data. Simply select followers & following and you will recieve an email telling you to download the zip file.

Once the zip file is downloaded and extracted you will see the various follower and following files in both html and json format. We only need the json format.

Simply run the script with the follower.json and following.json files as arguments an a list of people who you are following but aren't following you will be printed.

    python src/checker.py followers_1.json following.json

Adjust the file locations and folder structures accordingly (eg: if you're on Windows use forward slash).


## Future Development

No further development planned as it's easy to use. May use a more effective algorithm in the future or add examples/script for running this automatically.
