import pygame, sys
from checkers.constants import *
from checkers.game import Game
from checkers.pvp import PvP
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.font.init()
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu() :
    run = True
    text_col = BLACK

    while run:
        WIN.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), WIN, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)) :
            if click:
                PlayerVsPlayer()
        if button_2.collidepoint((mx, my)) :
            if click:
                PlayerVsAI()
        if button_3.collidepoint((mx, my)) :
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        pygame.draw.rect(WIN, (255, 0, 0), button_2)
        pygame.draw.rect(WIN, (255, 0, 0), button_3)
        draw_text('Player vs Player', font, (255, 255, 255), WIN, 50, 100)
        draw_text('Player vs AI', font, (255, 255, 255), WIN, 50, 200)
        draw_text('Quit', font, (255, 255, 255), WIN, 50, 300)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        clock.tick(60)

def PlayerVsAI():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

def PlayerVsPlayer():
        run = True
        clock = pygame.time.Clock()
        game = PvP(WIN)

        while run:
            clock.tick(FPS)

            if game.winner() != None:
                print(game.winner())
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
            
            game.update()
            pygame.display.update()
            clock.tick(60)
        pygame.quit()




main_menu()