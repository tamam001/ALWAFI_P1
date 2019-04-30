# -*- coding: utf-8 -*-
# Part of ALWAFI. See LICENSE file for full copyright and licensing details.

{
    'name': 'IoT Box Homepage',
    'category': 'Point of Sale',
    'sequence': 6,
    'website': 'https://www.odoo.com/page/point-of-sale-hardware',
    'summary': 'A homepage for the IoT Box',
    'description': """
IoT Box Homepage
================

This module overrides ALWAFI web interface to display a simple
Homepage that explains what's the iotbox and show the status,
and where to find documentation.

If you activate this module, you won't be able to access the 
regular ALWAFI interface anymore.

""",
    'depends': ['hw_proxy'],
    'installable': False,
}
