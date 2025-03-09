from odoo import models, fields

class Grupo(models.Model):
    _name = 'gestion.grupo'
    _description = 'Grupos de Alumnos'

    name = fields.Char(string='Nombre del Grupo', required=True)
    horario = fields.Char(string='Horario', required=True)
    guardia_ids = fields.One2many('gestion.guardias', 'grupo_id', string='Guardias')