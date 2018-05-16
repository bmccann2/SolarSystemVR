import viz
import vizact
import vizshape
import vizinfo
import viztracker


viz.setMultiSample(4)
viz.fov(60)
viztracker.go()

myTracker = viz.add('sensor.dls')

viztracker.get("movable").setPosition([0,-1.8,-1])

z_coordinates=[-1,-3,-5,-7,-12,-17,-53,-75,-400]
x_coordinates=[-5,0,5,10,17,30,50,80,-400]

MOVE_SPEED= 40
count=0
mode=0

mercuryTexture= viz.addTexture('Mercury.jpg')
mercury= vizshape.addSphere(radius=0.38, slices=20,stacks=20, pos=(0,0,0))
mercury.texture(mercuryTexture)
mercury.alpha(1.0)
mercury.addAction( vizact.spin(0,1,0,5) )

marsTexture= viz.addTexture('Mars.jpg')
mars= vizshape.addSphere(radius=0.53, slices=20,stacks=20, pos=(0,0,-1))
mars.texture(marsTexture)
mars.alpha(.9)
mars.addAction( vizact.spin(0,1,0,5) )

venusTexture= viz.addTexture('Venus.jpg')
venus= vizshape.addSphere(radius=0.95, slices=20,stacks=20, pos=(0,0,-2))
venus.texture(venusTexture)
venus.alpha(.8)
venus.addAction( vizact.spin(0,1,0,5) )

earthTexture= viz.addTexture('Earth.jpg')
earth= vizshape.addSphere(radius=1.0,slices=20,stacks=20, pos=(0,0,-4))
earth.texture(earthTexture)
earth.alpha(.8)
earth.addAction( vizact.spin(0,1,0,5) )

neptuneTexture= viz.addTexture('Neptune.jpg')
neptune= vizshape.addSphere(radius=3.8,slices=20,stacks=20, pos=(0,0,-4))
neptune.texture(neptuneTexture)
neptune.alpha(.8)
neptune.addAction( vizact.spin(0,1,0,5) )

uranusTexture= viz.addTexture('Uranus.jpg')
uranus= vizshape.addSphere(radius=4.00,slices=20,stacks=20, pos=(0,0,-8))
uranus.texture(uranusTexture)
uranus.alpha(.8)
uranus.addAction( vizact.spin(0,1,0,5) )

saturnRingTexture= viz.addTexture('Rings_2.png')
saturnRing= vizshape.addCircle(15, slices=20)
saturnRing.setEuler(90, 90, 0)
saturnRing.setPosition(0,0,-32)
saturnRing.alpha(.8)
saturnRing.texture(saturnRingTexture)
saturnTexture= viz.addTexture('Saturn.jpg')
saturn= vizshape.addSphere(radius=9.45,slices=20,stacks=20, pos=(0,0,-32))
saturn.texture(saturnTexture)
saturn.alpha(.8)
saturn.addAction( vizact.spin(0,1,0,5) )
saturnRing.addAction( vizact.spin(0,0,1,1) )

jupiterTexture= viz.addTexture('Jupiter_2.jpg')
jupiter= vizshape.addSphere(radius=11.2, slices=20, stacks=20, pos=(0,0,-43))
jupiter.texture(jupiterTexture)
jupiter.alpha(.8)
jupiter.addAction( vizact.spin(0,1,0,5) )


sunTexture= viz.addTexture('Sun_2.jpg')
sun= vizshape.addSphere(radius=173, slices=20, stacks=20, pos=(0,0,-40))
sun.texture(sunTexture)
sun.alpha(.8)
sun.addAction( vizact.spin(0,1,0,5) )

def updateView():
	if viz.key.isDown(viz.KEY_UP):
		viz.MainView.move([0,0,MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_DOWN):
		viz.MainView.move([0,0,-MOVE_SPEED*viz.elapsed()],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_LEFT):
		viz.MainView.move([-MOVE_SPEED*viz.elapsed(),0,0],viz.BODY_ORI)
	elif viz.key.isDown(viz.KEY_RIGHT):
		viz.MainView.move([MOVE_SPEED*viz.elapsed(),0,0],viz.BODY_ORI)
vizact.ontimer(0,updateView) 

def onButtonDown(e):
	if e.button is 0 and count>=0:
		count= count-1
		if count>0 and mode is 0:
			viz.MainView.setPosition([0,0,z_coordinates[count]])
			viz.MainView.setEuler([0,0,0])
		if count>0 and mode is 1:
			viz.MainView.setPosition([x_coordinates[count],-3,-30])
			viz.MainView.setEuler([0,0,0])
		if count<0:
			count=0
	
	elif e.button is 1:
		count= count+1
		if count<7 and mode is 0:
			viz.MainView.setPosition([0,0,z_coordinates[count]])
			viz.MainView.setEuler([0,0,0])
		if count<7 and mode is 1:
			viz.MainView.setPosition([x_coordinates[count],-3,-30])
			viz.MainView.setEuler([0,0,0])
		if count>7:
			count=7
		if count is 7:
			viz.MainView.setPosition([x_coordinates[count],-3,-30])
	
	elif e.button is 2:
		mode=0
		count=0
		viztracker.get("movable").setPosition([0,-1.8,-1])
		mercury.setPosition([0,0,0])
		mars.setPosition([0,0,-1])
		venus.setPosition([0,0,-2])
		earth.setPosition([0,0,-4])
		neptune.setPosition([0,0,-4])
		uranus.setPosition([0,0,8])
		saturnRing.setPosition([0,0,-32])
		saturn.setPosition([0,0,-32])
		jupiter.setPosition([0,0,-43])
		sun.setPosition([0,0,-43])
	
	elif e.button is 3:
		mode=1
		count=0
		viztracker.get("movable").setPosition([0,-1.8,-1])
		mercury.setPosition([-5,0,0])
		mars.setPosition([0,0,0])
		venus.setPosition([5,0,0])
		earth.setPosition([10,0,0])
		neptune.setPosition([17,0,0])
		uranus.setPosition([30,0,0])
		saturnRing.setPosition([50,0,1])
		saturn.setPosition([50,0,0])
		jupiter.setPosition([80,0,0])
		sun.setPosition([0,0,0])
vizact.ontimer(0,onButtonDown)		
#array controls (look up VizTracker)
#change of view (cross between version 1 and version 2)
