class Solution:
    def robotSim(self, commands, obstacles):
        # Store obstacles
        blocked = set()
        for o in obstacles:
            blocked.add((o[0], o[1]))

        # Directions: North, East, South, West
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]

        x, y = 0, 0
        dir = 0  # initially facing North