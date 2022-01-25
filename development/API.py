from development.Database.SQLLite import session_factory, Base
from pathlib import Path
import sqlalchemy

name = sqlalchemy.create_engine("sqlite:///instance/pdfextractor.db")
_SessionFactory = sqlalchemy.orm.sessionmaker(bind=name)

Base = sqlalchemy.ext.declarative.declarative_base()

def session_factory():
    Base.metadata.create_all(name)
    return _SessionFactory()


class API(Base):
    __tablename__ = "file"

    def extract_and_persist(self, filename: Path):
        object_id = self._persist()
        process = self._async_extract_and_persist(filename, object_id)
        process.start()

    def _persist(
            self,
            date: str = None,
            author: str = None,
            creator: str = None,
            producer: str = None,
            subject: str = None,
            title: str = None,
            number_of_pages: int = None,
            raw_info: str = None,
            content: str = None,
            object_id: int = None,
    ):
        """Private method to persist/update the object in the database"""
        session = session_factory()
        if object_id is None:
            self.status = "EN COURS"
            self.date = str(date)
            self.author = str(author)
            self.creator = str(creator)
            self.producer = str(producer)
            self.subject = str(subject)
            self.title = str(title)
            self.number_of_pages = number_of_pages
            self.raw_info = str(raw_info)
            self.content = str(content)
            session.add(self)
        else:
            article_model = session.query(API).get(object_id)
            article_model.status = "REUSSI"
            article_model.date = str(date)
            article_model.author = str(author)
            article_model.creator = str(creator)
            article_model.producer = str(producer)
            article_model.subject = str(subject)
            article_model.title = str(title)
            article_model.number_of_pages = number_of_pages
            article_model.raw_info = str(raw_info)
            article_model.content = str(content)

        session.commit()
        self.internal_id = self.id
        session.close()

        return self.internal_id
