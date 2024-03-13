from robot import Robot

if __name__ == "__main__":
    robot = Robot()
    test_file = "test3.txt"

    with open(test_file, "r") as file:
        for line in file:
            line = line.strip()
            words = line.split()
            command = words[0]
            if command == "PLACE":
                x, y, f = words[1].split(",")
                x = int(x)
                y = int(y)
                robot.place(x, y, f)
            elif command == "MOVE":
                robot.move()
            elif command == "LEFT":
                robot.left()
            elif command == "RIGHT":
                robot.right()
            elif command == "REPORT":
                robot.report()




