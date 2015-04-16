from django.contrib.auth.models import User


# add test users
user = User.objects.create_user("ghitzarai", "some@email.com", "1234")
user.is_superuser = True
user.save()
user = User.objects.create_user("slippu", "some@email.com", "1234")
user.is_superuser = True
user.save()


#set initial data
print "Adding misc"
execfile("populate/misc.py")

print "Adding all skills"
execfile("populate/skills.py")
