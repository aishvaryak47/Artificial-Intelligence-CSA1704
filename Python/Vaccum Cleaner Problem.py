def vacuum_world():
    # Initial state
    state = {'A': 'dirty', 'B': 'dirty'}
    location = 'A'
    steps = 0

    while state['A'] == 'dirty' or state['B'] == 'dirty':
        print(f"Step {steps}:")
        print(f"Vacuum in Room {location}, Room A: {state['A']}, Room B: {state['B']}")
        
        if state[location] == 'dirty':
            print(f"Cleaning Room {location}")
            state[location] = 'clean'
        else:
            location = 'B' if location == 'A' else 'A'
            print(f"Moving to Room {location}")
        
        steps += 1

    print("\nAll rooms are clean.")

vacuum_world()
