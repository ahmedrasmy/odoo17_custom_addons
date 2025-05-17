from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _log_access = True
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Patient Name', required=True)
