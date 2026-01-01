<div align="center">

# 🌀 Let Us Play Polygonal Spirals 🌀

**creating hypnotic patterns with python because why not**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-brightgreen?style=for-the-badge)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-ff69b4?style=for-the-badge)

</div>

---

## 🎨 What's This About?

ever wondered what happens when you code geometric shapes that just keep growing and spinning? well, you get some pretty cool spirals that'll make you stare at your screen for way too long.  

this repo is basically me playing around with python's turtle graphics to create mesmerizing polygonal spirals.  it's simple, it's fun, and it looks awesome. 

---

## ✨ The Collection

### 🔺 Triangle Spiral
**3 sides of pure chaos**
- Color:  `#229302` (fresh green vibes)
- Sides: 3 
- Angle: 120°
- Loops: 500 times

### ⬠ Pentagon Spiral
**5 sides of elegance**
- Color: `#9C026B` (that deep magenta tho)
- Sides: 5
- Angle: 72°
- Loops: 500 times

### ⬡ Hexagon Spiral
**the OG, the first one i coded**
- Color: `cyan` (classic choice)
- Sides: 6
- Angle: 60°
- Loops: 2000 times
- *This is where it all started folks*

### ⭕ Circle-ish Spiral
**50 sides that look like...  well, you'll see**
- Color: `#9C026B` 
- Sides: 50 (basically a circle at this point)
- Angle: 7.2°
- Loops: 20000 times
- *looks weird, kinda like buri buri zaimon's nose from shinchan lol*

---

## 🚀 How to Run This Thing

1. **Clone the repo** (you know the drill)
   ```bash
   git clone https://github.com/willow788/let-us-play-polygonal-spirals.git
   cd let-us-play-polygonal-spirals
   ```

2. **Pick your poison** (choose a spiral)
   ```bash
   cd "Python Code Files/Triangle Code"
   # or Pentagon Code, or Hexagon Code, or Circle-like Code
   ```

3. **Run it**
   ```bash
   python main.py
   ```

4. **Watch the magic happen** ✨

---

## 🧠 How Does This Work?

super simple actually: 

1. **Pick a polygon** - triangle, pentagon, hexagon, or go wild with 50 sides
2. **Calculate the angle** - just `360 / number_of_sides` 
3. **Start small** - begin with a length of 2
4. **Loop and grow** - draw a side, turn right by the angle, increase the length
5. **Repeat** - keep going until you have a beautiful hypnotic pattern

```python
sides = 6  # hexagon
angle = 360 / sides
length = 2

for i in range(2000):
    forward(length)
    right(angle)
    length += 1  # this is where the magic happens
```

the length expanding each time we loop is what makes it a beautiful hypnotic pattern instead of just a boring polygon. 

---

## 📁 Repo Structure

```
let-us-play-polygonal-spirals/
│
├── Python Code Files/
│   ├── Triangle Code/
│   │   └── main.py
│   ├── Pentagon Code/
│   │   └── main.py
│   ├── Hexagon Code/
│   │   └── main. py
│   └── Circle-like Code/
│       └── main.py
│
└── Demonstration/
    ├── Triangle Demo/
    │   ├── trri.txt
    │   └── [screenshots]
    ├── Pentagon Demo/
    │   └── [screenshots]
    ├── Hexagon Demo/
    │   ├── 1.txt
    │   └── [screenshots]
    └── Circle Demo/
        ├── circ.txt
        └── [screenshots]
```

---

## 💡 Why Did I Make This?

- **For fun** - honestly that's the main reason
- **Practice** - rewrote similar code multiple times because it's good practice (and no, not because i'm a donkey)
- **Exploration** - wanted to see what different polygons would look like as spirals
- **Hypnotic patterns** - they're just satisfying to watch

---

## 🎯 Want to Experiment?

go ahead!  here's what you can play with:

- **Change the colors** - `color("your_color_here")`
- **Adjust the sides** - try different numbers
- **Modify the loop count** - more loops = bigger spirals
- **Change the speed** - `speed(0)` is fastest, try slower values to watch it draw
- **Play with length increment** - instead of `length += 1`, try `length += 2` or `length += 0.5`

---

## 📝 Notes

- i've attached screenshots of outputs instead of screen recordings because they take up a large amount of data and my laptop doesn't have much space (and i dont have that much patience too)
- look at the code, you'll understand it in a minute
- check the demonstration txt files for more casual explanations

---

## 🎉 Happy New Year Folks!

thanks for checking this out!   
now go create some spirals and get hypnotized 🌀

---

<div align="center">

**made with python, turtle graphics, and way too much free time**

⭐ star this repo if you like spirals ⭐

</div>
