import random
import winsound

class Experience():
    def __init__(self, limit):
        self.limit = limit
        self.xp = 0
        self.xp_levels = 0

    def reset(self):
        self.xp = 0
        self.xp_levels = 0

    def add(self, xp=0, levels=0):
        self.xp += xp
        self.xp_levels += levels

        if self.xp > self.limit:
            while self.xp > self.limit:
                self.xp_levels += 1
                self.xp = self.xp - self.limit
                winsound.PlaySound("level_up.wav", winsound.SND_ASYNC)
        else:
            winsound.PlaySound("get_xp.wav", winsound.SND_ASYNC)

    def get_xp(self):
        return self.xp

    def get_levels(self):
        return self.xp_levels

    def get_limit(self):
        return self.limit

if __name__ == "__main__":
    xp_1 = Experience(limit=15)

    xp_1.add(xp=5, levels=2)
    xp_1.add(xp=12)

    print(f"XP: {xp_1.get_xp()}, LEVELS: {xp_1.xp_levels}")
