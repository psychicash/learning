
class Pylon_a(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = get_image('images/test1.png')
        self.image = pygame.transform.scale(self.image, (270//2,350//2))

        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)

        self.rect.x = x
        self.rect.y = y
        self.creation_time = pygame.time.get_ticks()
        self.last = pygame.time.get_ticks()
        self.alph = 0
        self.alph_direction = 'in'
        self.rocking_direction = 'up'

    def update(self):
        if self.alph_direction == 'in':
            self.alph += 2
            self.image.set_alpha(self.alph)
            if self.alph >= 255:
                self.alph_direction = 'out'
        elif self.alph_direction == 'out':
            self.alph -= 2
            self.image.set_alpha(self.alph)
            if self.alph <= 0:
                self.alph_direction ='in'
        if self.rocking_direction == 'up':
            self.rect.y += 0.1


class Pylon_b(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = get_image('./images/test5.png') #background
        self.image = pygame.transform.scale(self.image, (417 // 2, 86 // 2))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x - (270//7)
        self.rect.y = y + (350//4)

    def update(self):
        pass

class Pylon_c(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = get_image('./images/test6.png')
        self.image = pygame.transform.scale(self.image, (467 // 2, 175 // 2))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x - (270 // 7) - 11
        self.rect.y = y + (350 // 4) - 5

    def update(self):
        pass
        
        
        # later in the game loop
        
class Game(object):                                     #class reps an instance of the game
    def __init__(self):                                 #creates all attributes of the game
        
        self.game_over = False
        self.all_sprites_list = pygame.sprite.Group() #create sprite lists
        #self.player = Player()  #create the player
        #self.player_list = pygame.sprite.Group()
        #self.player_list.add(self.player)

        self.pylon1 = Pylon_a(x= SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2)
        self.pylon1_list = pygame.sprite.Group()
        self.pylon1_list.add(self.pylon1)

        self.pylon2 = Pylon_b(x=SCREEN_WIDTH//2, y = SCREEN_HEIGHT//2)
        self.pylon2_list= pygame.sprite.Group()
        self.pylon2_list.add(self.pylon2)

        self.pylon3 = Pylon_c(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)
        self.pylon3_list = pygame.sprite.Group()
        self.pylon3_list.add(self.pylon3)

    def run_logic(self):
       
        if not self.game_over:                          
            self.all_sprites_list.update()             
            self.pylon1_list.update()
            self.pylon2_list.update()
            self.pylon3_list.update()
            
            
            
def display_frame(self, screen):
            
  screen.fill(DK_GREEN)


  if self.game_over:                      #game over screen
     pass

  if not self.game_over:
      self.all_sprites_list.draw(screen)
      self.pylon2_list.draw(screen)
      self.pylon1_list.draw(screen)
      self.pylon3_list.draw(screen)
