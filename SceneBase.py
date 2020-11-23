class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("Überschreiben")

    def Update(self):
        print("Überschreiben")

    def Render(self, screen):
        print("Überschreiben")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
