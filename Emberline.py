name = "Customer"
print("Hello,", name)
print("Emberline is real.")
for i in range(1, 4):
    print("Building Emberline - step", i)
def do_step(step_name):
    print("Emberline doing:",step_name)
    return True

def base_battery_ok(level, threshold):
    return level >= threshold
def run_all(steps, battery_level, threshold):
    if base_battery_ok(battery_level, threshold):
        for step in steps:
            do_step(step)
    else:
        print("Charge first.")
steps = (["sweep_floor", "bring_water",
    "wash_dishes"])

# battery 80, need at least 20 -> runs the steps
run_all,(steps, 80, 20)

#battery 10, need at least 20 -> prints Charge first
run_all(steps, 10, 20)

for step in steps:
    print(step)
print("Done for now.")

def handle_bump(bumped):
    if bumped:
        print("Bump! Turning around.")
        return "turn"
    else:
        print("Path clear.")
        return "forward"
handle_bump(True)
action = handle_bump(False)  #True to test bump
print("Action:", "cleaning in progress")
def needs_dock(level,
threshold):
    return level < threshold

def go_dock():
    print("Emberline docking to charge.")
    return "dock"
threshold = 20

def status(battery, bumped):
# starts here
    if needs_dock(battery, 20):
#inside (indented)
        return go_dock()
    if bumped:
        return "turn"
    return "keep_working"
#still inside
print(status(15, False))  #should dock
print(status(80, True))   #should turn
print(status(80, False))  #should keep working
#OUTSIDE - no indent, runs on its ownpreter) to run Python online.

chores = ["sweep_floor",
"bring_water", "wash_dishes",
"say_hello"]

def run_chores(battery, bumped,
chore_list):
  state = status(battery,
bumped)
  print("State:", state)
  if state != "keep_working":
    return
  for chore in chore_list:
    print("Emberline doing:",
chore)

run_chores(80, False, chores)
run_chores(15, False, chores)
run_chores(80, True, chores)

def main():
  print("Emberline v0.1")
  run_chores(80, False, chores)
  run_chores(15, False, chores)
  run_chores(80, True, chores)
main()

def drive(direction):
  print("Driving", direction)
  return direction

def run_chores(battery, bumped,
chore_list):
  state = status(battery,
bumped)
  print("State:", state)
  if state == "dock":
      return
  if state == "turn":
      drive ("left")
      return
  drive("forward")
  for chore in chore_list:
      print ("Emberline doing:",
  chore)

def use_battery(level, use = 5):
    level = level - use
    if level < 0:
      level = 0
    print("Battery now:", level)
    return level

def needs_dock(battery): 
    if battery <= 20:
      print("Dock now:")
      return True
    return False

battery = 15
if needs_dock(battery):
  print("Go charge")
