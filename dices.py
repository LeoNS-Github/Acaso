import re
from random import choice, randint
from commands.utils import isEnFun

def diceBody(command):
  isEn = isEnFun(command)
  result = choice([
    ['Cabeça','Head'],['Tronco','Body'],['Ombro E','L Shoulder'],
    ['Ombro D','R Shoulder'],['Braço E','L Arm'],['Braço D','R Arm'],
    ['Mão E','L Hand'],['Mão D','R Hand'],['Perna E','L Leg'],
    ['Perna D','R Leg'],['Joelho E','L Knee'],['Joelho D','R Knee'],
    ['Pé E','L Feet'],['Pé D','R Feet'],
  ])
  return f'` {result[isEn]} ` {command}'

def diceNumber(command):  
  result = randint( 1, int( command ) )
  return f'` {result} ` D{command}'

def complexDice(command):
  print(command)
  list = re.findall('^[0-9]d[0-9]+|[+|-][0-9]+', command)
  print(list)
  result = 0
  rolls = []
  attributes = 0
  for param in list:

    if param.count('d'):
      dices = param.split('d')

      print(dices)

      if dices[0] == '':
        dices[0] = 1

      while dices[0] > 0:
        rolls.append( randint( 1, int(param[1:] ) ) ) 
        dices[0] = dices[0]-1

    elif param[0] == '+':
      attributes += int(param[1:])

    elif param[0] == '-':
      attributes -= int(param[1:])

  print('rolls = '+ str(rolls) )
  result = sum(rolls)

  return f'` { str(result) } ` {command}'