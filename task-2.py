import turtle


def draw_pythagoras_tree(branch_length: float, turtle_cursor: turtle.Turtle, angle: int, recursion_depth: int):
    if recursion_depth == 0:
        return
    else:
        turtle_cursor.forward(branch_length)
        turtle_cursor.right(angle)
        draw_pythagoras_tree(branch_length * 0.7,
                             turtle_cursor, angle, recursion_depth - 1)
        turtle_cursor.left(angle * 2)
        draw_pythagoras_tree(branch_length * 0.7,
                             turtle_cursor, angle, recursion_depth - 1)
        turtle_cursor.right(angle)
        turtle_cursor.backward(branch_length)


if __name__ == "__main__":
    recursion_depth = int(
        input("Enter the recursion depth for the Pythagorean tree: "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle_cursor = turtle.Turtle()
    turtle_cursor.color("green")
    turtle_cursor.width(2)
    turtle_cursor.speed(0)
    turtle_cursor.left(90)

    draw_pythagoras_tree(100, turtle_cursor, 45, recursion_depth)
    screen.exitonclick()
