import pygal 

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca':341260000, 'us': 30093490000, 'mx': 1134230000})

wm.render_to_file('na_populations.svg')