from random import choice
from commands.char import damage, setCharacter, shootA, shootB, showParty, updateCharacter, openParty
from commands.dices import complexDice, diceBody, diceNumber
from commands.utils import charList, helpResponse

def get_response(username, message, user_imput) -> str:
  guildId = str(message.guild.id)
  guildName = str(message.guild.name)
  command = user_imput.lower()
  command = command[1:]
  command = command.split(' ')
  if command[0] == 'roll':
    try:
      if command[1] == 'body' or command[1] == 'corpo':
        return diceBody(command[1])
        
      else: 
        return diceNumber(command[1])

      # return complexDice(command[1])
      # else:
      #   print(command)
      #   return 'OoF'
      
    except:
      return 'OoF'

  elif command[0] == 'open':
    return openParty(message)
    
  elif command[0] == 'join':
    try:
      response = setCharacter(username['id'], message, command[1])
      if response == True:
        return 'Character set'
      else:
        return response
        
    except:
      return 'Something went wrong'

  elif command[0] == 'party':
    return showParty(guildId)
      
  elif command[0] == 'update':
    return updateCharacter(username, message, command[1])

  elif command[0] == 'char':
    char = charList[guildId][username['id']]
    print(char)
    response = f'''
{char['name'].title()}
  Vida restante ` {char['hp']} `
  Munição A ` {char['ammo1']} `
  Munição B ` {char['ammo2']} ` 
    '''
    return response
  
  elif command[0] == 'ajuda' or command[0] == 'help':
    return helpResponse(command[0])

  elif command[0] == 'tiroa':
    count = 1
    return shootA(username['id'], guildId, count)
  
  elif command[0] == 'tirob':
    count = 1
    return shootB(username['id'], guildId, count)

  elif command[0] == 'dano':

    if len(command) != 3:
      print('command não tem 3 argumentos')
      return 'OoF'
    
    if command[1][0] != '#':
      return 'OoF'

    return cura(guildId, command)

  elif command[0] == 'cura':

    if len(command) != 3:
      print('command não tem 3 argumentos')
      return 'OoF'
  
    if command[1][0] != '#':
      return 'OoF'
  
    return damage(guildId, command)


    
  else:
    return choice(['What?', 'Que?'])
