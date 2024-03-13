from odoo import models, fields, api

class User(models.Model):
    _name = "user"
    _description = "users of my shop"


    full_name = fields.Char(string="name", required=True)
    name = fields.Char(string="name", related='full_name') # name field display by default 
    birth_day = fields.Date(string="birth_day")
    email = fields.Char(string="email", required=True)
    phone_number = fields.Char(string="phone_number", required=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="gender")
    is_mar = fields.Boolean(string="married", default=False)
    order_ids = fields.One2many('order', 'user', string="orders")

   
   
    
    