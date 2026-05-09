def validate_output(output):

    errors = []

    # Check app name
    if "app_name" not in output:
        errors.append("Missing app_name")

    # Check pages
    if "pages" not in output:
        errors.append("Missing pages")

    elif len(output["pages"]) == 0:
        errors.append("Pages list is empty")

    # Check database
    if "database" not in output:
        errors.append("Missing database schema")

    # Check API schema
    if "api_schema" not in output:
        errors.append("Missing api schema")

    # Final validation result
    if len(errors) == 0:

        return {
            "valid": True,
            "errors": []
        }

    else:

        return {
            "valid": False,
            "errors": errors
        }