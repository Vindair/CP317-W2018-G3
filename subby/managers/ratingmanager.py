from django.db import models
from django.conf import settings

class RatingManager(models.Manager):
    use_in_migrations = True

    def create_rating(self, rating_number, comment, user_id, reviewed_user_id):
        r = self.model()

        if not r.validate_rating(rating_number):
            raise ValueError('Rating is not valid rating number')

        r.set_rating(rating_number)
        r.set_comment(comment)
        r.set_user_id(user_id)
        r.set_reviewed_user_id(reviewed_user_id)
        r.save()
        return r
