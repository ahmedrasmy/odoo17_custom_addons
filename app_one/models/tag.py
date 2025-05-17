from odoo import models,fields



class Tag(models.Model):
    _name = 'tag'
    _description = 'This Tag Table'

    name = fields.Char('Tag Name',required=True)
