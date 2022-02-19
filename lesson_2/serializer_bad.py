import json
import enum

import toml
import yaml


class FormatType(enum.Enum):
    JSON = 1
    YAML = 2
    TOML = 3


# SINGLE RESPONSIBILITY
# OPEN-CLOSED
class Serializer:
    def __init__(self, format_type: FormatType):
        if format_type not in FormatType:
            raise ValueError(f"Wrong FormatType {format_type}")
        self._format_type = format_type

    def dump(self, value) -> str:
        if self._format_type is FormatType.JSON:
            return json.dumps(value)
        elif self._format_type is FormatType.YAML:
            return yaml.dump(value)
        elif self._format_type is FormatType.TOML:
            return toml.dumps(value)

    def load(self, value: str):
        if self._format_type is FormatType.JSON:
            return json.loads(value)
        elif self._format_type is FormatType.YAML:
            return yaml.load(value, yaml.Loader)
        elif self._format_type is FormatType.TOML:
            return toml.loads(value)


# ----

obj = {"2": [21, 42]}

serializer = Serializer(FormatType.JSON)

d = serializer.dump(obj)
print(d)

o = serializer.load(d)
print(o)
