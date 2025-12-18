import os
from collections import deque
from aegis.core.modes import Mode

class Context:
    def __init__(self,mode:Mode):
        self.cwd = os.getcwd()
        self.mode = mode
        self.history = deque(maxlen=20)
        self.task = None

    def update_cwd(self):
        self.cwd = os.getcwd()

    def set_mode(self,mode:Mode):
        self.mode = mode

    def add_history(self,user_input:str):
        self.history.append(user_input)

    def set_task(self, task:str):
        self.task = task

    def snapshot(self)-> dict:
        return{
            "cwd":self.cwd,
            "mode":self.mode.value,
            "history":list(self.history),
            "task":self.task,
        }