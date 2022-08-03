from rest_framework import permissions

from .permissions import isStaffEditorPermission


class StaffEditorPermissionMixin():

    permission_classes = [permissions.IsAdminUser , isStaffEditorPermission]


class UserQuerysetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user

        qs = super().get_queryset(*args ,**kwargs)
        return qs.filter(**lookup_data)
