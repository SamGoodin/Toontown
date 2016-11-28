from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        if x == 1

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor = Actor()
        self.pandaActor.loadModel("models/panda-model")
        self.pandaActor.loadAnims({"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # set up the dictionary:
        self.keyz_dctn = {'front': 0, 'back': 0}
        # the events:
        self.accept('1', self.set_key, ['front', 1])
        self.accept('2', self.set_key, ['back', 1])

        self.accept('1-up', self.set_key, ['front', 0])
        self.accept('2-up', self.set_key, ['back', 0])
        # the handler and the key task:
        self.anim_contrl = self.pandaActor.getAnimControl("walk")
        self.taskMgr.add(self.key_press_play_task, "key_task")

    def key_press_play_task(self, task):
        if (self.keyz_dctn['front'] == 1):
            if (not self.anim_contrl.isPlaying()):
                print "PLAYING FORWARDS..."
                self.pandaActor.setPlayRate(1.0, "walk")
                self.pandaActor.play("walk")
                self.taskMgr.add(self.showAnimState, "anim_task")
        elif (self.keyz_dctn['back'] == 1):
            if (not self.anim_contrl.isPlaying()):
                print "PLAYING BACKWARDS..."
                self.pandaActor.setPlayRate(-1.0, "walk")
                self.pandaActor.play("walk")
                self.taskMgr.add(self.showAnimState, "anim_task")
        return task.cont

    def set_key(self, key, value):
        self.keyz_dctn[key] = value

    # When the animation stops playing, print a message:
    def showAnimState(self, task):
        if (not self.anim_contrl.isPlaying()):
            print "ANIMATION IS NOT PLAYING..."
            taskMgr.remove("anim_task")
        return task.cont


app = MyApp()
app.run()