from typing import Final
from discord import Intents, Client, Message
from commands.responses import get_response
from commands.utils import notCommand
from os import environ
from keepAlive import keep_alive

key:Final[str] = environ['BOT_KEY']

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)


async def send_message(username,message:Message,user_message:str,pv:bool)->None:
  if not user_message:
    print('User message is empty')
    return
  
  pv = (user_message[0] == '?')
  
  try:
    response: str = get_response(username, message, user_message)
    await message.author.send(response) if pv else await message.channel.send(response)
  except Exception as e:
    print(e)


@client.event
async def on_ready():
  print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
  if message.author == client.user:
    return

  username = {
    'id': str(message.author.id),
    'nick': str(message.author.nick),
    'name': str(message.author.name),
  }
  user_message = str(message.content)
  channel: str = str(message.channel)

  if(notCommand(user_message)):
    return
  
  print(f'{username["name"]} said: "{user_message}" ({channel})')
  await send_message(username, message, user_message, pv = False)

keep_alive()

def main() -> None:
  client.run(key)

if __name__ == '__main__':
  main()
