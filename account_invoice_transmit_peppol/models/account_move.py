# Copyright 2023 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _transmit_invoice_by_peppol(self):
        """Mass sending by peppol"""
        invoices = self._transmit_invoice("peppol")
        return invoices.peppol_export_invoice()
