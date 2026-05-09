def generate_assumptions(prompt):

    prompt = prompt.lower()

    assumptions = []

    if "modern" in prompt:
        assumptions.append(
            "Responsive modern UI included"
        )

    if "app" in prompt:
        assumptions.append(
            "Authentication system included"
        )

    if "dashboard" not in prompt:
        assumptions.append(
            "Basic dashboard added"
        )

    return assumptions