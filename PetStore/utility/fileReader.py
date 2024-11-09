import json
import logging
import os

from PetStore.lib.config.config import Config


def get_file_path(file_name: str) -> str:
    """
    Returns the path of given file name

    :param file_name: file name
    :return: file path
    :rtype: str
    """
    try:
        return os.path.join(Config.PROJECT_ROOT_DIR, os.path.join("test_data", file_name))
    except FileNotFoundError as e:
        logging.warning("Given file may not be exists. Exception is : {}".format(e))


def read_json_data_file(file_name: str) -> dict:
    """
    Returns data from given file name

    :param file_name: file to be read
    :return: data from given file
    :rtype: dict
    """
    try:
        file_path = get_file_path(file_name=file_name)

        with open(file=file_path) as file:
            json_data = json.load(file)

        return json_data
    except FileNotFoundError as e:
        logging.warning("Given file may not be exists. Exception is : {}".format(e))
