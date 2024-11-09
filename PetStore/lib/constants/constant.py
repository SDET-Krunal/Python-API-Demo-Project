class Constants:
    """ Common application constants """
    DEFAULT_BASE_API_URL = "https://petstore.swagger.io"
    ADMIN_USER_NAME = ""
    ADMIN_PASSWORD = ""
    DEFAULT_TIMEOUT = 30

    class HTTPMethods:
        """ HTTP Methods """
        GET = 'get'
        POST = 'post'
        PUT = 'put'
        DELETE = 'delete'
        VALID_METHODS = [GET, POST, PUT, DELETE]
