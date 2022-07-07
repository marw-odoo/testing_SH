# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'ss.spaceship'
    _description = 'hopefully this model has an FTL drive!'
    
    name = fields.Char(string='Ship Name', required=True)
    description = fields.Text(string='Description')
    
    available = fields.Boolean(string='Available?', default=True)
    