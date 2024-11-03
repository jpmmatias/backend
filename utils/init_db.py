from config.database import Base, engine
from models.Todo import Todo


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Todo.metadata.create_all(bind=engine)