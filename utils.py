from typing import List

charList = {}
char: List[str]
commandList = [
    'roll',
    'open',
    'party',
    'join',
    'char',
    'update',
    'ajuda',
    'help',
    'tiroa',
    'tirob',
    'dano',
    'cura'
]
enCommandList = ['body','help']

def isEnFun(text: str):
  if text in enCommandList:
    return 1
  return 0

def notCommand(text: str):
  text = text.lower()
  if text[0] != '!' and text[0] != '?':
    return True
  command = text[1:]
  command = command.split(' ')
  if command[0] not in commandList:
    return True

def helpResponse(text: str):
  if text not in enCommandList:
    return """
Comandos:
  ` !roll [*Valor* | *Corpo*] ` Rola um dado de tamanho determinado ou um dado de partes do corpo.
  ` !open ` Cria uma party no servidor usado.
  ` !party ` Exibe uma lista dos personagens na party do servidor.
  ` !join [*Nome*, *Vida*, *Munição A*, *Munição B*] ` Adiciona um personagem na party do servidor.
  ` !char [*Nome*] ` Exibe os dados do personagem.
  ` !update [*Nome*, *Vida*, *Munição A*, *Munição B*] ` Atualiza os dados do personagem citado.
  ` !ajuda ` Exibe esta mensagem (Obviamente).
"""
  return """
Commands:
  ` !roll [*Range* | *Body*] ` Rolls a dice in the given Range or a body parts dice.
  ` !open ` Creates a party in the current server.
  ` !party ` Shows a list of the party in the server.
  ` !join [*Name*, *Life*, *Ammo A*, *Ammo B*] ` Adds a character in the party.
  ` !char [*Name*] ` Shows the data of the character.
  ` !update [*Name*, *Life*, *Ammo A*, *Ammo B*] ` Updates the data of a given character.
  ` !help ` Shows this message (Obviously).
"""