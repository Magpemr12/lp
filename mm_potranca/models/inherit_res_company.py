# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritResCompany(models.Model):
    _inherit = 'res.company'

    inter_company = fields.Boolean('Intercompañoas', default=False)
