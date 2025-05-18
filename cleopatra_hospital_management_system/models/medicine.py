from odoo import models, fields, api


class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'medicine'
    _log_access = True
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True)
