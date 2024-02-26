from datetime import datetime
from app.src.dao.post_dao import get_new_board_index

class Post:
    def __init__(self, title, image, content,board):
        self.id = get_new_board_index(board)
        self.title = title
        self.image = image
        self.content = content
        self.date = datetime.now().timestamp()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'content': self.content,
            'date' : self.date
        }
 
