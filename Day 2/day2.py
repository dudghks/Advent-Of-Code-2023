with open('input.txt') as file:
    lines = file.readlines()

# Parser
# args: game as a string
# returns: id, max number of cubes shown
def parse_game(game):
    game_split = game.split('; ')
    game_id = game_split[0][5:game_split[0].index(':')]
    game_split[0] = game_split[0][game_split[0].index(':') + 2:]
    cubes = {}
    for g in game_split:
        g = g.split(', ')
        for c in g:
            c = c.split(' ')
            if c[1] in cubes.keys():
                cubes[c[1]] = max(int(cubes[c[1]]), int(c[0]))
            else:
                cubes[c[1]] = c[0]
    out = (int(game_id), int(cubes.get('red')), int(cubes.get('green')), int(cubes.get('blue')))
    return out

sum = 0
for game in lines:
    result = parse_game(game[:-1])
    if result[1] <= 12 and result[2] <= 13 and result[3] <= 14:
        sum += result[0]
print(sum)

# Part 2:
sum = 0
for game in lines:
    result = parse_game(game[:-1])
    sum += result[1] * result[2] * result[3]
print(sum)