# main.py
import turtle
from turtle import Screen
import random


# Hero class
class Hero(turtle.Turtle):
    def __init__(self, position, color="cyan"):
        super().__init__()
        self.shape("triangle")
        self.color(color)
        self.shapesize(stretch_wid=2, stretch_len=2)  # bigger ship
        self.setheading(90)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x > 280:  # right boundary of rectangle
            new_x = 280
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x < -280:  # left boundary of rectangle
            new_x = -280
        self.goto(new_x, self.ycor())


# Bullet class
class Bullet(turtle.Turtle):
    def __init__(self, position, color="red"):
        super().__init__()
        self.shape("square")  # base shape
        self.color(color)
        self.shapesize(stretch_wid=0.3, stretch_len=0.8)  # thin and small
        self.penup()
        self.goto(position)
        self.speed(0)  # instant drawing speed

    def move(self):
        self.sety(self.ycor() + 8)  # move upward - SLOWER


# Alien class
class Alien(turtle.Turtle):
    def __init__(self, position, color="white"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.goto(position)
        self.direction = 1
        self.speed(0)

    def move(self):
        new_x = self.xcor() + (self.direction * 8)  # FASTER alien movement - increased more
        if new_x > 280 or new_x < -280:
            self.direction *= -1
            self.sety(self.ycor() - 50)  # drop down more
        else:
            self.setx(new_x)


# Alien Bullet class
class AlienBullet(turtle.Turtle):
    def __init__(self, position, color="yellow"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=0.3, stretch_len=0.8)  # thin laser
        self.penup()
        self.goto(position)
        self.speed(0)

    def move(self):
        self.sety(self.ycor() - 10)  # move downward (slower than hero bullets)



# Shield class - FIXED
class Shield(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)  # thick but short
        self.goto(position)
        self.health = 3  # shield can take 3 hits

    def hit(self):
        """Call this when a bullet hits the shield"""
        self.health -= 1
        if self.health == 2:
            self.color("yellow")  # slightly damaged
        elif self.health == 1:
            self.color("red")  # critical
        elif self.health <= 0:
            self.hideturtle()  # destroyed
            return True  # shield destroyed
        return False  # shield still alive


screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.tracer(0)

hero = Hero(position=(0, -250))
bullets = []  # hero bullets
alien_bullets = []  # alien bullets
aliens = []
shields = []  # shield blocks
lives = 5  # hero lives - CHANGED TO 5
score = 0  # NEW: score system
level = 1  # NEW: level system
game_state = "playing"  # playing, won, game_over
last_bullet_time = 0  # NEW: bullet cooldown

# Score / Lives display - UPDATED to corner
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(-480, 250)  # moved to corner
score_writer.write(f"Lives: {lives}\nScore: {score}\nLevel: {level}", font=("Arial", 16, "bold"))


def update_display():
    score_writer.clear()
    score_writer.goto(-480, 250)  # corner position
    score_writer.write(f"Lives: {lives}\nScore: {score}\nLevel: {level}", font=("Arial", 16, "bold"))


def fire_bullet():
    global last_bullet_time
    import time
    current_time = time.time()

    # Only allow firing every 0.3 seconds (300ms cooldown)
    if current_time - last_bullet_time > 0.3:
        bullet = Bullet(position=(hero.xcor(), hero.ycor() + 20))
        bullets.append(bullet)
        last_bullet_time = current_time


def next_level():
    global level, aliens, shields, game_state, hero, score_writer
    if game_state == "won":
        level += 1
        game_state = "playing"

        # Clear screen messages
        screen.clear()

        # Redraw everything
        draw_border()

        # Recreate hero
        hero = Hero(position=(0, -250))

        # Recreate scoreboard
        score_writer = turtle.Turtle()
        score_writer.hideturtle()
        score_writer.color("white")
        score_writer.penup()

        # Recreate aliens for next level
        start_x, start_y = -200, 200
        aliens = []
        for row in range(4):
            for col in range(4):
                alien = Alien(position=(start_x + col * 100, start_y - row * 60))
                aliens.append(alien)

        # Recreate shields
        shields = [
            Shield(position=(-150, -180)),
            Shield(position=(0, -180)),
            Shield(position=(150, -180))
        ]

        # Reset key bindings for new hero
        screen.listen()
        screen.onkeypress(hero.go_left, "Left")
        screen.onkeypress(hero.go_right, "Right")
        screen.onkey(fire_bullet, "space")
        screen.onkeypress(next_level, "n")

        update_display()


# Key bindings
screen.listen()
screen.onkeypress(hero.go_left, "Left")
screen.onkeypress(hero.go_right, "Right")
screen.onkey(fire_bullet, "space")
screen.onkeypress(next_level, "n")  # NEW: next level key


def draw_border():
    border = turtle.Turtle()
    border.hideturtle()
    border.color("white")
    border.pensize(3)
    border.penup()
    border.goto(-300, -280)
    border.pendown()
    for _ in range(2):
        border.forward(600)
        border.left(90)
        border.forward(560)
        border.left(90)


draw_border()

# Make 4x4 grid of aliens
start_x, start_y = -200, 200
for row in range(4):
    for col in range(4):
        alien = Alien(position=(start_x + col * 100, start_y - row * 60))
        aliens.append(alien)

# Create 3 small shields above the hero
shields = [
    Shield(position=(-150, -180)),  # left shield
    Shield(position=(0, -180)),  # middle shield
    Shield(position=(150, -180))  # right shield
]


def game_over():
    global game_state
    game_state = "game_over"
    go = turtle.Turtle()
    go.hideturtle()
    go.color("red")
    go.penup()
    go.goto(0, 0)
    go.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
    screen.update()


def you_won():
    global game_state
    game_state = "won"
    win = turtle.Turtle()
    win.hideturtle()
    win.color("green")
    win.penup()
    win.goto(0, 0)
    win.write("YOU WON!", align="center", font=("Arial", 40, "bold"))
    screen.update()



def game_loop():
    global lives, score, game_state

    if game_state != "playing":
        screen.ontimer(game_loop, 50)
        return

    # Move hero bullets
    for bullet in bullets[:]:
        bullet.move()
        if bullet.ycor() > 280:
            bullet.hideturtle()
            bullets.remove(bullet)

        # Collision check with aliens - UPDATED WITH SCORE
        for alien in aliens[:]:
            if bullet.distance(alien) < 25:
                alien.hideturtle()
                aliens.remove(alien)
                bullet.hideturtle()
                bullets.remove(bullet)
                score += 10  # NEW: add score - CHANGED TO 10
                update_display()
                break

        # Collision check with shields - FIXED
        for shield in shields[:]:
            if bullet.distance(shield) < 30:  # increased collision area
                if shield.hit():  # shield destroyed
                    shields.remove(shield)
                bullet.hideturtle()
                bullets.remove(bullet)
                break

    # Move aliens + chance to fire
    for alien in aliens[:]:
        alien.move()

        # Check if alien touched hero - GAME OVER
        if alien.distance(hero) < 30:
            game_over()
            return

        # Check if alien touched shield - ALIEN LOSES
        for shield in shields[:]:
            if alien.distance(shield) < 35:
                alien.hideturtle()
                aliens.remove(alien)
                break

        # More difficult alien firing based on level
        fire_chance = max(50, 200 - (level * 30))  # gets harder each level
        if random.randint(1, fire_chance) == 1:
            alien_bullet = AlienBullet(position=(alien.xcor(), alien.ycor() - 20))
            alien_bullets.append(alien_bullet)

    # Check if all aliens destroyed - YOU WON
    if not aliens:
        you_won()
        return

    # Move alien bullets
    for ab in alien_bullets[:]:
        ab.move()
        if ab.ycor() < -280:
            ab.hideturtle()
            alien_bullets.remove(ab)

        # Check collision with shields - FIXED
        for shield in shields[:]:
            if ab.distance(shield) < 30:  # increased collision area
                if shield.hit():  # shield destroyed
                    shields.remove(shield)
                ab.hideturtle()
                alien_bullets.remove(ab)
                break

        # Collision with hero
        if ab in alien_bullets and ab.distance(hero) < 25:
            ab.hideturtle()
            alien_bullets.remove(ab)

            lives -= 1
            update_display()

            if lives <= 0:
                game_over()
                return

    screen.update()
    screen.ontimer(game_loop, 50)


game_loop()
screen.mainloop()