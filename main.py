from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, Vec4
from panda3d.core import WindowProperties
from direct.gui.OnscreenText import OnscreenText
import random


class DemoGame(ShowBase):
    def __init__(self):
        super().__init__()

        # Window title
        props = WindowProperties()
        props.setTitle("Panda3D Demo Game - Python 3D Project")
        self.win.requestProperties(props)

        # Disable default mouse camera controls
        self.disableMouse()

        # Load a built-in Panda model
        self.player = self.loader.loadModel("models/panda")
        self.player.reparentTo(self.render)
        self.player.setScale(0.25)
        self.player.setPos(0, 0, 0)

        # Load floor
        self.floor = self.loader.loadModel("models/environment")
        self.floor.reparentTo(self.render)
        self.floor.setScale(0.25)
        self.floor.setPos(-8, 42, 0)

        # Load collectible
        self.collectible = self.loader.loadModel("models/smiley")
        self.collectible.reparentTo(self.render)
        self.collectible.setScale(0.8)
        self.collectible.setPos(5, 5, 1)

        # Create a way to keep track of the score
        self.score = 0

        self.score_text = OnscreenText(
            text="Score: 0",
            pos=(-1.15, 0.9),
            scale=0.07,
            fg=(1, 1, 1, 1),
            mayChange=True
        )

        # Camera setup
        self.camera.setPos(0, -20, 6)
        self.camera.lookAt(self.player)

        # Lighting
        ambient = AmbientLight("ambient")
        ambient.setColor(Vec4(0.4, 0.4, 0.4, 1))
        self.render.setLight(self.render.attachNewNode(ambient))

        directional = DirectionalLight("directional")
        directional.setColor(Vec4(0.9, 0.9, 0.9, 1))
        light_node = self.render.attachNewNode(directional)
        light_node.setHpr(0, -60, 0)
        self.render.setLight(light_node)

        # Keyboard tracking
        self.keys = {
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }

        self.accept("arrow_left", self.set_key, ["left", True])
        self.accept("arrow_left-up", self.set_key, ["left", False])

        self.accept("arrow_right", self.set_key, ["right", True])
        self.accept("arrow_right-up", self.set_key, ["right", False])

        self.accept("arrow_up", self.set_key, ["up", True])
        self.accept("arrow_up-up", self.set_key, ["up", False])

        self.accept("arrow_down", self.set_key, ["down", True])
        self.accept("arrow_down-up", self.set_key, ["down", False])

        self.accept("escape", exit)

        # Update loop
        self.taskMgr.add(self.update, "update")

    def get_x_bound_for_y(self, y):
        min_y = -10
        max_y = 10

        min_x_bound = 4    # narrower when closer to camera
        max_x_bound = 10   # wider when farther away

        # Clamp y so it stays inside the expected range
        y = max(min_y, min(max_y, y))

        # Convert y into a percentage
        percent = (y - min_y) / (max_y - min_y)

        # Interpolate between the narrow and wide bounds
        return min_x_bound + percent * (max_x_bound - min_x_bound)

    def move_collectible_randomly(self):
            random_x = random.uniform(-6, 6)
            random_y = random.uniform(-10, 10)
            self.collectible.setPos(random_x, random_y, 1)


    def set_key(self, key, value):
        self.keys[key] = value

    def update(self, task):
        speed = 8
        dt = globalClock.getDt()
        distance = self.player.getDistance(self.collectible)

        if self.keys["left"]:
            self.player.setX(self.player.getX() - speed * dt)
            self.player.setH(-90)

        if self.keys["right"]:
            self.player.setX(self.player.getX() + speed * dt)
            self.player.setH(90)

        if self.keys["up"]:
            self.player.setY(self.player.getY() + speed * dt)
            self.player.setH(180)

        if self.keys["down"]:
            self.player.setY(self.player.getY() - speed * dt)
            self.player.setH(0)

        y_bound_min = -10
        y_bound_max = 10

        current_y = self.player.getY()
        x_bound = self.get_x_bound_for_y(current_y)

        x = max(-x_bound, min(x_bound, self.player.getX()))
        y = max(y_bound_min, min(y_bound_max, self.player.getY()))

        self.player.setPos(x, y, self.player.getZ())

        if distance < 2:
            self.score += 1
            self.score_text.setText(f"Score: {self.score}")
            print("Collected!")
            self.move_collectible_randomly()

        return task.cont


game = DemoGame()
game.run()
