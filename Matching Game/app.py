import pygame
import game_config as gc 
from animal import Animal

from time import sleep
from pygame import display, event, image

def find_index(x, y):
	'''returns the index of the clicked image but taking the mouse click coordinates'''
	row = y // gc.IMAGE_SIZE
	col = x // gc.IMAGE_SIZE
	index = row * gc.NUM_TILES_SIDE + col

	return index

pygame.init()

display.set_caption("Memory game")

screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')
#screen.blit(matched, (0 , 0))  # blit is used to display the one surface on another surface
#display.flip()  # make sure that matched is displayed only when u filp it.

running = True   # to keep running the game loop

# instansiate all the animal tiles
tiles = [Animal(i) for i in range(gc.NUM_TILES_TOTAL)]
current_images = []

# Game loop

while running:
	# to current keyboard, mouse events and anyother events
	current_events = event.get()

	# loop through events and check whether a event is performed

	for e in current_events:
		# check if the X button is pressed or not
		if e.type == pygame.QUIT:
			running = False  # if they press X button we set running to false so tht we quit the game loop

		if e.type == pygame.K_ESCAPE:
			running = False

		if e.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y  = pygame.mouse.get_pos()
			index = find_index(mouse_x, mouse_y)
			# checking whether the 2 images are not same
			if index not in current_images:
				current_images.append(index)
			if len(current_images) > 2:
				current_images = current_images[1:]



	screen.fill((255, 255, 255))

	total_skipped = 0

	# iterate over the tiles and display them
	for tile in tiles:
		# display images only in current imgs and all other as white
		if not (tile.skip):
			image_i = tile.image if tile.index in current_images else tile.box
			screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
		else:
			total_skipped += 1

	display.flip()

	# check for the match
	if len(current_images) == 2:
		idx1, idx2 = current_images
		if tiles[idx1].name == tiles[idx2].name:
			tiles[idx1].skip = True
			tiles[idx2].skip = True
			sleep(0.4)
			# display matched
			screen.blit(matched, (0, 0))
			display.flip()
			sleep(0.5)
			current_images = []

	if total_skipped == len(tiles):
		running = False


	display.flip()

print("GAME OVER!")