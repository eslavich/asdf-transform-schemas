import os
from urllib.request import pathname2url, urljoin

from .common import SCHEMAS_ROOT, STANDARD_PATHS_BY_ID


class AsdfTransformSchemasExtension:
    @property
    def types(self):
        return []

    @property
    def tag_mapping(self):
        return []

    @property
    def standard_ids(self):
        return set(STANDARD_PATHS_BY_ID.keys())

    def get_standard_path(self, standard_id):
        return STANDARD_PATHS_BY_ID.get(standard_id)

    @property
    def url_mapping(self):
        transform_root = os.path.join(SCHEMAS_ROOT, "transform")
        transform_root_url = urljoin("file:", pathname2url(transform_root))

        return [(
            "http://astroasdf.org/schemas/transform/",
            transform_root_url + "/{url_suffix}.yaml"
        )]
