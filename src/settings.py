from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import create_engine


class Settings():
    database_url: str = "postgresql://postgres:unity@localhost:5432/personal_local"

    def get_engine(self):
        try:
            assert self.database_url
            return create_engine(self.database_url)
        except AssertionError as a_error:
            print(a_error)
        return None

    @staticmethod
    def get_session(db_engine):
        return scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
        )


settings = Settings()
engine = settings.get_engine()
db_session = Settings.get_session(db_engine=engine)


def get_session():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
