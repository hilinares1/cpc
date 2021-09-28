# -*- coding: utf-8 -*-
{
    'name': """
Website URL Redirect URL Rewrite""",

    'summary': """
       SEO URL Redirect, URL Rewrite for 301, 404, Bulk URL Redirect, Multiple Website URL Redirection in odoo 14, 13, 12, 11""",

    'description': """
       SEO URL Redirect, URL Rewrite for 301, 404, Bulk URL Redirect, Multiple Website URL Redirection in odoo 14, 13, 12, 11
    """,
    'category': 'Website',
    'version': '14.0.0.0.1',

    'depends': ['base', 'website','product','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/seo_data.xml',
        'views/product_inherit.xml',
        'views/website_seo_redirection_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/assets_demo.xml',
        'demo/website_seo_redirection_demo.xml',
    ],
    'price': 33.00,
    'currency': 'USD',
    'support': ': business@aagaminfotech.com',
    'author': 'Aagam Infotech',
    'website': 'http://aagaminfotech.com',
    'installable': True,
    'license': 'AGPL-3',
    'external_dependencies': {'python': ['qrcode', 'pyotp']},
    'images': ['static/description/images/Banner-Img.png'],
}
