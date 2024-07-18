from pydantic import ValidationError


def handle_errors(err: ValidationError) -> list[dict]:
    msg: list[dict] = []
    for e in err:
        field = e["loc"][0] if len(e["loc"]) > 0 else ""
        msg.append({"field": field, "error": e["msg"]})
    return msg
