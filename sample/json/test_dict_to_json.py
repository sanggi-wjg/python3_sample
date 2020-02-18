import json


def ret_dict_to_json(data):
    return json.dumps(data)


if __name__ == '__main__':
    jsonData = ret_dict_to_json(
        {
            'apiMethod': '123',
            'partnerId': 'jamy'
        }
    )

    print(jsonData)
