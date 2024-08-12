from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_open_sales_js(self):
        return self.product_tmpl_id.action_open_sales_js()

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    sale_line_ids  = fields.One2many('sale.order.line','product_template_id')
    sale_ids       = fields.Many2many('sale.order',compute="get_sale_ids")
    count_sale_ids = fields.Integer(compute="get_sale_ids")
    product_label_id = fields.Many2one('product.label',string="Etiqueta")

    def get_sale_ids(self):
        for record in self:
            sales = self.env['sale.order'].search([('order_line.product_template_id', '=', record.id)])
            record.sale_ids = [(6,0,sales.ids)] if sales else False
            record.count_sale_ids = len(sales) if sales else 0


    def action_open_sales_js(self):
        return {
            "name": f"VENTAS",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "sale.order",
            "target": "current",
            "domain":  [('id','in',self.sale_ids.ids)]

        }
