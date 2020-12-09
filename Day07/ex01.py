import re
import collections

outers = collections.defaultdict(list)
inners = collections.defaultdict(list)
shiny_golds = set()


def find_colour(colour):
    for col in outers[colour]:
        shiny_golds.add(col)
        find_colour(col)


def bag_count(colour):
    res = 0
    for num, inner_bag in inners[colour]:
        res += num * (1 + bag_count(inner_bag))
    return res


with open('input07.txt', 'r') as file:
    data = file.read().split('\n')

for line in data:
    outer = line.split("bags contain")[0].strip()
    print(outer)
    inner_data = re.findall(r"(\d+) (\w+ \w+)", line)
    for count, inner in inner_data:
        print("Contains", count, inner, "bags.")
        outers[inner].append(outer)
        inners[outer].append((int(count), inner))

find_colour("shiny gold")
print("Answer:", len(shiny_golds))
print("Part 2: ", bag_count("shiny gold"))
