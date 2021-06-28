"""
x
y
r
d
target
result
x = -1
y = 2
r = 2
d = 60
target = [[0, 1], [-1, 1], [1, 0], [-2, 2]]
res: 2

"""
import math
import numpy as np

def attack_circle_sector(x,y,r,d,targets):
    x = float(x)
    y = float(y)
    # makes a bigger circle from origin but angles same
    radius = math.sqrt(x**2 + y**2)
    # calc angle
    theta = np.arctan2(np.array([y]), np.array([x]))[0]
    # convert from radian to degree
    start_angle = 180 * theta/np.pi

    # now get the two end angles
    endAngleA = start_angle - d
    endAngleB = start_angle + d
    # get percentage
    #total_sector_angle = abs(endAngleB - endAngleA)
    #sector_percent = total_sector_angle / 360
    # iterate targets and if endB >= theta >= endA and
    # radius <= r, it is hit
    killed = []
    for monster in targets:
        mon_x, mon_y = monster
        mon_x = np.array([float(mon_x)])
        mon_y = np.array([float(mon_y)])
        mon_radius = (math.sqrt(mon_x**2 + mon_y**2))
        mon_theta = (np.arctan2(mon_y, mon_x) * (180/np.pi))[0]
        if (endAngleB >= mon_theta >= endAngleA) and (mon_radius <= r):
            killed.append((mon_x, mon_y))

    print(killed)
    return len(killed)


if __name__=="__main__":
    x = -1
    y = 2
    r = 2
    d = 60
    targets = [[0, 1], [-1, 1], [1, 0], [-2, 2]]
    print(attack_circle_sector(x,y,r,d,targets))