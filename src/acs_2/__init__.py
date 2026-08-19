from acs_2.elements.config import Configs
from acs_2.worker import Worker
from acs_2.elements.database import Database

import time

Configs= Configs()
Database= Database()

Worker= Worker()

def main() -> None:
    Configs.load()

    if check(data=Database.load(
            {
                "password": Configs.database_password(),
                "user": Configs._DATABASE_USER,
                "url": Configs._DATABASE_URL
            }
        )
    ):
        print("Database loaded")

        Database.test()
    else:
        print("Error loading the database")

    if not Configs._IS_MANAGER and Configs._IS_MANAGER!= None:
        Worker.setup(
            {
                "token": Configs.token(),
                "started": time.time(),
                "port": Configs._PORT
            }
        )
    
def check(data: dict) -> bool:
    if data.get("state", False) and not data.get("error", None):
        if data.get("succeses", None)== data.get("total", None):
            return True

    return False