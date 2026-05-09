def generate_api_schema(app_type):

    if app_type == "crm":

        return {
            "endpoints": [
                {
                    "path": "/login",
                    "method": "POST"
                },
                {
                    "path": "/contacts",
                    "method": "GET"
                }
            ]
        }

    elif app_type == "ecommerce":

        return {
            "endpoints": [
                {
                    "path": "/products",
                    "method": "GET"
                },
                {
                    "path": "/orders",
                    "method": "POST"
                }
            ]
        }

    else:

        return {
            "endpoints": []
        }