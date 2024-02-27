from random import randint
from commands.utils import charList

def openParty(message):
  guild = str(message.guild.id)
  
  if guild not in charList:
    charList[guild] = {}
    print(f'Party created in {message.guild.name}')
    return f'Party created in {message.guild.name}'
  
  else:
    return '''Party already exists'''

def showParty(guild):
  party = charList[guild]
  response = "Party:"
  print(party)
  for char in party:
    char = party[char]
    response += f'''
` {char["id"]} ` {char["name"].title()} 
    PV: {char["hp"]} 
    Municao A: {char["ammo1"]} 
    Municao B: {char["ammo2"]}
'''
  return response

def setCharacter(userId, message, user_imput):
  guild = str(message.guild.id)

  if guild not in charList:
    return f'Party does not exist in {message.guild.name}'

  if userId in charList[guild]:
    return 'Você ja tem um personagem'
  
  char = user_imput.split(',')
  
  if len(char) == 4:

    if char[2].count('/') != 1:
      return
    if char[3].count('/') != 1:
      return
    check1 = char[1].split('/')
    check2 = char[2].split('/')
    check3 = char[3].split('/')
    try:
      int(check1[0])
      int(check1[1])
      int(check2[0])
      int(check2[1])
      int(check3[0])
      int(check3[1])
    except:
      return 'OoF'

      
    newId = f'#{len(charList[guild])+1}'
    char = {
      "id": newId,
      "name": char[0],
      "hp": char[1],
      "ammo1": char[2],
      "ammo2": char[3],
    }
    charList[guild][userId] = char
    return True
  else:
    return 'List out of format'

def updateCharacter(username, message, user_imput)-> str:
  print(message)
  return 'Nothing'

def shootA(username, guild, count = 1):
  if guild not in charList:
    return "Party não existe"
    
  if username not in charList[guild]:
    return "Você não tem um personagem"

  ammo = charList[guild][username]['ammo1'].split('/')
  if ammo[0] == '0':
    response = '` *Tec ` Sem Munição'
  else:
    ammo[0] = str(int(ammo[0]) - count)
    charList[guild][username]['ammo1'] = f'{ammo[0]}/{ammo[1]}'
    response = f'` {randint(1,100)} ` -> D100'
  return response

def shootB(username, guild, count = 1):
  if guild not in charList:
    return "Party não existe"

  if username not in charList[guild]:
    return "Você não tem um personagem"

  ammo = charList[guild][username]['ammo2'].split('/')
  if ammo[0] == '0':
    response = '` *Tec ` Sem Munição'
  else:
    ammo[0] = str(int(ammo[0]) - count)
    charList[guild][username]['ammo2'] = f'{ammo[0]}/{ammo[1]}'
    response = f'` {randint(1,100)} ` -> D100'

  return response

def damage(guild, command):
  isDamaged = False
  if guild not in charList:
    return "Party não existe"
  
  for char in charList[guild]:
    print(char)
    if command[1] == charList[guild][char]['id']:
      hp = charList[guild][char]['hp'].split('/')

      if int(hp[0]) - int(command[2]) < 0:
        hp[0] = 0
      else: 
        hp[0] = str(int(hp[0]) - int(command[2]))
        
      charList[guild][char]['hp'] = f'{hp[0]}/{hp[1]}'
      isDamaged = {'name': charList[guild][char]['name'], 'dano': command[2]}

  if isDamaged == False:
    return 'Personagem não encontrado'  
  
  return f'{isDamaged["name"]} recebeu {isDamaged["dano"]} de dano'

  
  