from acs_2.elements.config import Configs
from acs_2.worker import Worker
import time

Configs= Configs()

Worker= Worker()

def main() -> None:
    print("Hello from acs-2!")

    Configs.load()

    data= {
        "token": Configs.token(),
        "started": time.time()
    }

    if not Configs._IS_MANAGER and Configs._IS_MANAGER!= None:

        Worker.setup(data)
    
def check(data: dict) -> bool:
    if data.get("state", False) and not data.get("error", None):
        if data.get("succeses", None)== data.get("total", None):
            return True

    return False