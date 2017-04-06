planet_list = ['Mercury', 'Mars']
print(planet_list)

planet_list.append('Jupiter')
planet_list.append('Saturn')
print(planet_list)

planet_list.extend(['Uranus'])
planet_list.extend(['Neptune'])
print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print(planet_list)

planet_list.append('Pluto')
print(planet_list)

rocky_planets = []
rocky_planets = planet_list[0:4]
print(rocky_planets)

del planet_list[8]
print(planet_list)

missions = [('Cassini', 'Saturn'),
('Galileo', 'Jupiter'),
('Messenger', 'Mercury'),
('Pioneer', 'Venus'),
('Curiosity', 'Mars'),]

for planet in planet_list:
    for mission in missions:
        if planet is mission[1]:
            print('{0} was visited by {1}'.format(planet, mission[0]))
