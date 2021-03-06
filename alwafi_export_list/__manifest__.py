# -*- coding: utf-8 -*-
# Copyright 2018 AlWarfi TEAM CI

{
    'name': 'AlWarfi export list view',
    'version': '11.0.1.0.0',
    'category': 'Web',
    'author': 'AlWarfiTeamCI, \
            AlWarfi Community Association (OCA)',
    'summary':'AlWarfi 11 module to export current list view',
    'license': 'AGPL-3',
    'depends': [
        'web',
    ],
    "data": [
        'views/web_export_view_view.xml',
    ],
	'images': [
		'static/src/img/main_1.png',
		'static/src/img/main_2.png',
		'static/src/img/main_screenshot.png'
	],
    'qweb': [
        "static/src/xml/web_export_view_template.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True

}
