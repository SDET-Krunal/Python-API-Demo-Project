from PetStore.APIObjects import routes
from PetStore.APIObjects.baseAPI import ResponseObject

from PetStore.lib.constants.constant import Constants as Const


class UserEndpoints(object):
    """ User API Endpoint """

    def __init__(self, cls):
        self._cls = cls

    def get_user(self, user_name: str) -> ResponseObject:
        """
        Return user details of given user's name

        :return dict: user details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.GET, routes.GET_UPDATE_DELETE_USER.format(user_name))

        return ResponseObject(response)

    def create_user(self, user_details: str) -> ResponseObject:
        """
        Return created new user details

        :return dict: user details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.POST, routes.CREATE_USER, json=user_details)

        return ResponseObject(response)

    def update_user(self, user_name: str, user_details: dict) -> ResponseObject:
        """
        Return updated user details

        :return dict: user details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.PUT, routes.GET_UPDATE_DELETE_USER.format(user_name),
                                     json=user_details)

        return ResponseObject(response)

    def delete_user(self, user_name: str) -> ResponseObject:
        """
        Return deleted user details

        :return dict: user details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.DELETE, routes.GET_UPDATE_DELETE_USER.format(user_name))

        return ResponseObject(response)
