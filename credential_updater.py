import aa_api
import sys
from aa_api import request_token
from requests.exceptions import HTTPError


class ValueNotFound(Exception):
    pass


class Credential:
    def __init__(self, base_url, credential_name, attribute_name, new_value, token):
        self.base_url = base_url
        self.credential_name = credential_name
        self.attribute_name = attribute_name
        self.new_value = new_value
        self.token = token
        self.credential_id = self.__get_credential_id__()
        self.credential = self.__get_credential__()
        self.attribute = self.__get_attribute__()
        self.attribute_value = self.__get_attribute_value__()

    def __get_credential_id__(self):
        response = aa_api.get_credential_list(self.base_url, self.token)
        for credential in response['list']:
            if str.lower(credential['name']) == str.lower(self.credential_name):
                return credential['id']
        raise ValueNotFound('Credential ' + self.credential_name + ' not found')

    def __get_credential__(self):
        return aa_api.get_credential(self.base_url, self.credential_id, self.token)

    def __get_attribute__(self):
        for attribute in self.credential['attributes']:
            if str.lower(attribute['name']) == str.lower(self.attribute_name):
                return attribute
        raise ValueNotFound("Attribute" + self.attribute_name + ' not found')

    def __get_attribute_value__(self):
        response = \
            aa_api.get_attribute_value(self.base_url, self.credential_id, self.attribute['id'], self.token)
        if response:
            return response['list'][0]
        else:
            raise ValueNotFound("Attribute value" + self.attribute_value + ' not found')

    def update_credential(self):
        return aa_api.update_credential(self.base_url, self.credential['id'], self.attribute_value['id'],
                                        self.attribute_value['version'], self.new_value, self.token)


def main():
    response = None
    # Add first word for password
    new_value = sys.argv[4]
    # Add a space and the word for each word after the first one
    for i in range(5, len(sys.argv)):
        new_value += ' ' + sys.argv[i]

    credential = Credential(sys.argv[1], sys.argv[2], sys.argv[3], new_value, request_token(sys.argv[1]))
    try:
        response = credential.update_credential()
        response.raise_for_status()
    except HTTPError:
        raise HTTPError(response.json())
    except Exception as err:
        raise err

    print("Credential attribute successfully updated.")


if __name__ == "__main__":
    main()
