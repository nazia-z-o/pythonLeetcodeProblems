class Solution:
    hash_max = 60001

    def hashCheck(self, x: int, y: int) -> (int, int):
        return (x, y * self.hash_max)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_set = set()
        for obs in obstacles:
            obs_set.add(self.hashCheck(obs[0], obs[1]))

        x, y = 0, 0
        maxSquare = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 0
        for cmd in commands:
            if cmd == -1:
                curr = (curr + 1) % 4
            elif cmd == -2:
                curr = (curr + 3) % 4
            else:
                dx, dy = directions[curr]
                for i in range(1, cmd + 1):
                    temp_x, temp_y = x + dx, y + dy
                    t = self.hashCheck(temp_x, temp_y)
                    if t in obs_set:
                        break
                    else:
                        x, y = temp_x, temp_y
                        maxSquare = max(maxSquare, x * x + y * y)

        return maxSquare
