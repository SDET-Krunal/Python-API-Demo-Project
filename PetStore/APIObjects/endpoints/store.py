from PetStore.APIObjects import routes
from PetStore.APIObjects.baseAPI import ResponseObject

from PetStore.lib.constants.constant import Constants as Const


class StoreEndpoints(object):
    """ Store API Endpoint """

    def __init__(self, cls):
        self._cls = cls

    def get_order(self, order_id: str) -> ResponseObject:
        """
        Return order details

        :return dict: order details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.GET, routes.GET_DELETE_ORDER.format(order_id))

        return ResponseObject(response)

    def place_an_order(self, order_details: dict) -> ResponseObject:
        """
        Return placed order details

        :return dict: order details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.POST, routes.PLACE_ORDER, json=order_details)

        return ResponseObject(response)

    def get_inventory(self) -> ResponseObject:
        """
        Return list of all order details

        :return list: order details
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.GET, routes.GET_INVENTORY)

        return ResponseObject(response)

    def delete_order(self, order_id: str) -> ResponseObject:
        """
        Return deleted order details

        :return dict: status code with type and message
        :rtype: ResponseObject
        """
        response = self._cls.request(Const.HTTPMethods.DELETE, routes.GET_DELETE_ORDER.format(order_id))

        return ResponseObject(response)
