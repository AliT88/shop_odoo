from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Order(models.Model):
    _name = "order"
    _description = "Each order can contian several order item"

    is_paid = fields.Boolean(string="is_paid", default=False)
    user = fields.Many2one('user', string="user")
    items_ids = fields.One2many('order.item', "order", string="items")
    coupon = fields.Char(string="coupon")
    discount = fields.Integer(compute='_compute_discount', string="discount", default=0, readonly=True, store=True,)
    total_price = fields.Float(compute="_compute_total_price", string="total price", readonly=True, store=True,)
    factor_id = fields.Many2one('factor', string='Factor')

    @api.depends('coupon')
    def _compute_discount(self):
        for record in self:
            if record.coupon:
                data = self.env['coupon'].search([('code', '=', record.coupon)])
                if data['is_active']:
                    if data['expired'] > fields.Date.today():
                        record.discount = data['discount']
                    else:
                        raise ValidationError(_("Sorry! your coupon is expired."))
                else:
                    record.discount = 0
                    raise ValidationError(_("Your coupon is wrong"))
            else:
                record.discount = 0
        

    @api.depends('discount')
    def _compute_total_price(self):
        s = 0
        for record in self:
            for item in record.items_ids:
                s += item.total
            if record.discount:
                record.total_price = s - (s * (record.discount/100))
            else:
                record.total_price = s

    # def create(self, vals_list):
    #     self.env['factor'].create({'code': 1001})
    #     return super().create(vals_list)

    def final_registration(self):
        self.is_paid = True
        self.env['factor'].create({'code': 100})
    
class OrderItem(models.Model):
    _name = "order.item"
    _description = "Order Item"

    product = fields.Many2one('product', string="product")
    order = fields.Many2one('order', string="order")
    quantity = fields.Integer(string="quantity")
    total = fields.Integer(compute='_compute_total', string="total", readonly=True)
    price = fields.Integer(related='product.price', string="price")

    @api.depends('product.price', 'quantity')
    def _compute_total(self):
        for record in self:
            record.total = record.product.price * record.quantity
    
    # @api.depends('product.price')
    # def _compute_price(self):
    #     for record in self:
    #         record.price = record.product.price
    




