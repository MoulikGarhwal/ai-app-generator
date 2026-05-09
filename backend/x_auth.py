def generate_auth(app_type):

    if app_type == "crm":

        return {
            "roles": [
                {
                    "name": "admin",
                    "permissions": [
                        "view_dashboard",
                        "manage_contacts",
                        "manage_users"
                    ]
                },
                {
                    "name": "user",
                    "permissions": [
                        "view_contacts"
                    ]
                }
            ]
        }

    elif app_type == "ecommerce":

        return {
            "roles": [
                {
                    "name": "admin",
                    "permissions": [
                        "manage_products",
                        "manage_orders"
                    ]
                },
                {
                    "name": "customer",
                    "permissions": [
                        "buy_products",
                        "view_orders"
                    ]
                }
            ]
        }

    else:

        return {
            "roles": [
                {
                    "name": "user",
                    "permissions": []
                }
            ]
        }