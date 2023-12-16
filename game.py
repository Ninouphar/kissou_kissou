import pygame
from sys import exit
from random import randint

def display_score():

	current_time = 10 - (int(pygame.time.get_ticks() / 1000) - start_time)
	score_surf = test_font.render(f'{current_time}\'', False, (231,58,118))
	score_rect = score_surf.get_rect(center = (400,50))
	# score_surf_2 = pygame.transform.rotozoom(score_surf_2, 0, 0.5)
	score_surf_2 = test_font.render('of kissous left', False, (255,192,203))
	score_rect_2 = score_surf_2.get_rect(center = (400,100))

# (231,58,118)
	# nb_of_kissous = test_font.render(f'{kissou}', False, (231,58,118))
	# nb_of_kissous_rect = nb_of_kissous.get_rect(center = (520, 50))

	# timer_text = test_font.render('Kissou as fast', False, (255,192,203))
	# timer_text_rect = timer_text.get_rect(center = (400, 90))

	# timer_text_2 = test_font.render('as you can !', False, (255,192,203))
	# timer_text_2_rect = timer_text_2.get_rect(center = (400, 130))

	screen.blit(score_surf, score_rect)
	screen.blit(score_surf_2, score_rect_2)
	# screen.blit(timer_text, timer_text_rect)
	# screen.blit(timer_text_2, timer_text_2_rect)
	# screen.blit(nb_of_kissous, nb_of_kissous_rect)
	return current_time

def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect):
				return False
	return True


#INITIALISATION
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Early_GameBoy.ttf', 40)
game_active = False
start_time = 0
score = 0

#DECOR
sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('kiss_wallpaper.jpg').convert()
ground_surface = pygame.transform.rotozoom(ground_surface, 0, 0.7)
ground_rect = ground_surface.get_rect(topleft = (16,300))

#KYLIE
kylie_surface = pygame.image.load('kylie.png').convert_alpha()
kylie_surface = pygame.transform.rotozoom(kylie_surface,0,0.4)
kylie_rect = kylie_surface.get_rect(bottomright = (480, 300))
kylie_position = 0


#MENU
game_name = test_font.render('Kissou Kissou', False, (244,237,222))
# game_name = pygame.transform.rotozoom(game_name, 0, 0.5)
game_name_rect = game_name.get_rect(center = (400, 70))

image_menu = pygame.image.load('chalamet.png').convert_alpha()
image_menu_rect = image_menu.get_rect(center = (400,200))

game_message = test_font.render('Press enter to kissou', False, (244,237,222))
game_message = pygame.transform.rotozoom(game_message, 0, 0.8)
game_message_rect = game_message.get_rect(center = (400,350))

#TIMOTHEE
tim_surface = pygame.image.load('chalamet.png').convert_alpha()
tim_surface = pygame.transform.rotozoom(tim_surface,0,0.5)
tim_rect = tim_surface.get_rect(midbottom = (250,300))
tim_position = 0

#SCORE
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)
kissou = 0

while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			exit()
		if game_active:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					if tim_rect.left >= 0:
						tim_position = 12
					if kylie_position >= 0:
						kylie_position = -12
					
		else:
			start_time = int(pygame.time.get_ticks() / 1000)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					kissou = 0
					game_active = True

	if game_active: 
		screen.blit(sky_surface, (0,0))
		screen.blit(ground_surface, ground_rect)

		score = display_score()
		if score <= 0:
			game_active = False

		tim_rect.x += tim_position
		if tim_rect.left >= 400:
			tim_rect.left = 400
		if tim_rect.left <= 250:
			tim_rect.left = 250

		kylie_rect.x += kylie_position
		if kylie_rect.left >= 460:
			kylie_rect.left = 460

		screen.blit(tim_surface, tim_rect)
		screen.blit(kylie_surface, kylie_rect)

		if tim_rect.colliderect(kylie_rect):
			tim_position = -5
			kylie_position = 5
			kissou += 1
		
		if score > 30:
			game_active = False
		
	else:
		screen.fill((255,182,193))
		screen.blit(image_menu, image_menu_rect)
		tim_rect.midbottom = (80,300)
		tim_position = 0
		kylie_position = 0
		kylie_rect.x = 450
		tim_rect.x = 150
		
		score_message = test_font.render(f'Your score: {kissou}', False, (244,237,222))
		# score_message = pygame.transform.rotozoom(score_message, 0, 0.5)
		score_message_rect = score_message.get_rect(center = (400,330))

		screen.blit(game_name, game_name_rect)

		# print (kissou);
		if kissou == 0:
			screen.blit(game_message, game_message_rect)
		else:
			screen.blit(score_message, score_message_rect)
	# keys = pygame.key.get_pressed()
	# if keys[pygame.K_SPACE]:
	#     print('jump')
	# if (tim_rect.colliderect(snail_rect)):

	# if(tim_rect.collidepoint(mouse_pos)):
	#     print(pygame.mouse.get_pressed())
		

	pygame.display.update()
	clock.tick(60)