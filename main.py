import discord
import tweepy
import tokens
import time
from tweepy import auth
from functions import convert

auth = tweepy.OAuthHandler(tokens.tweepykey, tokens.tweepysecret)
auth.set_access_token(tokens.tweepyaccess, tokens.tweepyaccesssecret)
api = tweepy.API(auth)

 
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@client.command()
#async def pm(ctx):
    #used_id_list = []


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'https://twitter.com' in message.content:
        fx = convert(message.content)
        await message.channel.send(fx)
    else:
        pass

    if message.content.startswith('!timeline'):
        defaultTimeline = api.home_timeline()
        i = 0
        for tweet in defaultTimeline:
            if i <= 20:
                await message.channel.send(tweet.text)
                i+=1
                time.sleep(1)


client.run(tokens.discordtoken)
