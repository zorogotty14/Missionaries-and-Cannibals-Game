import pygame
from Person import person
from Boat import boat
from aisolver import breadth_first_search, print_solution, State  # Import the BFS solver and State class

pygame.init()
display_width = 1280
display_height = 650
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Setting color values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_red = (226, 110, 110)

# Loading images
boatImg = pygame.image.load('images/boat.png')
bgImg = pygame.image.load('images/bg1.png')
mImg = pygame.image.load('images/missionary.png')
cImg = pygame.image.load('images/cannibal.png')
c1Img = pygame.image.load('images/cannibal1.png')
m1Img = pygame.image.load('images/missionary1.png')
ngImg = pygame.image.load('images/newgame.png')
ng1Img = pygame.image.load('images/newgame1.png')
gameoverImg = pygame.image.load('images/gameover.png')
wonImg = pygame.image.load('images/winner.png')
goImg = pygame.image.load('images/go.png')
go1Img = pygame.image.load('images/go1.png')
soundonImg = pygame.image.load('images/soundon.png')
soundoffImg = pygame.image.load('images/soundoff.png')
gameoversd = pygame.mixer.Sound('music/gameover.wav')
wonsd = pygame.mixer.Sound('music/won.wav')

# Setting default font
font = pygame.font.SysFont(None, 25)

def animate_solution(solution_path, gameDisplay, mc, boat, font):
    for state in solution_path:
        gameDisplay.blit(bgImg, (0, 0))
        gameDisplay.blit(ngImg, (1000, 45))
        gameDisplay.blit(soundonImg, (1150, 40))
        gameDisplay.blit(boatImg, (boat.x, boat.y))

        # Update the display of missionaries and cannibals
        for i, person in enumerate(mc):
            if person.char == 'M':
                person.x = 50 + (i * 60) if state.missionaryLeft > i else 1050 + ((i - state.missionaryLeft) * 60)
            else:
                person.x = 50 + (i * 60) if state.cannibalLeft > i - 3 else 1050 + ((i - 3 - state.cannibalLeft) * 60)
            person.display()

        # Display state
        state_text = font.render("State: " + f"({state.cannibalLeft}, {state.missionaryLeft}, {state.boat}, {state.cannibalRight}, {state.missionaryRight})", True, black)
        gameDisplay.blit(state_text, [20, 20])

        pygame.display.update()
        pygame.time.wait(1000)  # Wait for 1 second between steps

def main():
    x = (display_width * 0.1)
    y = (display_height * 0.8)
    x_change, y_change = 0, 0

    # Creating missionaries and cannibals objects
    mc = []
    mc.append(person(x - 135, y - 100, 0, 0, 'M', 'left', mImg, m1Img, gameDisplay))
    mc.append(person(x - 90, y - 100, 0, 0, 'M', 'left', mImg, m1Img, gameDisplay))
    mc.append(person(x - 45, y - 100, 0, 0, 'M', 'left', mImg, m1Img, gameDisplay))
    mc.append(person(x - 135, y - 250, 0, 0, 'C', 'left', cImg, c1Img, gameDisplay))
    mc.append(person(x - 90, y - 250, 0, 0, 'C', 'left', cImg, c1Img, gameDisplay))
    mc.append(person(x - 45, y - 250, 0, 0, 'C', 'left', cImg, c1Img, gameDisplay))

    # Creating boat position objects
    boat_pos = boat(157, 478, 2, m1Img, c1Img, gameDisplay)

    pygame.display.set_caption('Missionaries and Cannibals')
    clock = pygame.time.Clock()
    crashed = False
    boat_position = 0  # Indicates boat at left shore
    a, b = 0, 0
    action = [a, b]  # Indicates no of missionaries and cannibals to move
    m, c, bt = 3, 3, 1  # Indicates 3 missionaries, 3 cannibals and boat at left shore
    state = State(m, c, 'left', 0, 0)  # Initial state of missionaries, cannibals, and boat

    gameover = False
    gameoverplayed, wonplayed = False, False
    left, right = False, False
    won = False
    moves = 0  # For counting the number of moves

    # Loading the background music
    pygame.mixer.music.load('music/bgmusic.mp3')
    pygame.mixer.music.play(-1)  # Play the bg music infinite times
    sound = True

    # Solve the problem using BFS
    missionaries = 3
    cannibals = 3
    solution = breadth_first_search(missionaries, cannibals)

    # Generate the solution path
    solution_path = []
    if solution:
        path = []
        path.append(solution)
        parent = solution.parent
        while parent:
            path.append(parent)
            parent = parent.parent

        for t in range(len(path)):
            state = path[len(path) - t - 1]
            solution_path.append(state)

    # Animate the solution
    animate_solution(solution_path, gameDisplay, mc, boat_pos, font)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.blit(bgImg, (0, 0))
        gameDisplay.blit(ngImg, (1000, 45))
        if sound:
            gameDisplay.blit(soundonImg, (1150, 40))
        else:
            gameDisplay.blit(soundoffImg, (1150, 40))

        # Display the missionaries and cannibals
        for i in range(6):
            mc[i].display()

        # Display state, actions, and moves
        state_text = font.render(f"State: ({state.cannibalLeft}, {state.missionaryLeft}, {state.boat}, {state.cannibalRight}, {state.missionaryRight})", True, black)
        gameDisplay.blit(state_text, [20, 20])
        action_text = font.render("Action: " + str(action), True, black)
        gameDisplay.blit(action_text, [20, 50])
        moves_text = font.render("No. of moves: " + str(moves), True, black)
        gameDisplay.blit(moves_text, [20, 80])
        cur = pygame.mouse.get_pos()  # Getting cursor position

        # Click and point actions of sound button
        if 1150 + 50 > cur[0] > 1150 and 40 + 50 > cur[1] > 40:
            if sound:
                gameDisplay.blit(soundoffImg, (1150, 40))
            else:
                gameDisplay.blit(soundonImg, (1150, 40))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if sound:
                    sound = False
                    pygame.mixer.music.pause()
                else:
                    sound = True
                    pygame.mixer.music.play()

        # Click and point actions of new game button
        if 1000 + 119 > cur[0] > 1000 and 45 + 36 > cur[1] > 45:
            gameDisplay.blit(ng1Img, (1000, 20))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                main()
        gameDisplay.blit(boatImg, (x, y))  # Display boat

        # Checking gameover
        if (state.missionaryLeft < state.cannibalLeft and state.missionaryLeft > 0) or (state.missionaryRight < state.cannibalRight and state.missionaryRight > 0):
            gameDisplay.blit(gameoverImg, (400, 250))
            gameover = True

        # Checking game won
        if state.is_goal() and action == [0, 0]:
            gameDisplay.blit(wonImg, (400, 250))
            won = True

        # Update boat position for movement
        x = x + x_change

        # Update missionary and cannibal position for movement
        for i in range(6):
            mc[i].x += mc[i].x_change
        action = [a, b]

        pygame.display.update()
        clock.tick(25)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
