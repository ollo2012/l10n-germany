# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountEdiXmlCII(models.AbstractModel):
    _inherit = "account.edi.xml.cii"

    def _get_exchanged_document_vals(self, invoice):
        vals = super()._get_exchanged_document_vals(invoice)
        labor_note = invoice._l10n_de_get_labor_cost_note_text()
        if labor_note:
            existing = vals.get("included_note") or ""
            vals["included_note"] = (
                f"{existing}\n\n{labor_note}" if existing else labor_note
            )
        return vals
