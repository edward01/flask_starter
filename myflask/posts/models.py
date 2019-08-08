# -*- coding: utf-8 -*-
"""Post models."""
import datetime as dt

from myflask.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)


class Post(SurrogatePK, Model):
    __tablename__ = "posts"
    body = Column(db.String(140))
    timestamp = Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="posts")

    def __init__(self, body, **kwargs):
        """Create instance."""
        db.Model.__init__(self, body=body, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<Post({body})>".format(body=self.body)
