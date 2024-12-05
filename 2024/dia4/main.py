def solution1():
    with open("input.txt") as file:
        data = file.readlines()

    total_sum = 0
    for i in range(0, len(data)):
        row = data[i].strip()
        for j in range(0, len(row)):
            char = row[j]

            if char != "X":
                continue

            adjacent_words = []

            # check right
            if j < len(row) - 3:
                adjacent_words.append(row[j + 1] + row[j + 2] + row[j + 3])

            # check down right
            if (j < len(row) - 3) and (i < len(data) - 3):
                adjacent_words.append(
                    data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
                )

            # check down
            if i < len(data) - 3:
                adjacent_words.append(data[i + 1][j] + data[i + 2][j] + data[i + 3][j])

            # check down left
            if j > 2 and i < len(data) - 3:
                adjacent_words.append(
                    data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
                )

            # check left
            if j > 2:
                adjacent_words.append(row[j - 1] + row[j - 2] + row[j - 3])

            # check left up
            if j > 2 and i > 2:
                adjacent_words.append(
                    data[i - 1][j - 1] + data[i - 2][j - 2] + data[i - 3][j - 3]
                )

            # check up
            if i > 2:
                adjacent_words.append(data[i - 1][j] + data[i - 2][j] + data[i - 3][j])

            # check right up
            if j < len(row) - 3 and i > 2:
                adjacent_words.append(
                    data[i - 1][j + 1] + data[i - 2][j + 2] + data[i - 3][j + 3]
                )

            total_sum += sum(
                [True if word == "MAS" else False for word in adjacent_words]
            )
    print(total_sum)


def solution2():
    with open("input.txt") as file:
        data = file.readlines()

    total_sum = 0

    for i in range(1, len(data) - 1):
        row = data[i].strip()
        for j in range(1, len(row) - 1):
            if data[i][j] != "A":
                continue

            word = (
                data[i - 1][j - 1]
                + data[i - 1][j + 1]
                + data[i + 1][j + 1]
                + data[i + 1][j - 1]
            )

            adjacent_words = []
            for offset in range(len(word)):
                new_word = ""
                for char in range(len(word)):
                    new_word += word[(offset + char) % len(word)]
                adjacent_words.append(new_word)

            total_sum += (
                1
                if any([True if word == "MMSS" else False for word in adjacent_words])
                else 0
            )
    print(total_sum)


solution2()
