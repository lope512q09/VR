import viz
import vizshape


#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

viz.MainView.collision(viz.ON)
# viz.MainView.setPosition([12, 15, -20])
viz.MainView.setEuler([0, 0, 0])

#Increase the Field of View
viz.MainWindow.fov(60)

viz.MainView.move([0,0,-8])

piazza = viz.addChild('piazza.osgb')


piazza = viz.addChild('piazza.osgb')

for x in [-3, -1, 1, 3]:
    for z in [4, 2, 0, -2, -4]:
        plant = viz.addChild('plant.osgb',cache=viz.CACHE_CLONE)
        plant.setPosition([x,0,z])