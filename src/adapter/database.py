from src.infra.database.dynamodb import Dynamodb
from src.infra.database.mysql import MySQL


class DatabaseFactory:
    @staticmethod
    def create_database_gpt(db_type: str = "dynamodb"):
        if db_type == "dynamodb":
            return Dynamodb()
        else:
            raise ValueError(f"Unknown database type: {db_type}")

    @staticmethod
    def create_database_brickas(db_type: str = "mysql"):
        if db_type == "mysql":
            return MySQL()
        else:
            raise ValueError(f"Unknown database type: {db_type}")
