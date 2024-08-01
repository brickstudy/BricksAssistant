from src.infra.database.dynamodb import Dynamodb


class DatabaseFactory:
    @staticmethod
    def create_database_gpt(db_type: str = "dynamodb"):
        if db_type == "dynamodb":
            return Dynamodb()
        else:
            raise ValueError(f"Unknown database type: {db_type}")
