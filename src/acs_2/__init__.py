from acs_2.elements.config import Configs
from acs_2.worker import Worker
from acs_2.elements.database import Database

import time

Configs= Configs()
Database= Database()

Worker= Worker()

def main() -> None:
    Configs.load()

    database_status= status(data=Database.connect(
            load={
                "password": Configs.database_password(),
                "user": Configs._DATABASE_USER,
                "url": Configs._DATABASE_URL
            }
        )
    )
    if database_status["status"]:
        print("Database loaded")
    
        print(status(Database.test())["message"])
    else:
        print(f"Error loading the database: {database_status["message"]}")

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
        if data.get("successes", 0)== data.get("total", 1):
            return True

    return False

def status(data: dict) -> dict:
    state= False
    success= False
    message= None
    error= None
    if data.get("state", False):
        state= True
        message= data.get("message", message)

    if data.get("successes", 0)== data.get("total", 1):
        success= True

    if data.get("error", False):
        state= False
        message= data.get("error", message)
        error= data.get("error", None)

    check_r= check(data=data)

    return {
        "more": {
            "state": state,
            "success": success
        },
        "status": success and state and not error and check_r,
        "check": check_r,
        "message": message
    }