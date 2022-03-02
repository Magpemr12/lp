# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InhertStockQuant(models.Model):
    _inherit = 'stock.quant'

    user_ids = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])