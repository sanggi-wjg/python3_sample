import json


def ret_json_to_dict(jsonStr: str):
    return json.loads(jsonStr)


if __name__ == '__main__':
    result = ret_json_to_dict('{'
                              '    "glossary": {'
                              '        "title": "example glossary",'
                              '		"GlossDiv": {'
                              '            "title": "S",'
                              '			"GlossList": {'
                              '                "GlossEntry": {'
                              '                    "ID": "SGML",'
                              '					"SortAs": "SGML",'
                              '					"GlossTerm": "Standard Generalized Markup Language",'
                              '					"Acronym": "SGML",'
                              '					"Abbrev": "ISO 8879:1986",'
                              '					"GlossDef": {'
                              '                        "para": "A meta-markup language, used to create markup languages such as DocBook.",'
                              '						"GlossSeeAlso": ["GML", "XML"]'
                              '                    },'
                              '					"GlossSee": "markup"'
                              '                }'
                              '            }'
                              '        }'
                              '    }'
                              '}')
    print(result)
    # 일부로 에러내면 json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 561 (char 560)
