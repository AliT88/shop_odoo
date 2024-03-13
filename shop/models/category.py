from odoo import models, fields, api

class Category(models.Model):
    _name = "category"
    _description = "Each product link at least one category"

    name = fields.Char(string="name", required=True)
    is_sub = fields.Boolean(string="is sub category", default=False)
    super_category = fields.Many2one('category', string="super category")
    full_name = fields.Char(string="name", compute="_compute_full_name")
    color = fields.Integer(string="color")


    @api.depends('super_category', 'name')
    def _compute_full_name(self):
        for record in self:
            if record.is_sub:
                record.full_name = f'{record.super_category.full_name} / {record.name}'
            else:
                record.full_name = record.name
    

    # def _compute_display_name(self):
    #     if self.is_sub:
    #         return self.full_name
    #     return self.name
    