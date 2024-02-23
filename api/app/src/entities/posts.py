import uuid
from datetime import datetime
class Post:
    def __init__(self, title, image, content):
        self.id = str(uuid.uuid4())
        self.title = title
        self.image = image
        self.content = content
        self.date = Date.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'content': self.content,
            'date' : self.date
        }
