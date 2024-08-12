from odoo import api, fields, models
import datetime

class ProductLabelWizard(models.TransientModel):
    _name = "product.label.wizard"
    _description  = "product.label.wizard"
    product_tmp_ids     = fields.Many2many('product.template',required=True)

    '''
    categ_id      = fields.Many2one('product.template.attribute.value',
                                    domain=[('attribute_id.type_rolls','=','cat')],
                                    string="Categoria",
                                    required=True
                                    )
    model_id = fields.Many2one('product.template.attribute.value',
                               string="Modelo",
                               required=True
                               )

    color_id = fields.Many2one('product.template.attribute.value',
                               domain=[('attribute_id.type_rolls', '=', 'color')],
                               string="Color",
                               required=True
                               )

    #line_ids      = fields.One2many('product.wizard.variant.line','parent_id')
    sale_id       = fields.Many2one('sale.order')
    purchase_id = fields.Many2one('purchase.order')

    def add_product(self):
        product = self.env['product.product'].search([
            ('product_tmpl_id','=',self.product.id),

            ('product_template_attribute_value_ids.id','in', [self.categ_id.id]),
            ('product_template_attribute_value_ids.id', 'in', [self.color_id.id]),
            ('product_template_attribute_value_ids.id', 'in', [self.model_id.id])
        ])

        if not product:

            product = self.env['product.product'].sudo().create({
                'product_tmpl_id': self.product.id ,
                'product_template_attribute_value_ids': [(6,0,[self.categ_id.id,self.color_id.id,self.model_id.id])]
            })

        if self.sale_id:
            self.sale_id.order_line += self.env['sale.order.line'].new({
                'product_id': product.id
            })

        if self.purchase_id:
            self.purchase_id.order_line += self.env['purchase.order.line'].new({
                'product_id': product.id
            })


        #for product in products:
        #    if product.product_template_attribute_value_ids
        #raise ValueError(products)

    @api.onchange('sale_id')
    def change_salex(self):
        pt = self.env['product.template'].search([('attribute_line_ids','!=',False)],limit=1)
        if pt:
            self.product = pt.id
    '''




