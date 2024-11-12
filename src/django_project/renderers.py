import orjson
from rest_framework.renderers import JSONRenderer


class CustomORJSONRenderer(JSONRenderer):
    media_type = "application/json"
    format = "json"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        serialized_data = orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY)
        return serialized_data
