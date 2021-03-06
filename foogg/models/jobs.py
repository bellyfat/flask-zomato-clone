from datetime import datetime, timedelta
from foogg.extensions import db
from .users import Users


class History(db.EmbeddedDocument):
    status = db.StringField(default='new')
    made_at = db.DateTimeField(default=datetime.utcnow)


class Jobs(db.Document):
    title = db.StringField(max_length=75, required=True)
    priority = db.StringField(max_length=6, required=True)
    status = db.StringField(default='new')
    history = db.EmbeddedDocumentListField(History)
    created_on = db.DateTimeField(default=datetime.utcnow)
    created_by = db.ReferenceField(Users)
    valet = db.ReferenceField(Users)

    meta = {
        'indexes': ['priority', 'created_on']
    }
