<div align="center">

# 🍀 Let Us Play Polygonal Spirals 🍀

**Creating hypnotic patterns with Python's turtle graphics!**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-brightgreen?style=for-the-badge)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-ff69b4?style=for-the-badge)

</div>

---

## 🎨 What's This About?

Ever wondered what happens when you code geometric shapes that keep growing and spinning? You get mesmerizing spirals that are both mathematically elegant and visually captivating.

This repo explores polygonal spirals using Python's built-in turtle graphics for interactive, educational, and artistic fun.  
Great for beginners, educators, or anyone curious about creating generative art with code.

---

## ✨ The Collection

Each subfolder runs a classic or creative spiral:

### 🔺 Triangle Spiral
- Color:  `#229302`
- Sides: 3
- Angle: 120°
- Loops: 500

### ⬟ Pentagon Spiral
- Color: `#9C026B`
- Sides: 5
- Angle: 72°
- Loops: 500

### ⬡ Hexagon Spiral
- Color: `cyan`
- Sides: 6
- Angle: 60°
- Loops: 2000

### ⭕ Circle-ish Spiral
- Color: `#9C026B`
- Sides: 50 (almost a circle)
- Angle: 7.2°
- Loops: 20000

---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/willow788/let-us-play-polygonal-spirals.git
   cd let-us-play-polygonal-spirals
   ```

2. **Pick a spiral**
   ```bash
   cd "Python Code Files/Triangle Code"
   # or Pentagon Code, or Hexagon Code, or Circle-like Code
   ```

3. **Run it**
   ```bash
   python main.py
   ```

4. **Enjoy the show!**

Requires only Python 3 (no extra libraries needed; `turtle` is included in the standard library).

---

## 🧠 How Does It Work?

1. Choose a polygon: triangle, pentagon, hexagon, or a high-sided "circle".
2. Compute the turning angle: `360 / number_of_sides`.
3. Start with an initial side length.
4. Loop:
    - Draw a side,
    - Turn right by the angle,
    - Increase the length.
5. Repeat for hundreds or thousands of iterations.

```python
sides = 6        # hexagon, for example
angle = 360 / sides
length = 2
for i in range(iterations):
    turtle.forward(length)
    turtle.right(angle)
    length += 1
```

---

## 🗂️ Repository Structure

```
let-us-play-polygonal-spirals/
├── Python Code Files/
│   ├── Triangle Code/
│   │   └── main.py
│   ├── Pentagon Code/
│   │   └── main.py
│   ├── Hexagon Code/
│   │   └── main.py
│   └── Circle-like Code/
│       └── main.py
├── Demonstration/
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⭐️ Ideas for Expansion

- Try different colors, drawing speeds, or background themes.
- Experiment with the side increment (change by more than 1, or use a non-linear increase).
- Combine multiple spirals for layered art.
- Add keyboard controls or interactive parameters.

---

## 📄 License

MIT License — see [LICENSE](LICENSE).  
You are free to use, modify, and share.

---

## 👤 Author

Made with ❤️ by [willow788](https://github.com/willow788)

---

**If these spirals delight you (or your inner child), give the repo a star!**
