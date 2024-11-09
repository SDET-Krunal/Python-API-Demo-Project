from http import HTTPStatus

import pytest

from PetStore.lib.constants.APIResponseMessage import ErrorResponseMessage
from PetStore.utility.fileReader import read_json_data_file


@pytest.mark.usefixtures("petstore_api")
class TestUserAPIEndpoint:
    """ Tests for User API Endpoint """

    def test_create_users(self, petstore_api):
        """
        Scenario Tested:
            [x] Verify user is created successfully.
        """
        user_details_payload = read_json_data_file(file_name="create_user.json")
        response = petstore_api.user.create_user(user_details=user_details_payload)

        assert response["code"] == HTTPStatus.OK
        assert response["type"] == "unknown"
        assert response["message"] == str(user_details_payload["id"])

    @pytest.mark.parametrize("user_name", ["krunal.panchal.31"])
    def test_get_user_details(self, petstore_api, user_name):
        """
        Scenario Tested:
            [x] Verify correct user details is coming for given user's name.
        """
        response = petstore_api.user.get_user(user_name=user_name)
        expected_user_details = read_json_data_file(file_name="create_user.json")

        assert response["id"] == expected_user_details["id"]
        assert response["username"] == expected_user_details["username"]
        assert response["firstName"] == expected_user_details["firstName"]
        assert response["lastName"] == expected_user_details["lastName"]
        assert response["email"] == expected_user_details["email"]
        assert response["password"] == expected_user_details["password"]
        assert response["phone"] == expected_user_details["phone"]
        assert response["userStatus"] == expected_user_details["userStatus"]

    @pytest.mark.parametrize("user_name", ["krunal.panchal"])
    def test_get_invalid_user_details(self, petstore_api, user_name):
        """
        Scenario Tested:
            [x] Verify error message while fetching invalid user details.
        """
        response = petstore_api.user.get_user(user_name=user_name)

        assert response["code"] == 1
        assert response["type"] == "error"
        assert response["message"] == ErrorResponseMessage.USER_NOT_FOUND

    @pytest.mark.parametrize("user_name", ["krunal.panchal.31"])
    def test_update_user_details(self, petstore_api, user_name):
        """
        Scenario Tested:
            [x] Verify user details is getting updated successfully.
        """
        user_details_payload = read_json_data_file(file_name="update_user.json")
        response = petstore_api.user.update_user(user_name=user_name, user_details=user_details_payload)

        assert response["code"] == HTTPStatus.OK
        assert response["type"] == "unknown"
        assert response["message"] == str(user_details_payload["id"])

    @pytest.mark.parametrize("user_name", ["krunal.panchal.31"])
    def test_delete_user_details(self, petstore_api, user_name):
        """
        Scenario Tested:
            [x] Verify user details is getting deleted successfully.
        """
        response = petstore_api.user.delete_user(user_name=user_name)

        assert response["code"] == HTTPStatus.OK
        assert response["type"] == "unknown"
        assert response["message"] == user_name
