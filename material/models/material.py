from odoo import models, fields, exceptions, api


class Material(models.Model):
    _name = "material"
    code = fields.Char(string="Code", required=True, index=True)
    name = fields.Char(string="Name", required=True)
    type = fields.Selection(
        [("fabric", "Fabric"), ("jeans", "Jeans"), ("cotton", "Cotton")], required=True
    )
    buy_price = fields.Float(string="Buy Price", required=True)
    suplier_id = fields.Many2one("material.suplier", string="Suplier", required=True)

    @api.constrains("buy_price")
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise exceptions.ValidationError("Buy price < 100")
    
    def to_dict(self):
        return {
            "id":self.id, 
            "name": self.name,
            "code":self.code,
            "buy_price": self.buy_price,
            "suplier": self.suplier_id.to_dict(),
            }


class Suplier(models.Model):
    _name = "material.suplier"
    name = fields.Char(string="Name", required=True, index=True)
    material_id = fields.One2many("material", "suplier_id", string="Suplier")

    def to_dict(self):
        return {"id": self.id, "name": self.name}