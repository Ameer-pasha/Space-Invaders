# 🚀 Space Invaders Game

A classic Space Invaders game built with Python's turtle graphics library. Defend Earth from the alien invasion!

## 🎮 Game Features

- **Classic Space Invaders gameplay** - Shoot aliens before they reach you
- **Progressive difficulty** - Aliens fire more frequently as levels increase
- **Destructible shields** - Use cover that degrades over time (3 hits each)
- **Multiple lives** - Start with 5 lives
- **Scoring system** - Earn 10 points per alien destroyed
- **Level progression** - Complete levels to advance
- **Smooth controls** - Responsive movement and firing with cooldown

## 🕹️ How to Play

### Controls
- **Left Arrow** ← - Move hero left
- **Right Arrow** → - Move hero right  
- **Spacebar** - Fire bullets (300ms cooldown)
- **N** - Next level (when you win)

### Gameplay
1. **Objective**: Destroy all aliens to advance to the next level
2. **Avoid**: Don't let aliens reach you or hit you with their bullets
3. **Strategy**: Use shields for protection, but they can only take 3 hits each
4. **Scoring**: Each alien destroyed gives you 10 points

### Game Over Conditions
- ❌ Aliens reach your position
- ❌ You lose all 5 lives from alien bullets

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No additional libraries required (uses built-in `turtle` module)

### Running the Game
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/space-invaders-game.git
   cd space-invaders-game
   ```

2. **Run the game**
   ```bash
   python main.py
   ```
   Or on some systems:
   ```bash
   python3 main.py
   ```

## 🎯 Game Mechanics

### Hero
- **Movement**: 20 pixels per key press
- **Boundary**: Contained within game borders
- **Firing**: Limited to prevent spam (300ms cooldown)

### Aliens
- **Movement**: Move horizontally as a group, drop down when hitting edges
- **Speed**: 8 pixels per move (faster than original)
- **Firing**: Random chance increases with each level
- **Collision**: Destroyed when touching shields

### Shields
- **Health**: 3 hits each
- **Visual feedback**: Green → Yellow → Red → Destroyed
- **Position**: Strategically placed between hero and aliens

### Difficulty Progression
- **Level 1**: Aliens fire rarely (1/200 chance)
- **Level 2**: Moderate firing (1/170 chance)
- **Level 3+**: Increasingly aggressive (minimum 1/50 chance)

## 📁 Project Structure

```
space-invaders-game/
│
├── main.py              # Main game file with all classes and logic
├── requirements.txt     # Dependencies (none needed)
├── README.md           # This file
└── .gitignore          # Git ignore file
```

## 🏗️ Code Structure

### Classes
- **Hero**: Player-controlled spaceship
- **Bullet**: Hero projectiles
- **Alien**: Enemy spaceships with AI movement
- **AlienBullet**: Enemy projectiles
- **Shield**: Destructible cover objects

### Key Functions
- `game_loop()`: Main game logic and collision detection
- `fire_bullet()`: Bullet creation with cooldown
- `next_level()`: Level progression system
- `update_display()`: Score and lives UI updates

## 🎨 Game Features Detail

### Visual Elements
- **Clean border**: White rectangular game boundary
- **Color-coded shields**: Visual health indication
- **Smooth animations**: 50ms game loop for fluid movement
- **Clear UI**: Lives and score display in corner

### Game Balance
- **Hero bullets**: Slower speed (8 pixels/frame) for challenge
- **Alien bullets**: Medium speed (10 pixels/frame)
- **Alien movement**: Fast horizontal movement (8 pixels)
- **Shield durability**: Balanced for strategic gameplay

## 🚧 Future Enhancements

Potential features to add:
- [ ] Sound effects
- [ ] Power-ups (faster firing, shields, multi-shot)
- [ ] Different alien types with varying points
- [ ] Boss battles
- [ ] High score persistence
- [ ] Particle effects
- [ ] Multiple difficulty modes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎮 Screenshots

<img width="1489" height="884" alt="image" src="https://github.com/user-attachments/assets/df6ee103-990c-4abd-bc29-78f7c4af6122" />

## 👨‍💻 Author

Created with ❤️ by Ameer Pasha

---

**Enjoy defending Earth from the alien invasion! 🛸👾**
