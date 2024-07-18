from pydantic import ValidationError


def handle_errors(err: ValidationError) -> list[dict]:
    msg: list[dict] = []
    for e in err:
        msg.append({"field": e["loc"][0], "error": e["msg"]})
    return msg
