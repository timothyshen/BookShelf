#_*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '15/04/2020 22:21'


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user_id' : user.id,
        'token': token,
        'name' : user.username,
        'role': user.profile.role
    }
