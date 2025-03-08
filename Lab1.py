import random

class Agent:
    def __init__(self, name, battery_level=100):
        self.name = name
        self.position = (0, 0)
        self.battery_level = battery_level
        self.board_size = (6, 6)
        self.trajectory = []

    def move(self, direction):
        x, y = self.position
        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < self.board_size[0] - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < self.board_size[1] - 1:
            y += 1
        else:
            print("Invalid move! Agent stays in the same position.")

        self.position = (x, y)
        self.battery_level -= 1
        self.trajectory.append(self.position)

    def decision(self):
        possible_moves = []

        x, y = self.position
        if x > 0:
            possible_moves.append("up")
        if x < self.board_size[0] - 1:
            possible_moves.append("down")
        if y > 0:
            possible_moves.append("left")
        if y < self.board_size[1] - 1:
            possible_moves.append("right")

        return random.choice(possible_moves)

    def play_game(self):
        while self.position != (5, 5) and self.battery_level > 0:
            next_move = self.decision()
            self.move(next_move)

        if self.battery_level <= 0:
            print(f"{self.name} ran out of battery. Game over!")
        # else:
            print(f"{self.name} reached the destination (5, 5) in {len(self.trajectory)} steps.")
            print("Trajectory:", self.trajectory)
            print("Number of steps taken:", len(self.trajectory))


# Example usage:
dummy_agent = Agent("Dummy")
dummy_agent.play_game()

