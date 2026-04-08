def min_wear_cost(L, W, targets, D):
    L1, L2, L3 = L
    current = (0, 0, 0)
    total_cost = 0

    for T in targets:
        best_cost = float('inf')
        best_state = None

        # Only loop i and o
        for i in range(L1 + 1):
            for o in range(L3 + 1):

                # constraint: difference
                if abs(i - o) > D:
                    continue

                m = T - i - o

                # check middle valid
                if 0 <= m <= L2:

                    cost = (
                        abs(i - current[0]) * W[0] +
                        abs(m - current[1]) * W[1] +
                        abs(o - current[2]) * W[2]
                    )

                    if cost < best_cost:
                        best_cost = cost
                        best_state = (i, m, o)

        total_cost += best_cost
        current = best_state

    return total_cost


# Test
Limits = [10, 10, 10]
Wear = [1, 3, 5]
Targets = [15, 8]
D = 4

print(min_wear_cost(Limits, Wear, Targets, D))