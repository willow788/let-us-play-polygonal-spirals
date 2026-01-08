# 📐 Math & Turtle Tips

## How Polygonal Spirals Work

For a regular n-sided polygon:
- The interior angle is `angle = 360 / n`.
- Draw each side, turn, and slightly increase the length—this stretches the shapes into a dramatic spiral.

Example (Hexagon):
```python
import turtle
sides = 6
angle = 360 / sides
length = 2
for i in range(2000):
    turtle.forward(length)
    turtle.right(angle)
    length += 1
```

This method can be used with any sides ≥3!

## Turtle Performance

- Use `turtle.speed(0)` for fastest drawing.
- Use `turtle.hideturtle()` to remove the animated cursor for cleaner look.
- `turtle.bgcolor()` and `turtle.pencolor()` let you style your spirals.

## Fun Experiments

- Color gradients: change pen color inside the loop.
- Nonlinear growth: try `length *= 1.01` instead of `length += 1`.
- Negative increments or alternating angles for wild patterns.
- Save your art: `turtle.getscreen().getcanvas().postscript(file="spiral.eps")`

## Further Reading

- [Turtle graphics Python docs](https://docs.python.org/3/library/turtle.html)
- [Polygon formulas - Wikipedia](https://en.wikipedia.org/wiki/Regular_polygon)
- For advanced math: Try Fermat spirals, Fibonacci patterns, or combine polygons!
