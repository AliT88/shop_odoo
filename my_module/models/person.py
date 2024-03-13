from odoo import models, fields

class person(models.Model):
    _name = "my_person"
    _description = "person informations"

    full_name = fields.Char(string="name", required=True)
    age = fields.Integer(string="age", default=0)
    phone_number = fields.Char(string="phone", required=True)
    birth_day = fields.Date(string="BirthDay")
    is_mar = fields.Boolean(string="Married", default=False)


