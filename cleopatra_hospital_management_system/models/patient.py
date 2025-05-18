from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api , _

from odoo17.odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Patient Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')

    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        readonly=True
    )

    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', string='State')
    national_id_number = fields.Char(
        string='National ID Number',
        size=14,
        help='Must be exactly 14 characters.'
    )


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                rec.age = relativedelta(today, rec.date_of_birth).years
            else:
                rec.age = 0

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            self.state_id = False  # Reset state if country changes
            return {
                'domain': {
                    'state_id': [('country_id', '=', self.country_id.id)]
                }
            }
        else:
            return {
                'domain': {
                    'state_id': []
                }
            }

    @api.constrains('national_id_number')
    def _check_national_id_number_constrains(self):
        for rec in self:
            # Only check if the field is set and non-empty
            if rec.national_id_number:
                if not rec.national_id_number.isdigit():
                    raise ValidationError(_('National ID Number must contain only digits.'))
                if len(rec.national_id_number) != 14:
                    raise ValidationError(_('National ID Number must be exactly 14 digits long.'))
                allowed_prefix = ['2','3']
                if rec.national_id_number[0] not in allowed_prefix:
                    raise ValidationError(_('National ID Number must be starts with 2 or 3.'))
