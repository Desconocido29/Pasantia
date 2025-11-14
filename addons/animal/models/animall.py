from odoo import models, fields

class Animal(models.Model):
    _name = 'animal.model'
    _description = 'Registro de Animales'

    name = fields.Char(string="Animal")
    patas = fields.Integer(string="Patas")
    nombre_cliente = fields.Many2one('res.partner', string="Nombre del Cliente")
    raza = fields.Many2many('product.category', string="Raza")

    def action_print_animal_report(self):
        return self.env.ref('animal.report_animal_pdf_action').report_action(self)
