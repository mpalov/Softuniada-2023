def find_pref(nums, old_p, new_p):
    for num in nums:
        if num == old_p:
            return old_p
        elif num == new_p:
            return new_p

    return -1


particles = int(input())

graph_p = {}
graph_e = {}

pairs_p = {}
pairs_e = {}

merged = [False] * particles

for i in range(particles):
    pref = [int(x) for x in input().split()]
    graph_p[i] = pref

for i in range(particles):
    pref = [int(x) for x in input().split()]
    graph_e[i] = pref

while len(pairs_p) < particles:
    p = -1

    for p in range(len(merged)):
        if not merged[p]:
            break

    if p < 0 or p >= particles:
        break

    e = graph_p[p].pop(0)

    if e not in pairs_e:
        pairs_p[p] = e
        pairs_e[e] = p
        merged[p] = True
    else:
        p_old = pairs_e[e]
        p_new = p
        pref = find_pref(graph_e[e], p_old, p_new)

        if pref == p_new:
            del pairs_p[pairs_e[e]]
            merged[pairs_e[e]] = False
            pairs_e[e] = p
            pairs_p[p] = e
            merged[p] = True

for i in range(particles):
    print(f"{i} <-> {pairs_p.get(i)}")
