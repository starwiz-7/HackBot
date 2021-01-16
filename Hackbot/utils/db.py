from datetime import datetime
from pymongo import MongoClient
from mongotriggers import MongoTrigger
import pymongo
import asyncio
import logging
import sys
sys.path.append('..')
client = MongoClient(
    "mongodb+srv://Admin:HackBotAdmin@hackbot.g1uz8.mongodb.net/HackBot?retryWrites=true&w=majority"
)
bot_db = client.get_database("HackBot")
guilds = bot_db.get_collection("Guild-channels")
hackathons = bot_db.get_collection("Hackathons")
assets = bot_db.get_collection("Assets")

def save_new_guild(guild_id,channel_id):
    guilds.insert_one(
        {'guild': guild_id,'channel': channel_id}
    )

def update_channel(guild_id, channel_id):
    guilds.update_one({
        'guild':guild_id
    },
    {
        '$set':{'channel':channel_id}
    })

def delete_guild(guild_id):
    guilds.delete_one({
        'guild':guild_id
    })

def get_guilds():
    return list(guilds.find({}))

def is_guild(guild_id):
    return list(guilds.find({'guild':guild_id}))

def get_hackathon(website):
    return list(hackathons.find({'website':website}))

def new_hackathon():
    return list(hackathons.find({'new':True}))

def update_hackathon(name,website):
    hackathons.update_one({'name':name, 'website':website},{'$set':{'new':False}})

def get_asset(website):
    return list(assets.find({'website':website}))