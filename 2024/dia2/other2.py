def aoc02():
    def ok(r):
        return sorted(r) in [r, r[::-1]] and all(
            1 <= abs(i - j) <= 3 for i, j in zip(r, r[1:])
        )

    def ok2(r):
        return any(ok(r[:i] + r[i + 1 :]) for i in range(len(r)))

    # print(sum(ok([int(x) for x in r.split()]) for r in open("input.txt")))
    print(sum(ok2([int(x) for x in r.split()]) for r in open("input.txt")))


aoc02()
