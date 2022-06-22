from os import getenv

from office365.runtime.http.http_method import HttpMethod

TIMEOUT = int(getenv("TRUSTMI_OFFICE365_TIMEOUT", 60))


class RequestOptions(object):
    """Request options"""

    def __init__(self, url):
        """

        :type url: str
        """
        self.url = url
        self.data = None
        self.headers = {}
        self.auth = None
        self.method = HttpMethod.Get
        self.verify = True
        self.stream = False
        self.proxies = None
        self.timeout = TIMEOUT

    @property
    def is_file(self):
        return hasattr(self.data, 'read') and callable(self.data.read)

    @property
    def is_bytes(self):
        return hasattr(self.data, 'decode') and callable(self.data.decode)

    def set_header(self, name, value):
        self.headers[name] = value

    def ensure_header(self, name, value):
        if name not in self.headers:
            self.headers[name] = value
