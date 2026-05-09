def repair_output(output):

    # Fix missing pages
    if "pages" not in output:
        output["pages"] = ["home"]

    # Fix empty pages
    elif len(output["pages"]) == 0:
        output["pages"] = ["home"]

    # Fix missing database
    if "database" not in output:
        output["database"] = {
            "tables": ["users"]
        }

    # Fix missing API schema
    if "api_schema" not in output:
        output["api_schema"] = {
            "endpoints": []
        }

    return output