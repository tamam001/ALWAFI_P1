
from odoo import api, fields, models, _



class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    amount_untaxed = fields.Monetary(string='Amount',
        store=True, readonly=True, compute='_compute_amount', track_visibility='always')
