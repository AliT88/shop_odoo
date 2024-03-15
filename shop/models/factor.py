from odoo import fields, models, api

class Factor(models.Model):
    _name = "factor"
    _description = "After pay and register your order, a factor is created."

    code = fields.Integer(string="Factor number")
    #order_ids = fields.One2many('order', 'factor_id', string="Order")
     
    
    