from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    ocupacion = fields.Char(string='Ocupación',)

    representante_id = fields.Many2one('res.partner',string='Representante',)
    
    tarea_id = fields.One2many('project.task','res.partner',string='tareas',)
    
    proyecto_id = fields.Many2many('project.project','res.partner',string='Los proyecto del contacto',)
    
    total_tarea =fields.integer(compute='_compute_total_tareas',string='Total de tareas',)
    
    @api.depends('tarea_id')    
    def _compute_total_tarea(self):
        for partner in self:
            partner.total_tareas= len(partner.tarea_id)

