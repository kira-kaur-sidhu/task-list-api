from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)

    def to_dict(self):
        if self.completed_at is None:
            completed = False
        else:
            completed = True
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": completed
        }

    @classmethod
    def from_dict(cls, task_data):
        return cls(
            title = task_data["title"],
            description = task_data["description"],
            completed_at = task_data["completed_at"] if "completed_at" in task_data else None
        )