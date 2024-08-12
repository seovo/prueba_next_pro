from odoo import api, fields, models


class productLabel(models.Model):
    _name    = 'product.label'
    name     = fields.Char(required=True)
    description  =  fields.Text()