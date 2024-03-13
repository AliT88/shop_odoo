from odoo import models, fields

class Product(models.Model):
    _name = "product"
    _description = "Products of my shop"

    name = fields.Char(string="name", required=True)
    descriptions = fields.Text(string="description")
    price = fields.Integer(string="price", required=True)
    created = fields.Date(string="created_date")
    category_id = fields.Many2one('category', string="category")
    
