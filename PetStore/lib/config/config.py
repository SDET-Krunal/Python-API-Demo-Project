import os


class Config(object):
    """ Configuration variables related to automation framework """

    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
