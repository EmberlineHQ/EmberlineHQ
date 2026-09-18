name = "Customer"
print("Hello,", name)
print("Emberline is real.")
for i in range(1, 4):
    print("Building Emberline - step", i)

def do_step(step_name):
    print("Emberline doing:", step_name)
    return True

def base_battery_ok(level, threshold):
    return level >= threshold

def use_battery(level, use=5):
    level = level - use
    if level < 0:
        level = 0
    print("Battery now:", level)
    return level

def run_all(steps, battery_level, threshold):
    if base_battery_ok(battery_level, threshold):
        for step in steps:
            do_step(step)
            battery_level = use_battery(battery_level)
    else:
        print("Charge first.")

steps = ["sweep_floor", "bring_water", "wash_dishes"]

def handle_bump(bumped):
    if bumped:
        print("Bump! Turning around.")
        return "turn"
    print("Path clear.")
    return "forward"

def needs_dock(battery, threshold=20):
    if battery <= threshold:
        print("Dock now")
        return True
    return False

def go_dock():
    print("Emberline docking to charge.")
    return "dock"

def status(battery, bumped):
    if needs_dock(battery):
        return go_dock()
    if bumped:
        return "turn"
    return "keep_working"

def run_chores(battery, bumped, chore_list):
    state = status(battery, bumped)
    print("State:", state)
    if state != "keep_working":
        return
    for chore in chore_list:
        print("Emberline doing:", chore)

def main():
    print("Emberline v0.1")
    print("--- run_all checks ---")
    run_all(steps, 80, 20)
    run_all(steps, 10, 20)
    print("--- bump / status ---")
    handle_bump(True)
    handle_bump(False)
    print(status(15, False))
    print(status(80, True))
    print(status(80, False))
    print("--- chores ---")
    run_chores(80, False, steps)
    run_chores(15, False, steps)
    print("--- location - - -")
    room = where_am_i("living room")
    room = where_am_i("kitchen")
    room = where_am_i("outside")
    print("Last room was:", room)
    print("Done for now.")

main()
