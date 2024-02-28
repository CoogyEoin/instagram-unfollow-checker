import json
import sys


"""
Script for checking who's not following me.

Usage: python checker.py <follower.json> <following.json>
"""

args = sys.argv

follower_list = []
following_list = []

with open(args[1], "r") as follower_file:
    follower_list = json.load(follower_file)

with open(args[2], "r") as following_file:
    following_list = json.load(following_file)

my_dict = {}

for i in follower_list:
    follower_name = i["string_list_data"][0]["value"]
    my_dict[follower_name] = 1

for i in following_list["relationships_following"]:
    following_name = i["string_list_data"][0]["value"]
    if following_name not in my_dict:
        print(following_name)

