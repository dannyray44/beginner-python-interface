import zlib
import json, base64

def is_json(my_var):
    try:
        _ = json.loads(my_var)
    except ValueError as e:
        return False
    return True

def zip_as_json(var):
    if is_json(var):
        json_string = var
    else:
        json_string = json.dumps(var)
    return base64.b64encode( zlib.compress( json_string.encode('utf-8') )).decode('ascii')

def unzip_json(zipped_json, insist=True):
    try:
        json_str = zlib.decompress(base64.b64decode(zipped_json))
    except:
        raise RuntimeError("Could not decode/unzip the contents")
    return json_str


