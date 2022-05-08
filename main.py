import discord
import os
import requests
import json
from keep_alive import keep_alive 

client=discord.Client()

def get_activity():
  response=requests.get("http://www.boredapi.com/api/activity/")
  
  json_data=json.loads(response.text)

  
  return (f"No problem, try a {json_data['type']} kind of activity like --> " + f"{json_data['activity']}")
  


def get_joke():
  response=requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
  
  json_data=json.loads(response.text)
  json_data=dict(json_data)

  return str(json_data['setup']+"\n"+"--> " +json_data['delivery'])

def get_age(name):
    u="https://api.agify.io?name="+name
    response=requests.get(u)
    json_data=json.loads(response.text)
    json_data=dict(json_data)
    age=int(json_data['age'])

    des=""

    if 0<=age<=5:
        des="Chuchu Chu Chuchu, such a cute baby."
    elif 6<=age<=12:
        des="Hey kiddo!"
    elif 13<=age<=20:
        des="You are a teenager now, be responsible!"
    elif 21<=age<=30:
        des="I hope you are serious about your career!"
    elif 31<=age<=45:
        des="Hi you are old enough to have a happy retirement."
    else:
        des="Hey oldy, better sleep."

    return (f"Age={str(age)}"+"\n"+des)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  
  if message.author==client.user:
    return
    
  msg=message.content
  
  if msg.startswith("$heyo"):
    await message.channel.send(f"Hello {message.author}!")
    
  if msg.startswith("$age"):    
    name=msg.replace("$age ","")
    try:
      await message.channel.send(get_age(name))
    except:
      await message.channel.send("Sorry there is an error. Please try again.")
    
  if msg.startswith("$joke"):
    await message.channel.send(get_joke())
    
  if msg.startswith("$activity"):
    await message.channel.send(get_activity())

keep_alive()
client.run(os.getenv('TOKEN'))