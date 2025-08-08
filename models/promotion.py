from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Promotion(models.Model):
    _name = "promotion"
    _description = "Modelo para gestionar descuentos promocionales en productos"

    name = fields.Char(string="Nombre", required=True)
    active = fields.Boolean(string="Activo", required=False)
    discount = fields.Float(string="Descuento", required=True)
    date_start = fields.Date(string="Fecha de Inicio", required=True)
    date_end = fields.Date(string="Fecha de Fin", required=True)
    product_id = fields.Many2many("product.product", string="Producto", required=True)

    @api.constrains("discount")
    def _check_discount(self):
        for record in self:
            if record.discount < 0 or record.discount > 100:
                raise ValidationError("El descuento debe estar entre 0 y 100.")

    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        for record in self:
            if record.date_end < record.date_start:
                raise ValidationError(
                    "La fecha de cierre no puede ser anterior a la fecha de inicio."
                )

            if record.active:
                for product in record.product_id:
                    promotion_in_between = self.env["promotion"].search(
                        [
                            ("id", "!=", record.id),
                            ("product_id", "in", product.id),
                            ("date_start", "<=", record.date_end),
                            ("date_end", ">=", record.date_start),
                            ("active", "=", True),
                        ]
                    )

                if promotion_in_between:
                    raise ValidationError(
                        "Las fechas de la promoción chocan con las de una promoción activa, por favor, ajuste las fechas."
                    )
