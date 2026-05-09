def generate_database(app_type):

    if app_type == "crm":

        return {
            "tables": [
                "users",
                "contacts",
                "leads"
            ]
        }

    elif app_type == "ecommerce":

        return {
            "tables": [
                "users",
                "products",
                "orders",
                "payments"
            ]
        }

    else:

        return {
            "tables": [
                "users"
            ]
        }