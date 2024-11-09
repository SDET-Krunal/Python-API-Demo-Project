from PetStore.APIObjects.baseAPI import BaseApiObject
from PetStore.APIObjects.endpoints.pet import PetEndpoints
from PetStore.APIObjects.endpoints.store import StoreEndpoints
from PetStore.APIObjects.endpoints.user import UserEndpoints


class PetStoreAPI(BaseApiObject):
    """ LogX Fulfillment Service API Resources """

    def __init__(self):
        """ LogX Fulfillment Service API """
        super().__init__()

        self.pet = PetEndpoints(self)
        self.store = StoreEndpoints(self)
        self.user = UserEndpoints(self)
