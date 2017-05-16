# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo import tools, _
from odoo.modules.module import get_module_resource

from datetime import date, datetime


class Enjoy_Reporte_Base(models.Model):
    _name = "enjoy.report.mail"
    _description = "enjoy Reporte Base"

    company_id = fields.Many2one('res.company', string='Empresa', readonly=True,
                                 default=lambda self: self.env.user.company_id)
    catalogo_id = fields.Many2one('enjoy.catalogo', 'Catalogue', required=True)
    destino_ids = fields.One2many('enjoy.destino', 'report_id', 'Remitentes')

    @api.multi
    def enviar_reporte(self):
        attachment_id = self.env['report'].get_action(self, 'enjoy.report_enjoy_catalogo')
        email_id = self.env['mail.mail'].create({
            'subject': 'Report',
            'email_to': 'roche@uci.cu',
            'email_from': 'roche@uci.cu',
            'body_html': "<html></html>",
            # 'attachment_ids': [(6, 0, attachment_id)]
        })
        self.env['mail.mail'].send(email_id)
        return True
