# Copyright 2024 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    cr.execute("SELECT id FROM transmit_method WHERE code = 'peppol'")
    record = cr.fetchone()
    if record:
        res_id = record[0]
        openupgrade.add_xmlid(
            cr,
            "account_invoice_transmit_peppol",
            "peppol",
            "transmit.method",
            res_id,
            noupdate=True,
        )
