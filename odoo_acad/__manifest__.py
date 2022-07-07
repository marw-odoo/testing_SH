# -*- coding: utf-8 -*-

{
    'name': 'Ospace Academy',
    
    'summary': """Astronaut Trianing application""",
    
    'description': 'has stuff in it to learn to',
    
    'author': 'Rwasenge',
    
    'website': 'https://odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'license': 'OPL-1',
    
    'depends': ['base'],
    
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv'
    ],
    
    'demo': [
        'demo/spaceship_demo.xml',
    ],
}