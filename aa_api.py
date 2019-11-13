import requests
import json
from credentials import username, password
from requests.exceptions import HTTPError


def request_token(base_url):
    response = None
    try:
        response = requests.post(base_url + 'v1/authentication',
                                 data=json.dumps({'Username': username, 'Password': password}))
        response.raise_for_status()
    except HTTPError:
        raise HTTPError(response.json())
    except Exception as err:
        raise err

    return response.json()['token']


def get_credential_list(base_url, token):
    url = base_url + 'v2/credentialvault/credentials/list'
    headers = {'Content-Type': 'application/json', 'X-Authorization': token}
    data = json.dumps({
        "page": {
            "offset": 0,
            "length": 0
        }
    })

    return requests.post(url, headers=headers, data=data).json()


def get_credential(base_url, credential_id, token):
    url = base_url + 'v2/credentialvault/credentials/' + credential_id
    headers = {'Content-Type': 'application/json', 'X-Authorization': token}

    return requests.get(url, headers=headers).json()


def get_attribute_value(base_url, credential_id, attribute_id, token):
    url = base_url + 'v2/credentialvault/credentials/' + credential_id + "/attributevalues?credentialAttributeId=" + \
          attribute_id
    headers = {'Content-Type': 'application/json', 'X-Authorization': token}

    return requests.get(url, headers=headers).json()


def update_credential(base_url, credential_id, attribute_value_id, attribute_value_version, new_value, token):
    url = base_url + 'v2/credentialvault/credentials/' + credential_id + "/attributevalues/" + attribute_value_id
    headers = {'Content-Type': 'application/json', 'X-Authorization': token}
    data = json.dumps({
        'value': new_value,
        'version': str(attribute_value_version)
    })

    return requests.put(url, headers=headers, data=data)
