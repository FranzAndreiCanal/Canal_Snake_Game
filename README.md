# Snake Game in Pygame

+ Hello! I am Franz Andrei G. Canal.
+ In order to run the Snake Game, open the "main.py" which is contained inside the folder.
+ Note: Make sure that Pygame is installed in your device to avoid any errors.

## Video Presentation
+ 

# Overview

Welcome to the Snake Game, a classic arcade-style game implemented in Python using the Pygame library. This project provides a simple and enjoyable rendition of the iconic Snake Game, where players control a snake navigating a grid, consuming apples to grow longer.

# Features

## I. Snake Movement
+ Control the snake's movement using arrow keys: Up, Down, Left, and Right.
+ The snake's direction is responsive and smoothly updates based on user input.

## II. Apple Consumption
+ Apples randomly spawn on the grid for the snake to devour.
+ Upon consuming an apple, the snake's length increases, adding a layer of challenge as the game progresses.

## III. Game Over Conditions
+ The game resets if the snake collides with its own body, preventing self-intersection.
+ Boundary collisions trigger a game reset, ensuring a continuous and challenging gameplay experience.

# Snake Game in Pygame: Code Walkthrough

**Introduction**
+ Welcome, everyone! Today, we're diving into the code of a classic Snake Game implemented using Pygame. This simple yet engaging game brings back nostalgic memories for many, and we'll explore how it works and what makes it tick.

**Initialization**
+ Let's start with the setup. We initialize Pygame, set up the game window, and define some constants. The game window is 800x800 pixels, and we've got a block size of 50 pixels.

![1](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/614bdee5-322f-4d58-a14e-755869c0f728)

**Snake Class**
+ Now, let's take a look at the '**Snake**' class. This class manages the snake's behavior, including its movement, interaction with the game environment, and handling user input.

![2](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/8136df0b-a1d1-4290-b441-671c1800bc20)

**Apple Class**
+ Next up, the '**Apple**' class. This class represents the apples that the snake can eat. Apples spawn randomly on the grid, and when the snake consumes one, a new one appears.

![3](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/7cfcb864-2a29-4331-adcb-6c058a3bd64e)

**Grid Drawing**
+ We also have a function, '**draw_grid()**', responsible for rendering the grid on the game screen. This adds structure and visual appeal to our Snake Game.

![4](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/b7119263-42b6-4b25-8397-cdc4e819e29c)

**Game Loop**
+ Now, let's talk about the game loop. This loop is the heartbeat of our game, handling events, updating the game state, and rendering everything on the screen.

![5](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/e5b58fd0-47cc-4ddb-97d9-5abed8b7e8ef)

**Conclusion**
+ And there you have it – a detailed exploration of the code behind this Snake Game. From handling user input to managing game states, collision detection, and visual rendering, this code encapsulates fundamental game development concepts. Feel free to dissect and modify it as you embark on your own game development adventures.

Enjoy the journey, happy coding, and most importantly, happy gaming!



# Output

![403410685_1038340767384559_2198815117007840106_n](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/abafa0e1-4921-4d90-89f5-ed4bf6f54ec3)
![403408774_181694194964682_1203976614677370474_n](https://github.com/FranzAndreiCanal/Canal_Snake_Game/assets/145314497/ad0a70c9-12f7-4061-9f8c-7cf944e61566)
