"""
Custom profile renderers
"""
import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    """custom profile renderer"""

    charset = "utf-8"

    # data - python object that needs to be serialized
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Custom rendering logic for Profile"""
        # overiding the JSON renderer to render a list of profile under profile
        status_code = renderer_context["response"].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super().render(data, accepted_media_type, renderer_context)
        return json.dumps(
            {
                "status_code": status_code,
                "profile": data,
            }
        )


class ProfilesJSONRenderer(JSONRenderer):
    """cusotm profiles renderer"""

    charset = "utf-8"

    # data - python object that needs to be serialized
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Custom rendering logic for Profile"""
        # overiding the JSON renderer to render a list of profiles under profiles
        status_code = renderer_context["response"].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super().render(data, accepted_media_type, renderer_context)
        return json.dumps(
            {
                "status_code": status_code,
                "profiles": data,
            }
        )
