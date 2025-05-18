from odoo import models, fields, api


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _log_access = True
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Appointment Date')
    start_time = fields.Datetime(string='Appointment Start Time')
    end_time = fields.Datetime(string='Appointment End Time')

    state = fields.Selection([
        ('new','New'),
        ('scheduled','Scheduled'),
        ('in_progress','In Progress'),
        ('done','Done'),
        ('cancelled','Cancelled'),
    ], default='new',string='State',required=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient',required=True)
    medicines_ids = fields.Many2many('hospital.medicine', string='Medicines')

