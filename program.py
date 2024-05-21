bricksplan = ["⚪️", "⚪️ ⚪️", "⚪️ ⚪️ ⚪️", "⚪️ ⚪️ ⚪️ ⚪️"]
bricksview =["⬜️", "⬜️ ⬜️", "⬜️ ⬜️ ⬜️", "⬜️ ⬜️ ⬜️ ⬜️"]
print("Welcome to bricks warehouse. This is your playground to make your dream come true with bricks!")
print("__________________________________________________")
print("Choose from the bricks library to construct:")

print(bricksplan)
plan = []
view = []
programrun = True

while programrun:
        inp = int(input("Choose a brick (1-4): "))
        if 1 <= inp <= len(bricksplan):
            plan.append(bricksplan[inp-1])
            view.append(bricksview[inp-1])
            print("PLAN:", "".join(plan))
            print("VIEW:", "".join(view))
            # print("PLAN:", plan)
            # print("VIEW:", view)
        else:
          programrun = False
          print("invalid input")



