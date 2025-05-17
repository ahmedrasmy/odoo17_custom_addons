from odoo import models,fields,api

from odoo17.odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _inherit = ['mail.thread','mail.activity.mixin']

    _description = 'Property'

    name = fields.Char('Property Name',required=True,default='New Property')
    description =fields.Text('Property Description',tracking=True)
    postcode = fields.Char('Postcode',required=True)
    date_availability = fields.Date('Date Availability',tracking=True,default=fields.Date.today())
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    diff = fields.Float('Difference',compute='_compute_diff',store=False)
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area =fields.Integer('Garden Area')
    garden_orientation = fields.Selection([('north','North'),
                                           ('south','South'),
                                           ('east','East'),
                                           ('west','West')
                                           ],default='north')

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char('Owner Address',related='owner_id.address')
    owner_phone = fields.Char('Owner Phone',related='owner_id.phone')


    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
    ], default='draft')

    _sql_constraints = [
        ('unique_name','unique(name)','This name already exists')
    ]

    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            print("Inside _compute_diff method")
            rec.diff = rec.expected_price - rec.selling_price

    @api.onchange('expected_price')
    def onchange_expected_price(self):
        for rec in self:
            print("Inside _onchange_expected_price method")
            return {
                'warning':{'title':'warning','message':'negative value.','type': 'notification'},
            }

    def action_draft(self):
        for record in self:
            print("Inside action  draft")
            record.state = 'draft'
            # it is the same
            # record.write({
            #     'state':'draft'
            # })

    def action_pending(self):
        for record in self:
            print("Inside action  pending")
            record.state = 'pending'

    def action_sold(self):
        for record in self:
            print("Inside action  sold")
            record.state = 'sold'



    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0 :
                raise ValidationError('Bedrooms cannot be 0')


    # CRUD Operations
    #Create Method
    @api.model_create_multi
    def create(self, vals):
        res = super(Property,self).create(vals)
        # Logic Here
        print('This Inside Create Method')
        return res

    #Search Method = Read Method
    @api.model
    def _search(self,domain,offset=0,limit=None,order=None,access_rights_uid=None):
        res = super(Property, self)._search(domain,offset=0,limit=None,order=None,access_rights_uid=None)
        # Logic Here
        print('This Inside search  Method')
        return res

    #Write Method = Update Method
    def write(self,vals):
        res = super(Property, self).write(vals)
        # Logic Here
        print('This Inside Write Method')
        return res

    #Unlink Method = Delete Method
    def unlink(self):
        res = super(Property,self).unlink()
        print('This Inside Unlink method')
        return res


