from odoo import api, fields, models
import datetime

class ProductLabelWizard(models.TransientModel):
    _name = "product.label.wizard"
    _description  = "product.label.wizard"
    product_tmp_ids     = fields.Many2many('product.template',required=True,string="Productos")
    label_id            = fields.Many2one('product.label',required=True,string="Etiqueta")

    def set_labels(self):
        for record in self:
            for product in record.product_tmp_ids:
                product.product_label_ids = [(4,record.label_id.id)]