# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo import tools, _
from odoo.modules.module import get_module_resource

from datetime import date, datetime


class Enjoy_Reporte_House(models.Model):
    _name = "enjoy.report.mail"
    _description = "enjoy Reporte Base"

    casa_id = fields.Many2one('enjoy.casa', 'Casa', required=True)
    destino_ids = fields.Many2many('enjoy.destino', 'enjoy_destino_report_mail', 'report_mail_id', 'destino_id',
                                   'Recipients')

    @api.multi
    def enviar_reporte(self):
        self.ensure_one()
        template = self.env.ref('enjoy.email_template_edi_casa', False)
        for x in self.destino_ids:
            template.email_to = x.email
            template.send_mail(self.casa_id.id, force_send=True)
        return True


class Enjoy_Reporte_Catalogo(models.Model):
    _name = "enjoy.report.catalogo"
    _description = "enjoy Reporte Base"

    catalogo_id = fields.Many2one('enjoy.catalogo', 'Catalogue', required=True)
    destino_ids = fields.Many2many('enjoy.destino', 'enjoy_destino_report_catalogo', 'report_catalogo_id', 'destino_id',
                                   'Recipients')

    @api.multi
    def enviar_reporte(self):
        self.ensure_one()
        template = self.env.ref('enjoy.email_template_edi_catalogo', False)
        for x in self.destino_ids:
            template.email_to = x.email
            template.send_mail(self.catalogo_id.id, force_send=True)
        return True
