def test_parse_line_to_machine():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected_button_sets = [
        (3,),
        (1, 3),
        (2,),
        (2, 3),
        (0, 2),
        (0, 1),
    ]

    _, button_sets = parse_line_to_machine_with_joltage(line)

    assert button_sets == expected_button_sets

def test_joltage_parsing():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected = [3, 5, 4, 7]

    desired_state, _ = parse_line_to_machine_with_joltage(line)

    assert desired_state == expected

def test_real_input():
    with open(r"c:/Projects/playground/aoc2025/10/input.txt", encoding='utf-8') as f:
        sum_of_min_presses = 0
        lines = f.readlines()

        lines = [line.strip() for line in lines if line.strip()]

        for line in lines:
            print(f"Processing line: {line}")
            desired_state, button_tuples = parse_line_to_machine_with_joltage(line)
            min_presses = min_button_presses(desired_state, button_tuples)
            print(f"{line}\n  min button presses: {min_presses}")
            sum_of_min_presses += min_presses
        print(f"Sum of min button presses: {sum_of_min_presses}")

def parse_line_to_machine_with_joltage(line):
    parts = line.split(" ")
    button_sets_strs = parts[1:-1]
    desired_state_str = parts[-1]

    desired_state = desired_state_str[1:-1].split(",")
    desired_state = [int(x) for x in desired_state]

    button_sets = []
    for button_set_str in button_sets_strs:
        button_set_str = button_set_str[1:-1]
        button_indices = button_set_str.split(",")
        button_indices = [int(x) for x in button_indices]
        button_sets.append(button_indices)

    button_tuples = [tuple(bs) for bs in button_sets]

    return desired_state, button_tuples


# --- SOLVER IMPLEMENTATION ---
def min_button_presses(desired_state, button_tuples):
    """
    Given a desired_state (list of ints) and button_tuples (list of tuples of indices),
    return the minimum total number of button presses to reach the state from zero.
    Each button can be pressed any number of times (>=0).
    """
    import numpy as np
    try:
        from scipy.optimize import linprog
    except ImportError:
        linprog = None

    n_counters = len(desired_state)
    n_buttons = len(button_tuples)
    # Build matrix A: A[i][j] = 1 if button j increments counter i
    A = np.zeros((n_counters, n_buttons), dtype=int)
    for j, btn in enumerate(button_tuples):
        for i in btn:
            A[i, j] += 1
    b = np.array(desired_state)

    # Use integer linear programming if available
    if linprog is not None:
        # Relax to LP, then round up (since all coefficients are 1, this is often optimal)
        res = linprog(
            c=np.ones(n_buttons),
            A_eq=A,
            b_eq=b,
            bounds=[(0, None)] * n_buttons,
            method="highs",
        )
        if res.success:
            # If solution is already integer and valid, return it
            x = res.x
            if np.allclose(x, np.round(x)) and np.all(A @ np.round(x).astype(int) == b):
                return int(np.round(x).sum())
            # Try rounding up to nearest integer and check if it works
            x_up = np.ceil(x).astype(int)
            if np.all(A @ x_up == b):
                return int(x_up.sum())
    # Try integer programming with PuLP
    try:
        import pulp
        prob = pulp.LpProblem("MinButtonPresses", pulp.LpMinimize)
        x_vars = [pulp.LpVariable(f"x{i}", lowBound=0, cat=pulp.LpInteger) for i in range(n_buttons)]
        # Objective: minimize total presses
        prob += pulp.lpSum(x_vars)
        # Constraints: for each counter, sum of button effects == desired value
        for i in range(n_counters):
            prob += pulp.lpSum(A[i, j] * x_vars[j] for j in range(n_buttons)) == b[i]
        prob.solve(pulp.PULP_CBC_CMD(msg=0))
        if prob.status == pulp.LpStatusOptimal:
            x_sol = [int(pulp.value(var)) for var in x_vars]
            if np.all(A @ np.array(x_sol) == b):
                return int(sum(x_sol))
    except ImportError:
        pass

    # Brute-force for small button sets (n_buttons <= 7), no timeout
    from itertools import product
    min_presses = None
    max_presses = sum(desired_state) + 1
    for presses in product(range(max_presses), repeat=n_buttons):
        v = np.zeros(n_counters, dtype=int)
        for j, count in enumerate(presses):
            for i in button_tuples[j]:
                v[i] += count
        if np.all(v == b):
            total = sum(presses)
            if (min_presses is None) or (total < min_presses):
                min_presses = total
    if min_presses is not None:
        return min_presses
    raise ValueError("No solution found")


# --- TESTS FOR SOLVER ---
def test_min_button_presses_samples():
    import timeit
    # Sample 1
    line1 = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    desired1, buttons1 = parse_line_to_machine_with_joltage(line1)
    t_sample1 = timeit.timeit(lambda: min_button_presses(desired1, buttons1), number=1)
    result1 = min_button_presses(desired1, buttons1)
    print(f"Sample 1: {result1} (expected 10), time: {t_sample1:.4f}s")
    assert result1 == 10

    # Sample 2
    line2 = "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
    desired2, buttons2 = parse_line_to_machine_with_joltage(line2)
    t_sample2 = timeit.timeit(lambda: min_button_presses(desired2, buttons2), number=1)
    result2 = min_button_presses(desired2, buttons2)
    print(f"Sample 2: {result2} (expected 12), time: {t_sample2:.4f}s")
    assert result2 == 12

    # Sample 3
    line3 = "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    desired3, buttons3 = parse_line_to_machine_with_joltage(line3)
    t_sample3 = timeit.timeit(lambda: min_button_presses(desired3, buttons3), number=1)
    result3 = min_button_presses(desired3, buttons3)
    print(f"Sample 3: {result3} (expected 11), time: {t_sample3:.4f}s")
    assert result3 == 11
