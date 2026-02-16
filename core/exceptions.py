from rest_framework.views import exception_handler as drfEx

def exception_handler(exc, context):
    response = drfEx(exc, context)

    if response is None:
        return response
    

    response.data = {
        "error": {
            "type": response.status_code,
            "details": response.data,
        }
    }
    return response