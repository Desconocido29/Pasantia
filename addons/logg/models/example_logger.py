from odoo import models, fields
import logging

logger = logging.getLogger(__name__)

class TransientModule(models.TransientModel):
    _name = 'kg.transient'
    
    name = fields.Char(string='Nombre')
    id_animal = fields.Integer(string='ID')
    
    adios_mundo = fields.Many2one('kg.animal')
    
    

    def Holamundo(self):
        logger.info("Hola Mundo")
        
    def create_animal(self):
        return self.env["kg.animal"].create({"name": self.name})

    def unlink_animal(self):
        return self.env["kg.animal"].browse([self.id_animal]).unlink()

    def write_animal(self):
        return self.env["kg.animal"].browse([self.id_animal]).write({"name": self.name})
    
    def unlink_like_animal(self):
        return self.env["kg.animal"].search([('name','ilike',self.name)]).unlink()

    def adios_mundo_button(self):
        self.env["kg.animal"].adios_mundo()
        
    # def create(self):
    #     env=["kg.animal"].create=("name")
        

