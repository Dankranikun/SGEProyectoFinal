# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definimos el modelo de datos
class ListaTareas(models.Model):
    # Nombre y descripción del modelo de datos
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    # Campos del modelo
    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    # Cálculo del campo "urgente" basado en la prioridad
    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 10
            record.urgente = True
        else:
            record.urgente = False
