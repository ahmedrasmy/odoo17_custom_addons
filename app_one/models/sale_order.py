from odoo import models,fields



class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'This inherited Table Sale Order'

    property_id = fields.Many2one('property')


    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        print("Inside action confirm Method")
        return res