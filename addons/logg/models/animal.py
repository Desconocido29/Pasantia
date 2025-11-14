from odoo import models , fields
import logging

_logging = logging.getLogger(__name__)
_logger = logging.getLogger(__name__)


class Animal(models.Model):
    _name = 'kg.animal'
    
    name = fields.Char(string= "animal")
    
    def adios_mundo(self):
        _logging.info("Adios Mundo")
        
    def action_hello_world(self):  
        _logger.info(self.name)

    
    


