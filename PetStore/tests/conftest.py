import pytest

from PetStore.APIObjects.petStoreAPI import PetStoreAPI


@pytest.fixture()
def petstore_api() -> PetStoreAPI:
    """ API object """
    yield PetStoreAPI()
