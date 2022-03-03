
from odoo import tools
from odoo import models, fields, api


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    x_studio_lnea_de_producto = fields.Selection([
        ('QUALYMILK', 'QUALYMILK'),
        ('PISA', 'PISA'),
        ('OSATU', 'OSATU'),
        ], string='Línea de producto', readonly=True)
    

    x_studio_laboratorios_marcas = fields.Selection([
        ('REAFRIO', 'REAFRIO'),
        ('TECNOCAMPO', 'TECNOCAMPO'),
        ('PISA', 'PISA'),
        ], string='Laboratorios / Marcas', readonly=True)
    
    _depends = {
        'account.move': [
            'name', 'state', 'move_type', 'partner_id', 'invoice_user_id', 'fiscal_position_id',
            'invoice_date', 'invoice_date_due', 'invoice_payment_term_id', 'partner_bank_id',
        ],
        'account.move.line': [
            'quantity', 'price_subtotal', 'amount_residual', 'balance', 'amount_currency',
            'move_id', 'product_id', 'product_uom_id', 'account_id', 'analytic_account_id',
            'journal_id', 'company_id', 'currency_id', 'partner_id',
        ],
        'product.product': ['product_tmpl_id'],
        'product.template': ['categ_id', 'x_studio_lnea_de_producto', 'x_studio_laboratorios_marcas'],
        'uom.uom': ['category_id', 'factor', 'name', 'uom_type'],
        'res.currency.rate': ['currency_id', 'name'],
        'res.partner': ['country_id'],
    }
    
    def _select(self):
        return super(AccountInvoiceReport, self)._select() + ", template.x_studio_lnea_de_producto as x_studio_lnea_de_producto, template.x_studio_laboratorios_marcas"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + ", ai.x_studio_lnea_de_producto as x_studio_lnea_de_producto, template.x_studio_laboratorios_marcas"
    
    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + ", ai.x_studio_lnea_de_producto, template.x_studio_laboratorios_marcas"
