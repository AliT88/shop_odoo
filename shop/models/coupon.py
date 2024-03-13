from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Coupon(models.Model):
    _name = "coupon"
    _description = "Coupons have a percent discount"

    code = fields.Char(string="code", required=True)
    expired = fields.Date(string="expired", required=True)
    discount = fields.Integer(string="discount", required=True)
    is_active = fields.Boolean(string="is_active", compute="_compute_is_active")

    @api.depends('expired')
    def _compute_is_active(self):
        for record in self:
            record.is_active = record.expired > fields.Date.today()
    

    @api.constrains('discount')
    def _check_discount(self):
        for record in self:
            if  record.discount < 0 or record.discount > 70:
                raise ValidationError("Discount must be between 0 and 70")


    @api.constrains('expired')
    def _check_expired(self):
        for record in self:
            if (record.expired - fields.Date.today()).days > 10 :
                raise ValidationError("Maximum days to each discount must not be more than 10 days.")


    # @api.autovacuum('Delete expired coupon')
    # def _delete_expired_coupon(self):
    #     self.search([('expired', '<', fields.Date.today())]).unlink()

    
    
    # _sql_constraints = [
    #     ('check_discount', 'CHECK(discount > 0 AND discount <= 70)',' discount must be between 0 and 70')
    # ]