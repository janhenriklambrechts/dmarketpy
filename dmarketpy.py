import requests
import json

key = ""
class API(object):

    def __init__(self, key=''):
        """
        Creates API object.
        :param key: str
        :returns: none
        """
        self.key = key
        self.url = "https://dmarket.com/"


    def load_key(self, path):
        """ Load key from file.
        Expected file format is key and secret on separate lines.
        :param path: path to keyfile
        :type path: str
        :return: None
        """
        with open(path, 'r') as f:
            self.key = f.readline().strip()
        return



    def public_query(self, urlpath,params=None,timeout=None):
        """
        performs a public query (no authorization required)
        :param urlpath:  API URL path without "https://dmarket.com/"
        :type urlpath: str
        :param params:params: API request parameters
        :type params: dict
        :param timeout:(optional) if not ``None``
        :return: response.text, JSON object
        """
        if params is None:
            params = {}

        return self.get_query(urlpath,params=params,timeout=timeout)

    def private_query(self, type, urlpath, json=None, params=None, timeout=None):
        """
         performs a public query (authorization required)
        :param type: either "GET" or "POST"
        :type type: str
        :param urlpath:  API URL path without "https://dmarket.com/"
        :param json: API request body
        :type json: dict
        :param params: params: API request parameters
        :type params: dict
        :param timeout: timeout: (optional) if not ``None``
        :return: response.txt, JSON object
        :raises Exception when API-key is not set
        """
        if json is None:
            json = {}
        if params is None:
            params={}

        if not self.key:
            raise Exception('API-key not set!')

        headers = {
            "authorization" : self.key
        }

        if type == "GET":
            return self.get_query(operation=urlpath,headers=headers,params=params,timeout=timeout)
        if type == "POST":
            return self.post_query(operation=urlpath,headers=headers,json=json,params=params,timeout=timeout)

    def get_query(self, operation, headers=None, params=None, timeout=None):
        """ GET-query handling

        --- use public_query() or private_query() unless you have a good reason not to ---

        :param operation: API URL path without "https://dmarket.com/"
        :type operation: str
        :param headers: (optional) HTTPS headers
        :type headers: dict
        :param params: API request parameters
        :type params: dict
        :param timeout: (optional) if not ``None``
        :returns: response.txt, JSON object
        :raises: :py:exc:`requests.HTTPError`: if response status not successful

        """
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        url = self.url + operation
        response = requests.get(url, headers=headers, params=params,
                                timeout=timeout)
        if response.status_code not in (200, 201, 202):
            response.raise_for_status()

        return response.text

    def post_query(self, operation, headers=None, json=None, params=None, timeout=None):
        """Post-query handling

        --- use public_query() or private_query() unless you have a good reason not to ---

        :param operation:
        :type operation: str
        :param headers:
        :type headers: dict
        :param json:  API request body
        :type json: dict
        :param params: API request parameters
        :type params: dict
        :param timeout: (optional) if not ``None``
        :return: respons.txt, JSON object
        :raises: py:exc:`requests.HTTPError`: if response status not successful
        """

        if json is None:
            json = {}

        if params is None:
            params = {}
        if headers is None:
            headers = {}

        url = self.url + operation

        response = requests.post(url, headers=headers, params=params, json=json,
                                 timeout=timeout)
        if response.status_code not in (200, 201, 202):
            response.raise_for_status()

        return response.text



