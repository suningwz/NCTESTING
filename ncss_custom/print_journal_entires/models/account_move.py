# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    bayan = fields.Char()

    def total_debit_credit(self):
        res = {}
        for move in self:
            dr_total = 0.0
            cr_total = 0.0
            for line in move.line_ids:
                dr_total += line.debit
                cr_total += line.credit
            res.update({'cr_total': cr_total, 'dr_total': dr_total})
        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    payment_order_number = fields.Char()
    bayan = fields.Char()
