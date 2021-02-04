import pygame
import random

pygame.init()

#Screen size and display
WIDTH = 600
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.update()
pygame.display.set_caption("~Snake Game~")

#Speed in which the snake moves
speed = pygame.time.Clock()

#Blocks on screen colors
snake = (0, 210, 49)
food = (255, 0, 0)
white = (255, 255, 255)

#Creating the snake
def theSnake(snakeBody, snakeList):
	for x in snakeList:
		pygame.draw.rect(WINDOW, snake, [x[0], x[1], snakeBody, snakeBody])

#Creating the food
def placeFood(width, body):
	X = round(random.randrange(0, width - body) / 10) * 10
	Y = round(random.randrange(0, width - body) / 10) * 10

	return X, Y

#Game loop
def game():

	gameOver = False

	snakeList = []
	snakeLength = 1

	xCoor = WIDTH / 2
	yCoor = WIDTH / 2

	changeX = 0
	changeY = 0

	score = 0
	snakeBody = 10

	foodX, foodY = placeFood(WIDTH, snakeBody)

	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					changeX = -snakeBody
					changeY = 0
				elif event.key == pygame.K_RIGHT:
					changeX = +snakeBody
					changeY = 0
				elif event.key == pygame.K_UP:
					changeX = 0
					changeY = -snakeBody
				elif event.key == pygame.K_DOWN:
					changeX = 0
					changeY = +snakeBody

		if yCoor >= WIDTH or yCoor < 0 or xCoor >= WIDTH or xCoor < 0:
			print("cX = " + str(changeX) + "		cY = " + str(changeY) + "\ncX = " + str(xCoor) + "		cY = " + str(yCoor))
			gameOver = True

		xCoor += changeX
		yCoor += changeY

		WINDOW.fill(white)

		pygame.draw.rect(WINDOW, food, [foodX, foodY, snakeBody, snakeBody])

		snakeHead = []
		snakeHead.append(xCoor)
		snakeHead.append(yCoor)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for x in snakeList[:-1]:
			if x == snakeHead:
				gameOver = True

		theSnake(snakeBody, snakeList)
		
		pygame.display.update()

		if xCoor == foodX and yCoor == foodY:
			foodX, foodY = placeFood(WIDTH, snakeBody)
			snakeLength += 1

		speed.tick(15)

	pygame.quit()
	quit()

game()