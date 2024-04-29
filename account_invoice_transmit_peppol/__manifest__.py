# Copyright 2023 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Invoice Sent Peppol",
    "version": "16.0.1.0.0",
    "author": "BCIM",
    "license": "AGPL-3",
    "category": "Accounting & Finance",
    "depends": [
        "account_invoice_transmit",
        "account_invoice_export_ubl",
    ],
    "data": [
        "wizards/account_invoice_transmit.xml",
        "data/transmit_method.xml",
        "data/queue_job_channel.xml",
        "data/queue_job_functions.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
