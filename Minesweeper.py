import random
def countMines(x,y,gameField,yGridLength,xGridLength):
    mines = 0
    if x == 0 and y == 0:
      for i in range(x,x+2):
        for j in range(y,y+2):
          print(i,j,'\n',x,y)
          if gameField[j][i] == 'm':
            mines += 1
    elif x == 0 and y != 0 and y != yGridLength:
      for i in range(x,x+2):
        for j in range(y-1,y+2):
          if gameField[j][i] == 'm':
            mines += 1
    elif x == 0 and y == yGridLength:
      for i in range(x,x+2):
        for j in range(y-1,y+1):
          if gameField[j][i] == 'm':
            mines += 1
    elif x != 0 and x != xGridLength and y == 0:
      for i in range(x-1,x+2):
        for j in range(y,y+2):
          if gameField[j][i] == 'm':
            mines += 1
    elif x != 0 and x != xGridLength and y != 0 and y !=yGridLength:
      for i in range(x-1,x+2):
        for j in range(y-1,y+2):
          if gameField[j][i] == 'm':
            mines += 1
    elif x != 0 and x != xGridLength and y == yGridLength:
      for i in range(x-1,x+2):
        for j in range(y-1,y+1):
          if gameField[j][i] == 'm':
            mines += 1
    elif x == xGridLength and y == 0:
      for i in range(x-1,x+1):
        for j in range(y,y+2):
          if gameField[j][i] == 'm':
            mines += 1
    elif x == xGridLength and y != 0 and y != yGridLength:
      for i in range(x-1,x+1):
        for j in range(y-1,y+2):
          if gameField[j][i] == 'm':
            mines += 1
    elif x == xGridLength and y == yGridLength:
      for i in range(x-1,x+1):
        for j in range(y-1,y+1):
          if gameField[j][i] == 'm':
            mines += 1
    return str(mines)
def expertMode():
  #sets up the game (creates board etc)
  xGridLength = 30
  yGridLength = 16
  minesToCreate = 120
  gameField = [[0 for x in range(xGridLength)] for y in range(yGridLength)]
  playerField = [['u'for x in range(xGridLength)] for y in range(yGridLength)]
  xMiddle = [11,12,13,14,15,16,17,18]
  yMiddle = [6,7,8,9]
  print(len(gameField),len(gameField[0]),'hi')
  xGridLength -= 1
  yGridLength -= 1
  mines = 0
  print('\n\n\n\n')
  for i in gameField:
    print(i)
  while mines < minesToCreate:
    x = random.randint(0, xGridLength)
    y = random.randint(0, yGridLength)
    print(x,y)
    if gameField[y][x] != 'm' and (x not in xMiddle or y not in yMiddle):
      gameField[y][x] = 'm'
      mines += 1
  for i in gameField:
    print(i)
  for i in range(len(gameField)):
    for j in range(len(gameField[i])):
      if gameField[i][j] == 0:
        gameField[i][j] = countMines(j,i,gameField,yGridLength,xGridLength)
  print('\n\n\n\n\n\n\n')
  for i in gameField:
    print(i)

  print('\n\n\n\n')
  
  for i in xMiddle:
    for j in yMiddle:
      playerField[j][i] = gameField[j][i]
  print("   " + "0    " + "1    " + "2    " + "3    " + "4    " + "5    " + "6    " + "7    " + "8    " + "9   " + "10   " + "11   " + "12   " + "13   " + "14   " + "15   " + "16   " + "17   " + "18   " + "19   " + "20   " + "21   "+ "22   "+ "23   "+ "24   "+ "25   "+ "26   "+ "27   "+ "28   "+ "29   ")
  for i in range(len(playerField)):
    print("\n" + str(i) + str(playerField[i]))
  revealed = 0
  action = ''
  while (revealed < (((xGridLength+1) * (yGridLength+1))-minesToCreate)):
    xCoord = int(input("Enter the x coordinate of the square you would like to perform an action on.\nThe number should be more than or equal to 0, and less than or equal to 29. Make sure to enter ONE INTEGER ONLY You CANNOT change the coordinate after you input it: "))
    while xCoord < 0 or xCoord > xGridLength:
      #takes in the x coordinate, we will use this in the form of field[y][x]
      xCoord = int(input("Enter the x coordinate of the square you would like to perform an action on.\nThe number should be more than or equal to 0, and less than or equal to 29. Make sure to enter ONE INTEGER ONLY You CANNOT change the coordinate after you input it: "))
      #takes in the y coordinate, we will use this in the form of field[y][x]
    yCoord = int(input("Enter the x coordinate of the square you would like to perform an action on.\nThe number should be more than or equal to 0, and less than or equal to 15. \nMake sure to enter ONE INTEGER ONLY. \nYou CANNOT change the coordinate after you input it: "))
    while yCoord < 0 or yCoord > xGridLength:
      yCoord = int(input("Enter the x coordinate of the square you would like to perform an action on.\nThe number should be more than or equal to 0, and less than or equal to 15. \nMake sure to enter ONE INTEGER ONLY. \nYou CANNOT change the coordinate after you input it: "))
    while action != 'q' and action != 'f' and action != 'c' and action != 's':
      action = input("Which action would you like to do? Enter q to quit the game, enter f to plant a flag, enter c to click on a square: ")
    if action == 'q':
      exit()
    elif action == 'f':
      if playerField[yCoord][xCoord] != 'u':
        continue
      else:
        playerField[yCoord][xCoord] = 'f'
    elif action == 'c':
      if gameField[yCoord][xCoord] == 'm':
        print("You hit a mine! Game Over!")
        exit()
      else:
        playerField[yCoord][xCoord] = gameField[yCoord][xCoord]
        revealed += 1
    print("   " + "0    " + "1    " + "2    " + "3    " + "4    " + "5    " + "6    " + "7    " + "8    " + "9   " + "10   " + "11   " + "12   " + "13   " + "14   " + "15   " + "16   " + "17   " + "18   " + "19   " + "20   " + "21   "+ "22   "+ "23   "+ "24   "+ "25   "+ "26   "+ "27   "+ "28   "+ "29   ")
    for i in range(len(playerField)):
      print("\n" + str(i) + str(playerField[i]))
      #end the game
#game should end when all squares without mines are revealed
#so, when they click a square, if the square is safe the player board should copy the value from the field board and then the field board should change its value to r, when tiles - minesToCreate = amount of squares revealed the player should win
expertMode()
