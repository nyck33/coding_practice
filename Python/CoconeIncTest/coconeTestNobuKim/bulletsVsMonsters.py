'''
Shots from (0,0) so divide into quadrants
ne = 1, nw = 2, sw = 3, se =4

'''
# imports
import copy
import numpy as np


def get_quadrant_stuff(stuff_arrs, pos='ne'):
    """
    ne includes origin,
    nw includes any on x-axis, ie. y=0
    return list of tuples for each quad
    """
    ne, nw, sw, se = [], [], [], []
    for thing in stuff_arrs:
        x = thing[0]
        y = thing[1]
        if x >= 0 and y >= 0:
            ne.append((x, y))
        elif x < 0 and y >= 0:
            nw.append((x, y))
        elif x < 0 and y < 0:
            sw.append((x, y))
        else:
            se.append((x, y))

    return ne, nw, sw, se

def delete_killed(curr_mon, monsters):
    new_monsters = []
    for mon in monsters:
        if mon is not curr_mon:
            new_monsters.append(mon)
    return new_monsters


def get_kills(monsters, shots):
    """
    shots extend beyond the coord given
    find which shots hit monsters in the quad
    corner: 2 monster on same line, closer monster takes hit
            2 shots could be on same line
    lay down shot line, eliminate the nearest monster
    return list of kills and list of remaining monsters
    """
    killed, remaining = [], []
    mon_slope, shot_slope = 0, 0
    # sort monsters from lower x and y to higher(further)
    mons_sorted = sorted(monsters, key=lambda x: np.abs(x[0]))
    shots_sorted = sorted(shots, key=lambda x: np.abs(x[0]))
    # get line of shots, compare to mons_sorted, sort into kills and alive
    for i in range(len(shots_sorted)):
        curr_shot = shots_sorted[i]
        shot_x, shot_y = curr_shot
        if shot_x > 0:
            shot_slope = shot_y / shot_x
        else:
            shot_slope = 0
        for j in range(len(mons_sorted)):
            curr_mon = mons_sorted[j]
            mon_x, mon_y = curr_mon
            if mon_x > 0:
                mon_slope = mon_y / mon_x
            else:
                mon_slope = 0
            if mon_slope == shot_slope:
                # kill but can only kill one
                killed.append(curr_mon)
                # todo: prevent double counting of kills delete curr_mon from list
                mons_sorted = delete_killed(curr_mon, mons_sorted)
                break
    # list of tuples of killed mons (x,y)
    return killed


def main(monsters, bullets):
    ne_mons, nw_mons, sw_mons, se_mons = get_quadrant_stuff(monsters)
    quad_mons = [ne_mons, nw_mons, sw_mons, se_mons]
    ne_shots, nw_shots, sw_shots, se_shots = get_quadrant_stuff(bullets)
    quad_shots = [ne_shots, nw_shots, sw_shots, se_shots]
    # list of lists of kills from each quadrant
    all_kills = []
    for i in range(len(quad_mons)):
        curr_mons = quad_mons[i]
        curr_shots = quad_shots[i]
        curr_kills = get_kills(curr_mons, curr_shots)
        if len(curr_kills) > 0:
            all_kills.append(curr_kills)

    # count kills
    if len(all_kills) <= 0:
        print("no monsters killed")
        return -1
    num_kills = 0
    for j in range(len(all_kills)):
        quad_kills = all_kills[j]
        num_kills += len(quad_kills)

    return num_kills

if __name__=="__main__":
    monsters = [[2, 3], [4, 5], [3, -3], [2, -4], [3, -6],
                [-3, -3], [-5, 0], [-4, 4]]
    bullets = [[4, 1], [4, 6], [1, -2], [-4, -4],
               [-3, 0], [-4, 4]]
    print(main(monsters, bullets))
    # 5
    monsters = [[-4, 4], [-2, 2], [6, 2], [0, -2]]
    bullets = [[3, 1], [-1, 1], [-1, 1], [0, -4], [2, -3]]
    print(main(monsters, bullets))

    # 4
    monsters = [[1, 2], [-2, -1], [1, -2], [3, -1]]
    bullets = [[1, 0], [2, 1]]
    print(main(monsters, bullets))
    # -1
