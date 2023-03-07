def response_type(response):
    if type(response) == list:
            return list_content_type(response)
    elif 'dict' in str(type(response)):
        return dict_content_type(response)
    else:
        return str(type(response)).replace("class ","")

def list_content_type(list):
    types = []
    for i in list:
       types.append(response_type(i))
    return types

def dict_content_type(dict):
    types = {}
    count = 0
    for i, j in dict.items():
        i_type = response_type(i)
        j_type = response_type(j)
        count += 1
        types[f"{count}_{i_type}"] = j_type
    return types


