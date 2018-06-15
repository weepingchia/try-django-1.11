from django.contrib.auth import get_user_model

User = get_user_model()

test_ = User.objects.last()

# my followers associate to my profile; who's following me
test_.profile.followers.all()

# who i follow as reverse relationship as i'm the follower
test_.is_following.all() # == test_.profile.following.all()

