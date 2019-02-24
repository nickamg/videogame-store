# -*- coding: utf-8 -*-

from odoo import models, fields, api

class controller(models.Model):
    _name = 'videogame_store.controller'

    console_controller_id = fields.Many2one(
        'videogame_store.console',
        # Este es el domain, es el filtro que solo mostrara los mandos que sean inalambricos
        domain = [('inalambric', '=', True)],
        string = 'Console'
    )
    name = fields.Char(
        string = 'Controller name',
        size = 100,
        required = True
    )
    inalambric = fields.Boolean(
        string = 'Is inalambric'
    )
    color = fields.Char(
        string = 'Controller color',
        size = 20
    )
    description = fields.Text(
        string = 'Controller description'
    )