import turtle

def main():
    tina = turtle.Turtle()
    # Shapes: 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    tina.shape("arrow")

    x = 1
    tina.speed(10000)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for i in range(100):
        for i in colors:
            tina.forward(x * 0.3)
            tina.left(60)
            tina.color(i)
            tina.right(30.5)
            x = x + 1

if __name__ == "__main__":
    main()
