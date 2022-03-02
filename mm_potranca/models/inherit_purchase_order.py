# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('user_id')
    def _onchange_company_id(self):
        p_type = self.picking_type_id
        if not(p_type and p_type.code == 'incoming' and (p_type.warehouse_id.name == self.user_id.property_warehouse_id.name)):
            self.picking_type_id = self._get_picking_type(self.user_id.property_warehouse_id.name)

    @api.model
    def _get_picking_type(self, warehouse_id):
        picking_type = self.env['stock.picking.type'].search([('code', '=', 'incoming'), ('warehouse_id.name', '=', warehouse_id)], limit=1)
        if not picking_type:
            picking_type = self.env['stock.picking.type'].search([('code', '=', 'incoming'), ('warehouse_id', '=', False)])
        return picking_type