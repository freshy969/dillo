"""Shortcode management.

A shortcode is an incremental number that's unique per project and per type.
Example types are 'task' and 'shot.
"""

import logging
import pymongo

from bson import ObjectId
from flask import current_app

from dillo.utils.aid import encode_id

log = logging.getLogger(__name__)


def generate_shortcode(project_id, node_type):
    """Generates and returns a new shortcode.

    :param project_id: project ID
    :type project_id: bson.ObjectId
    :param node_type: the type, for now 'dillo_post', but can be extended.
    :type node_type: unicode
    """

    assert isinstance(project_id, ObjectId)

    db = current_app.db()
    db_fieldname = 'extension_props.dillo.last_used_shortcodes.%s' % node_type

    log.debug('Incrementing project %s shortcode for type %r',
              project_id, node_type)

    new_proj = db['projects'].find_one_and_update(
        {'_id': project_id},
        {'$inc': {db_fieldname: 1}},
        {db_fieldname: 1},
        return_document=pymongo.ReturnDocument.AFTER,
    )

    shortcode = new_proj['extension_props']['dillo']['last_used_shortcodes'][node_type]
    return encode_id(shortcode)
