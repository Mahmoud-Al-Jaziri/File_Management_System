from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import File

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    roles = ['Assistant', 'Auditor', 'Supervisor', 'Manager']
    permissions = {
        'Assistant': ['add_uploadedfile', 'view_uploadedfile'],
        'Auditor': ['view_uploadedfile', 'change_uploadedfile'],
        'Supervisor': ['view_uploadedfile', 'change_uploadedfile'],
        'Manager': ['add_uploadedfile', 'view_uploadedfile', 'change_uploadedfile', 'delete_uploadedfile'],
    }
    
    for role in roles:
        group, created = Group.objects.get_or_create(name=role)
        if created:
            for perm in permissions[role]:
                content_type = ContentType.objects.get_for_model(File)
                permission = Permission.objects.get(codename=perm, content_type=content_type)
                group.permissions.add(permission)
