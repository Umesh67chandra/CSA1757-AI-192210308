import itertools

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in itertools.permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm

        if s == 0 or m == 0:
            continue

        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

        if send + more == money:
            return f"SEND = {send}, MORE = {more}, MONEY = {money}"

    return "No solution found."

solution = solve_cryptarithmetic()
print(solution)
