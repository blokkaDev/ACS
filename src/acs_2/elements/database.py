from sqlalchemy import create_engine, text

class Database:
    def __init__(self):
        self._engine= None

    def load(self, data):
        try:
            url= f"postgresql+psycopg://{data.get("user", "user")}:{data.get("password", "password")}@{data.get("url", "url")}"

            self._engine= create_engine(
                url=url,
                pool_pre_ping=True
            )

            return {
                "state": True,
                "succeses": 1,
                "total": 1
            }
        except create_engine.sqlalchemy.exc.NoSuchModuleError as e:
            return {
                "state": False,
                "error": e
            }

    def test(self):
        with self._engine.connect() as connection:
            result= connection.execute(text("SELECT 1"))
            print(result.scalar())
