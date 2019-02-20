# -*- coding: utf-8 -*-

from odoo import models, fields, api

class console(models.Model):
    _name = 'videogame_store.console'

    name = fields.Char(
        string = 'Console name',
        size = 20,
        required = True
    )
    year = fields.Integer(
        string = 'Fabrication year',
        size = 4
    )
    manufacturer = fields.Char(
        string = 'Manufacturer name',
        size = 50,
        required = True
    )
    console_generation = fields.Integer(
        string = 'Console generation',
        size = 2
    )
    country = fields.Char(
        string = 'Country of origin',
        size = 50,
        compute = '_compute_country'
    )
    videogame_id = fields.One2many(
        'videogame_store.videogame', 
        inverse_name = 'console_videogame_id', 
        string = 'Videogame'
    )
    controller_id = fields.One2many(
        'videogame_store.controller', 
        inverse_name = 'console_controller_id', 
        string = 'Controller'
    )

    @api.one
    @api.depends('manufacturer')
    def _compute_country(self):
        if self.manufacturer == 'Nintendo':
            self.country = 'Japan'
        elif self.manufacturer == 'Sony':
            self.country = 'Japan'
        elif self.manufacturer == 'Microsoft':
            self.country = 'United States'
        else:
            self.country = 'Other'
