# -*- coding: utf-8 -*-
# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class PeppolServer(models.Model):

    _name = "peppol.server"

    _inherit = ["peppol.server", "server.env.mixin"]

    _sql_constraints = [  # we cannot really put the constraint on the name...
        ("name_uniq", "unique(name)", "Peppol server name must be unique."),
    ]

    @property
    def _server_env_fields(self):
        _gls_env_fields = [
            "url",
            "url_feedback",
            "account_user",
            "account_password",
        ]
        res = super(PeppolServer, self)._server_env_fields
        res.update({k: {} for k in _gls_env_fields})
        return res
