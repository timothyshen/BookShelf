# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '06/05/2020 16:27'

from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.profile.role == 'Author')
