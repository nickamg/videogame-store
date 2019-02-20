# -*- coding: utf-8 -*-

from odoo import models, fields, api

class videogame(models.Model):
    _name = 'videogame_store.videogame'

    console_videogame_id = fields.Many2one(
        'videogame_store.console',
        string = 'Console'
    )
    title = fields.Char(
        string = 'Videogame title',
        size = 100,
        required = True
    )
    year = fields.Integer(
        string = 'Release year',
        size = 4
    )
    category = fields.Char(
        string = 'Game category',
        size = 3
    )
    price = fields.Float(
        string = 'Game price',
        digits = (3, 2)
    )
    sold_units = fields.Integer(
        string = 'Sold units',
        size = 9
    )
    earning = fields.Float(
        string = 'Total earnings',
        digits = (9, 2)
    )
    
    @api.onchange('price', 'sold_units')
    def _onchange_price(self):
        self.earning = self.price * self.sold_units
