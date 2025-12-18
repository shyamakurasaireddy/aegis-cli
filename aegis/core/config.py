from pathlib import Path
import yaml

CONFIG_DIR = Path.home()/".config"/"aegis"
CONFIG_FILE = CONFIG_DIR/"config.yaml"

DEFAULT_CONFIG = {
    "mode":"learning"
}

class Config:
    def __init__(self):
        self.data = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        CONFIG_DIR.mkdir(parents=True,exist_ok=True)

        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE,"r") as f:
                    user_config = yaml.safe_load(f) or {}
                    self.data.update(user_config)
            except Exception:
                self.data = DEFAULT_CONFIG.clopy()
        else:
            self.save()

    def save(self):
        with open(CONFIG_FILE,"w") as f:
            yaml.safe_dump(self.data,f)

    def get(self, key,default=None):
        return self.data.get(key, default)
    
    def set(self, key, value):
        self.data[key] = value
        self.save()