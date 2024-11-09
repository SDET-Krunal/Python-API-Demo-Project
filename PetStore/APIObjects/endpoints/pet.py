from PetStore.APIObjects import routes
from PetStore.APIObjects.baseAPI import ResponseObject

from PetStore.lib.constants.constant import Constants as Const


class PetEndpoints(object):
    """ Pets API Endpoint """

    def __init__(self, cls):
        self._cls = cls

    def find_pet_by_status(self, pet_status: str) -> ResponseObject:
        """
        Return list of pets as per given status

        :return list: list of pets
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.GET, routes.FIND_PET_BY_STATUS, params={'status': pet_status})

        return ResponseObject(response)

    def add_pet(self, pet_details: dict) -> ResponseObject:
        """
        Return added new pet details

        :return dict: new added pet details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.POST, routes.ADD_UPDATE_PET, json=pet_details)

        return ResponseObject(response)

    def update_pet(self, pet_details: dict) -> ResponseObject:
        """
        Return updated pet details

        :return dict: updated pet details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.PUT, routes.ADD_UPDATE_PET, json=pet_details)

        return ResponseObject(response)

    def delete_pet(self, pet_id: dict) -> ResponseObject:
        """
        Return deleted pet details

        :return dict: status code with type and message
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.DELETE, routes.DELETE_PET.format(pet_id))

        return ResponseObject(response)
