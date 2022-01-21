from data_class import Experience as exp
import random

xp = exp(limit=int(input("Limit: ")))
to_add = 0

print("Menu")

while True:
    print(f"You have {xp.get_xp()} xp and {xp.get_levels()} levels!")
    ans = input("GetXp or Restart? (g/r)")

    if ans == "g":
        # get xp
        to_add = random.randint(1, xp.get_limit()-5)
        xp.add(xp=to_add)
        print(f"Added {to_add} experience points!")
    elif ans == "r":
        # restart
        xp.reset()
        print("Reset experience points and levels!")
    elif ans == "stop":
        # stop the process
        break
    else:
        print(f"Invalid input: {ans}!")
