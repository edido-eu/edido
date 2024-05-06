# Copyright 2024 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tools import sql


def migrate(cr, version):
    sql.rename_column(cr, "peppol_server", "user", "account_user")
    sql.rename_column(cr, "peppol_server", "password", "account_password")
