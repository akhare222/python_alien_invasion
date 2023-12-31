import sys
import pygame
import settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Overall class to manage games assets and behavior'''

    def __init__(self):
        "Initialize the game and create game resources"
        pygame.init()

        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion!")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:                       
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()         
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events""" 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_keydown_events(event)
            self._check_keyup_events(event)
    
    def _fire_bullet(self):
        """Create new bullet and add it to the bullets group"""
        if len(self.bullets) < settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keypresses"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
   
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()
    
    def _update_bullets(self):
        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


