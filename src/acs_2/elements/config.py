from dotenv import load_dotenv
from pathlib import Path
import os

class Configs:
    def __init__(self) -> None:
        current_dir= Path(__file__).parent
        project_root= current_dir.parent.parent.parent

        self.dotenv_path= project_root / '.env'

        self._IS_MANAGER= None
        self.__DEVICE_TOKEN= None

        self.num_successes= 0
        self.num_errors= 0

    def token(self) -> str:
        return str(self.__DEVICE_TOKEN)

    def load(self) -> dict:
        try:
            #Load the venv data
            load_dotenv(dotenv_path=self.dotenv_path)

            #Load the venv elements
            if os.getenv('IS_MANAGER').lower()== "true":
                self._IS_MANAGER= True
            else:
                self._IS_MANAGER= False

            self.__DEVICE_TOKEN= str(os.getenv('DEVICE_TOKEN', None))

            #Let's count the errors and the successes of the venv loading
            num_successes= 0
            num_errors= 0

            self.check(self._IS_MANAGER)
            self.check(self.__DEVICE_TOKEN)

            num_successes= self.num_successes
            num_errors= self.num_errors

            self.num_successes= 0
            self.num_errors= 0

            return {
                "state": True,
                "succeses": num_successes,
                "errors": num_errors,
                "total": num_successes + num_errors
            }
        except Exception as e:
            return {
                "state": False,
                "error": e
            }

    def check(self, var):
        if var is not None:
            self.num_successes+= 1
            return True
        else:
            self.num_errors+= 1
            return False