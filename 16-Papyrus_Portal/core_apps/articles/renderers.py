"""
Article renderers
"""
import json

from rest_framework.renderers import JSONRenderer


class ArticleJSONRenderer(JSONRenderer):
    """Article renderer"""

    charset = "utf-8"

    # data - python object that needs to be serialized
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Custom rendering logic for Article
        Render `data` into JSON, returning a bytestring.
        """
        if renderer_context is None:
            status_code = 200
        else:
            # overiding the JSON renderer to render a list of article under article
            status_code = renderer_context["response"].status_code

        if data is not None:
            errors = data.get("errors", None)
        else:
            errors = None

        if errors is not None:
            return super().render(data, accepted_media_type, renderer_context)
        return json.dumps(
            {
                "status_code": status_code,
                "article": data,
            }
        )


class ArticlesJSONRenderer(JSONRenderer):
    """Articles renderer"""

    charset = "utf-8"

    # data - python object that needs to be serialized
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Custom rendering logic for Articles
        Render `data` into JSON, returning a bytestring.
        """

        # overiding the JSON renderer to render a list of articles under articles
        status_code = renderer_context["response"].status_code
        errors = data.get("errors", None)

        if errors is not None:
            return super().render(data, accepted_media_type, renderer_context)
        return json.dumps(
            {
                "status_code": status_code,
                "articles": data,
            }
        )
