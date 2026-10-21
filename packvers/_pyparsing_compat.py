
"""Compatibility helpers for pyparsing 2.x and 3.x."""

try:
    from pyparsing import original_text_for
except ImportError:
    from pyparsing import originalTextFor as original_text_for


def set_parse_action(parser, *args, **kwargs):
    method = getattr(parser, "set_parse_action", None)
    if method is None:
        method = parser.setParseAction
    return method(*args, **kwargs)


def parse_string(parser, *args, **kwargs):
    method = getattr(parser, "parse_string", None)
    if method is None:
        method = parser.parseString
    return method(*args, **kwargs)


def as_list(results):
    method = getattr(results, "as_list", None)
    if callable(method):
        return method()

    return list(results)
