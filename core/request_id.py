import threading 

_local = threading.local()

def set_request_id(value):
    _local.request_id = value

def get_request_id():
    return getattr(_local, "request_id", "-")
