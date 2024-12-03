"""
--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

"""


def solution_1():
    with open("input.txt", "r") as file:
        total_safe = 0
        for row in file.readlines():
            nums = [int(x) for x in row.split(" ")]
            safe = True
            prev = nums[0]
            direction = (nums[1] - prev) / max(abs(nums[1] - prev), 1)
            for i in range(1, len(nums)):
                prev = nums[i - 1]
                num = nums[i]
                if (num == prev) or (abs(num - prev) > 3):
                    safe = False
                    break

                if (num - prev) * direction < 0:
                    safe = False
                    break
            if safe:
                total_safe += 1
        print(total_safe)


def solution_2():
    with open("input.txt", "r") as file:
        total_safe = 0
        for row in file.readlines():
            nums = [int(x) for x in row.split(" ")]
            safe = True
            without_prev = False
            without_curr = False
            direction = (nums[1] - nums[0]) / max(abs(nums[1] - nums[0]), 1)
            save_prev = []
            i = 1

            while i < len(nums):
                prev = nums[i - 1]
                curr = nums[i]

                # errors
                if (
                    (curr == prev)
                    or (abs(curr - prev) > 3)
                    or ((curr - prev) * direction < 0)
                ):
                    if not without_prev:
                        without_prev = True
                        save_prev = [i - 1, nums.pop(i - 1)]
                        i -= 2
                    else:
                        if not without_curr:
                            without_curr = True
                            nums.insert(save_prev[0], save_prev[1])
                            i = save_prev[0] + 1
                            nums.pop(i)
                            i -= 1
                        else:
                            safe = False
                            break
                i += 1
            if safe:
                total_safe += 1

        print(total_safe)


solution_2()
##78 75 77 80 81 82
# 32 36 39 42 44 46 47 48
