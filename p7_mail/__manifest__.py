# -*- coding: utf-8 -*-

{
    'name': 'Discuss',
    'version': '1.0',
    'category': 'Discuss',
    'summary': 'Chat, mail gateway and private channels',
    'description': "",
    'website': 'https://www.odoo.com/page/discuss',
    'depends': ['base', 'base_setup', 'bus', 'web_tour'],
    'data': [
        'data/mail_template.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'qweb': [
        # 'static/src/xml/activity.xml',
        # 'static/src/xml/activity_view.xml',
        # 'static/src/xml/composer.xml',
        # 'static/src/xml/chatter.xml',
        # 'static/src/xml/discuss.xml',
        # 'static/src/xml/followers.xml',
        # 'static/src/xml/systray.xml',
        # 'static/src/xml/thread.xml',
        # 'static/src/xml/abstract_thread_window.xml',
        # 'static/src/xml/thread_window.xml',
        # 'static/src/xml/announcement.xml',
        # 'static/src/xml/web_kanban_activity.xml',
    ],
}
