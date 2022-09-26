# Самая далекая планета


def find_farthest_orbit(orb):
    sp = []
    for i in orb:
        sp.append(i[0] * i[1])
    ind = sp.index(max(sp))
    return orb[ind]
     
 
list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(list_of_orbits))
