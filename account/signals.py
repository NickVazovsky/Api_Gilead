# from .models import UserAccount, CodeForUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=UserAccount)
# def post_save_generator_code(sender, instance, created, *args, **kwargs):
#     if created:
#         CodeForUser.objects.create(user=instance)