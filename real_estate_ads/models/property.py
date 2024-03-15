from odoo import fields, models, api

class Property(models.Model):
    _name = "estate.property"
    _description = "This is a property"

    name = fields.Char(string="name", required=True)
    description = fields.Text(string="description")
    postcode = fields.Char(string="postcode")
    type_id = fields.Many2one('property.type', string="Property type")
    tag_ids = fields.Many2many('property.tag', string="Property tag")
    date_availability = fields.Date(string="Available from", readonly=True)
    expected_price = fields.Float(string="Expected price")
    best_offer = fields.Float(string="Best offer")
    selling_price = fields.Float(string="selling price")
    bedrooms = fields.Integer(string="Bedrooms")
    leaving_area = fields.Integer(string="Living area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden_area')
    garden_orienatation = fields.Selection([
        ('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West')],
        string="Garden orientation", default="north")


    class PropertyType(models.Model):
        _name = 'property.type'
        _description = 'Each property has a type .i.e House, ...'

        name = fields.Char(string="name", required=True)

    class PropertyTag(models.Model):
        _name = 'property.tag'
        _description = 'Each property can have many tags .i.e Cozy, ...'

        name = fields.Char(string="name", required=True)
    
    
