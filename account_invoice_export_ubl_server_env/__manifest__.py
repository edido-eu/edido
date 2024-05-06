# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account Invoice Export UBL Server Env",
    "description": """
        Store peppol server into server environment""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV",
    "website": "https://acsone.eu/",
    "depends": ["account_invoice_export_ubl", "server_environment"],
    "data": ["data/peppol_server.xml"],
    "installable": True,
}
