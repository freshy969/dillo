from pillar.api.node_types import attachments_embedded_schema

node_type_post = {
    'name': 'dillo_post',
    'description': 'Dillo post type',
    'dyn_schema': {
        'post_type': {
            'type': 'string',
            'allowed': [
                'link',
                'text',
            ],
            'default': 'link',
        },
        # The actual content of a post. This can be a link or Markdown-formatted text.
        # Validation of the text happens in the posts/eve_hooks.py file and follows the rule:
        # - if status is draft, no content is allowed
        # - else, content must be min 5 chars long
        # We do not use the 'markdown' Pillar validator because of the specific processing
        # of the value of post_type.
        'content': {
            'type': 'string',
        },
        # The converted-to-HTML content.
        # TODO(fsiddi) rename to _content_html
        # This is not essential, but would be nice to do at some point.
        'content_html': {
            'type': 'string',
        },
        # URL to an image file that is used to generate the node.picture
        'picture_url': {
            'type': 'string',
        },
        # Status follows this order: pending -> draft -> published
        # - pending: just created
        # - draft: edited after creation
        # - published: published from pending or draft
        'status': {
            'type': 'string',
            'allowed': [
                'pending',
                'draft',
                'published',
                'deleted',
                'flagged',
            ],
            'default': 'pending',
        },
        'shortcode': {
            # Alphanumeric ID
            'type': 'string',
            'maxlength': 6,
        },
        'slug': {
            'type': 'string',
        },
        'tags': {
            # Tags are defined per project, here is a sample
            'type': 'list',
            'schema': {
                'type': 'string',
                'allowed': [
                    'Artwork',
                    'Community',
                    'Development',
                ],
                'default': 'Artwork',
            }
        },
        # Total count of positive ratings (updated at every rating action)
        'rating_positive': {
            'type': 'integer',
        },
        # Total count of negative ratings (updated at every rating action)
        'rating_negative': {
            'type': 'integer',
        },
        # Collection of ratings, keyed by user
        'ratings': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'user': {
                        'type': 'objectid'
                    },
                    'is_positive': {
                        'type': 'boolean'
                    },
                    # Weight of the rating based on user rep and the context.
                    # Currently we have the following weights:
                    # - 1 auto null
                    # - 2 manual null
                    # - 3 auto valid
                    # - 4 manual valid
                    'weight': {
                        'type': 'integer'
                    }
                }
            }
        },
        'hot': {'type': 'float'},
        'attachments': attachments_embedded_schema,
        # Count comments for the post.
        # Used for posts listing, so we do not require aggregations.
        'comments_count': {'type': 'integer'},
    },
    'form_schema': {
        'content_html': {'visible': False},
        'hot': {'visible': False},
        'ratings': {'visible': False},
        'rating_positive': {'visible': False},
        'rating_negative': {'visible': False},
        'slug': {'visible': False},
        'shortcode': {'visible': False},
        'attachments': {'visible': False},
        'comments_count': {'visible': False},
    },
    'parent': []
}
