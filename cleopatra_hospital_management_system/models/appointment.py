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

    patient_id = fields.Many2one('hospital.patient', string='Patient',required=True,domain=[('age','>=',50)])
    medicines_ids = fields.Many2many('hospital.medicine', string='Medicines')

    appointment_fees = fields.Float(String='Appointment Fees')
    x_ray_fees = fields.Float(String='X-Ray Fees')
    chair_fees = fields.Float(String='Chair Fees')
    total_price = fields.Float(string='Total Price',compute='_compute_total_price',store=True)

    @api.depends('appointment_fees', 'x_ray_fees','chair_fees')
    def _compute_total_price(self):
        for appointment in self:
            appointment.total_price = appointment.appointment_fees + appointment.x_ray_fees + appointment.chair_fees