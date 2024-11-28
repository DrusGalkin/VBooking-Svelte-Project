from typing import List, Dict


class CommonMixin:
    @staticmethod
    def to_capitalize(attrs, fields: List[str]):
        for key, value in attrs.items():
            if key in fields:
                attrs[key] = value.capitalize()
        return attrs
