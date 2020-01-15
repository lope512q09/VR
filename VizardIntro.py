import viz
import vizshape


#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

viz.MainView.collision(viz.ON)

#Increase the Field of View
viz.MainWindow.fov(60)

piazza = viz.addChild('piazza.osgb')
plant = viz.addChild('plant.osgb')
plant.setPosition([4, 0, 6])