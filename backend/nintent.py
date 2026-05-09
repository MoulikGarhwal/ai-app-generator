def extract_intent(prompt):

    prompt = prompt.lower()

    features = []

    if "login" in prompt:
        features.append("login")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "payments" in prompt:
        features.append("payments")

    if "crm" in prompt:
        app_type = "crm"

    elif "ecommerce" in prompt:
        app_type = "ecommerce"

    else:
        app_type = "general"

    return {
        "app_type": app_type,
        "features": features
    }