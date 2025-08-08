from odoo import api, fields, models
from datetime import date


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    promotion_id = fields.Many2one(
        "promotion",
        string="Promotion",
        domain="[('id', 'in', applicable_promotion_id)]",
    )

    applicable_promotion_id = fields.Many2many(
        "promotion",
        compute="_compute_applicable_promotion",
        store=False,
    )

    discount = fields.Float(
        string="Discount (%)",
        compute="_compute_discount",
        store=True,
        readonly=False,
    )

    @api.depends("product_id")
    def _compute_applicable_promotion(self):
        today = date.today()
        for line in self:
            if line.product_id:
                promotion = self.env["promotion"].search(
                    [
                        ("product_id", "=", line.product_id.id),
                        ("active", "=", True),
                        ("date_start", "<=", today),
                        ("date_end", ">=", today),
                    ]
                )
                line.applicable_promotion_id = promotion
            else:
                line.applicable_promotion_id = False

    @api.onchange("product_id")
    def _onchange_product_id_promotion(self):
        if self.product_id:
            if self.applicable_promotion_id:
                self.promotion_id = self.applicable_promotion_id

    @api.depends("promotion_id")
    def _compute_discount(self):
        for line in self:
            if line.promotion_id:
                line.discount = line.promotion_id.discount
            else:
                line.discount = 0.0
            
            line.price_unit -= (line.discount / 100.0) * line.price_unit
