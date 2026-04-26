# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountEdiXmlUbl20(models.AbstractModel):
    _inherit = "account.edi.xml.ubl_20"

    def _get_note_vals_list(self, invoice):
        note_vals = super()._get_note_vals_list(invoice)
        labor_note = invoice._l10n_de_get_labor_cost_note_text()
        if labor_note:
            note_vals.append({"note": labor_note})
        return note_vals
