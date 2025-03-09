from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string='Es Profesor', default=False)

class Guardia(models.Model):
    _name = 'gestion.guardias'
    _description = 'Gestión de Guardias de Profesores'

    fecha = fields.Date(string='Fecha de Guardia', required=True, default=fields.Date.today)
    profesor_id = fields.Many2one('hr.employee', string='Profesor de Guardia', required=True, domain=[('is_teacher', '=', True)])
    grupo_id = fields.Many2one('gestion.grupo', string='Grupo sin Profesor', required=True)
    hora = fields.Char(string='Hora', required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada')
    ], string='Estado', default='pendiente', required=True)

    @api.model
    def create(self, vals):
        existing = self.search([
            ('fecha', '=', vals.get('fecha')),
            ('hora', '=', vals.get('hora')),
            ('grupo_id', '=', vals.get('grupo_id'))
        ])
        if existing:
            raise ValueError("Ya existe una guardia asignada para este grupo en esta hora.")
        return super(Guardia, self).create(vals)

    def action_marcar_realizada(self):
        self.write({'estado': 'realizada'})