class Post:
    def __init__(self, id, title, img, user, content):
        self.id = id
        self.title = title
        self.img = img
        self.user = user
        self.content = content

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'img': self.img,
            'user': self.user,
            'content': self.content
        }
