# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InhertiResUser(models.Model):
    _inherit = 'res.users'

    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account", copy=False,
                                          ondelete='set null',
                                          help="Analytic account to which this project is linked for financial management. "
                                               "Use an analytic account to record cost and revenue on your project.")

    analytic_tag_ids_sale = fields.Many2many('account.analytic.tag', 'tag_sale_rel', string='Analytic Tags sale', store=True, readonly=False)
    analytic_tag_ids_purchase = fields.Many2many('account.analytic.tag', 'tag_purchase_rel', string='Analytic Tags purchase',
                                             store=True, readonly=False)