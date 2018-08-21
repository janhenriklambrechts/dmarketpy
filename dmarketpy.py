import requests
import json
import ast

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
        :return: API-response, dict
        """
        if params is None:
            params = {}

        return self.encoder(self.get_query(urlpath=urlpath,params=params,timeout=timeout))

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
        :return: API-response, dict
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
            return self.encoder(self.get_query(urlpath=urlpath,headers=headers,params=params,timeout=timeout))
        if type == "POST":
            return self.encoder(self.post_query(urlpath=urlpath,headers=headers,json=json))

    def get_query(self, urlpath, headers=None, params=None, timeout=None):
        """ GET-query handling

        --- use public_query() or private_query() unless you have a good reason not to ---

        :param urlpath: API URL path without "https://dmarket.com/"
        :type urlpath: str
        :param headers: (optional) HTTPS headers
        :type headers: dict
        :param params: API request parameters
        :type params: dict
        :param timeout: (optional) if not ``None``
        :returns: API response, str
        :raises: :py:exc:`requests.HTTPError`: if response status not successful

        """
        if params is None:
            params = {}
        if headers is None:
            headers = {}

        url = self.url + urlpath
        response = requests.get(url, headers=headers, params=params,
                                timeout=timeout)
        if response.status_code not in (200, 201, 202):
            response.raise_for_status()

        return response.text

    def post_query(self, urlpath, headers=None, json=None, params=None, timeout=None):
        """Post-query handling

        --- use public_query() or private_query() unless you have a good reason not to ---

        :param urlpath:
        :type urlpath: str
        :param headers:
        :type headers: dict
        :param json:  API request body
        :type json: dict
        :param params: API request parameters
        :type params: dict
        :param timeout: (optional) if not ``None``
        :return: API-response, str
        :raises: py:exc:`requests.HTTPError`: if response status not successful
        """

        if json is None:
            json = {}

        if params is None:
            params = {}
        if headers is None:
            headers = {}

        url = self.url + urlpath
        print(url)
        print(headers)
        print(json)

        response = requests.post(url=url, headers=headers, params=params, json=json, timeout=timeout)
        if response.status_code not in (200, 201, 202):
            response.raise_for_status()

        return response.text

    def encoder(self,json_data):
        """
        Modifies the JSON-string for dict modification
        :param json_data: string in JSON form
        :return: dict
        """
        json_data= json_data.replace("false","False")
        json_data= json_data.replace("true","True")
        return ast.literal_eval(json_data)