from ..models.material import Material
from odoo.tests import common,tagged


@tagged("standard", "material")
class TestMaterial(common.TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestMaterial, self).setUp()
        self.suplier = self.env['material.suplier'].create({
            "name": "PT SUPLIER1"
        })
        self.record : Material = self.env['material'].create({
            "code":"123",
            "name": "test",
            "type": "jeans",
            "buy_price": 500,
            "suplier_id": self.suplier.id
            })
        
    def test_01_material_price(self):
        self.assertGreater(self.record.buy_price, 100, "buy price > 100")


    def test_02_material_all_not_none(self):
        self.assertIsNotNone(self.record.code, "code required")
        self.assertIsNotNone(self.record.name, "name required")
        self.assertIsNotNone(self.record.type, "type required")
        self.assertIsNotNone(self.record.suplier_id, "suplier required")
