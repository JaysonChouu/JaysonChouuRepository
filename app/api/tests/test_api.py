import os

from django.conf import settings

from ..models import (Role, RoleMapping)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def create_default_roles():
    Role.objects.get_or_create(name=settings.ROLE_PROJECT_ADMIN)
    Role.objects.get_or_create(name=settings.ROLE_ANNOTATOR)
    Role.objects.get_or_create(name=settings.ROLE_ANNOTATION_APPROVER)


def assign_user_to_role(project_member, project, role_name):
    role, _ = Role.objects.get_or_create(name=role_name)
    if RoleMapping.objects.filter(user=project_member, project=project).exists():
        mapping = RoleMapping.objects.get(user=project_member, project=project)
        mapping.role = role
        mapping.save()
    else:
        mapping = RoleMapping.objects.get_or_create(role_id=role.id, user_id=project_member.id, project_id=project.id)
    return mapping


def remove_all_role_mappings():
    RoleMapping.objects.all().delete()


class TestUtilsMixin:
    def _patch_project(self, project, attribute, value):
        old_value = getattr(project, attribute, None)
        setattr(project, attribute, value)
        project.save()

        def cleanup_project():
            setattr(project, attribute, old_value)
            project.save()

        self.addCleanup(cleanup_project)


