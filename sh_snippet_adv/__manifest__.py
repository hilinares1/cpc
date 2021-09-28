# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
    "name": "Snippet Advance Settings",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "14.0.3",
    "category": "Website",
    "summary": "Set Custom Snippets, Custom Snippet Module, Custom Color, Set Different Hover At Snippet, Custom Border In Snippet, Custom Stylish Snippets, snippet settings Odoo",
    "description": """This module provides some utility features that extend the functionality of the web editor. You can set custom styles for your snippet. You can set a box-shadow, box-shadow hover, border style, custom border width, border color, border-radius, custom background-color.
    """,
    "depends": [
        "web_editor",
        "website"
    ],
    "data": [
        "views/web_editor.xml",
        "views/assets_wysiwyg.xml",
        "views/website_assets_frontend.xml",
    ],
    "images": ["static/description/background.png", ],
    "installable": True,
    "application": True,
    "autoinstall": False,
    "price": 1,
    "currency": "EUR",
    "license": "OPL-1"
}
