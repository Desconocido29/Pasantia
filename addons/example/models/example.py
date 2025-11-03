from odoo import models, fields

class TelefonoPersona(models.Model):
    _name = 'ejemplo.telefono_persona'
    _description = 'Teléfono de Persona'

    telefono = fields.Char(string='Teléfono', required=True)
    persona_id = fields.Many2one(comodel_name='ejemplo.persona', string='Persona', required=True)


class Pais(models.Model):
    _name = 'ejemplo.pais'
    _description = 'País'

    name = fields.Char(string='Nombre del País', required=True)


class Curso(models.Model):
    _name = 'ejemplo.curso'
    _description = 'Curso'

    name = fields.Char(string='Nombre del Curso', required=True)


class Persona(models.Model):
    _name = 'ejemplo.persona'
    _description = 'Persona'

    name = fields.Char(string='Nombre', required=True)
    pais_id = fields.Many2one(comodel_name='ejemplo.pais', string='País')
    telefonos = fields.One2many(comodel_name='ejemplo.telefono_persona', inverse_name='persona_id', string='Teléfonos')
    cursos = fields.Many2many(comodel_name='ejemplo.curso', string='Cursos')
