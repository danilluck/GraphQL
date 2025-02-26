from .model import Note
from configs import db

class NoteRepository:

    @staticmethod
    async def create(note_data:Note):
        async with db as session:
            async with session.begin():
                session.add(note_data)

            db.commit_rollback()