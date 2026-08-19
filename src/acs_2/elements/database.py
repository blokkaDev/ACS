from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

class Database:
    def __init__(self) -> None:
        self.__engine: Engine | None = None

    def connect(self, load: dict) -> dict:
        try:
            url= f"postgresql+psycopg://{load.get("user", "user")}:{load.get("password", "password")}@{load.get("url", "localhost:5432/acs")}"

            self.__engine= create_engine(
                url=url,
                pool_pre_ping=True
            )

            test= self.test()
            test["message"]= "Database connected successfully!"

            return test
        except Exception as e:
            return {
                "state": False,
                "error": e
            }

    def test(self) -> dict:
        if not self.__engine:
            return {
                "state": False,
                "error": "Error running 'Database.test()' engine does not exist try running Database.connect({'user': 'user', 'password': 'password', 'url': 'localhost:5432/acs'})"
            }

        try:
            with self.__engine.connect() as connection:
                result= connection.execute(text("SELECT 1"))

                return {
                    "state": True,
                    "message": "Test successfully completed!",
                    "result": result.scalar(),
                    "successes": 1,
                    "total": 1
                }
        except Exception as e:
            return {
                "state": False,
                "error": e
            }