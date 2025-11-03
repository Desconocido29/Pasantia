from odoo import models, fields

class Persona(models.Model):
    _name = 'persona'
    _description = 'Persona'
    
    
    name = fields.Char(string="name" , required= True)
    
