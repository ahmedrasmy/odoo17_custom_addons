from odoo import models,fields



class Client(models.Model):
    _name = 'client'
    _description = 'This client Table Inherited from owner model'
    _inherit = 'owner'
