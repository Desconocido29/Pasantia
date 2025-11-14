from odoo import models , fields, api
from odoo.exceptions import ValidationError

import logging

logger = logging.getLogger(__name__)

class AnimalInherit(models.Model):
    _inherit = 'animal.model'
    
    
    def Holamundo(self):
        logger.info("Hola Mundo")
        
    def adios_mundo_cruel(self):
        logger.info("Adios Mundo desde el modulo2")
        
    @api.model
    def create(self, vals):
        if 'patas' in vals and vals['patas'] <= 3:
            raise ValidationError("No puede tener 3 o menos patas.")
        else:
            logger.info("El animal tiene más de 3 patas.")
        return super(AnimalInherit, self).create(vals)
    
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def Hasta_pronto(self):
        logger.info("Hasta pronto")