# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InhertStockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    def _default_inventory_adjustment_ref(self):
        ref = self.env['stock.inventory.adjustment.name'].search([])
        lista_ref = ref.mapped('inventory_adjustment_name')
        if lista_ref != []:
            return lista_ref[-1]

    references = fields.Char(default=_default_inventory_adjustment_ref)
    