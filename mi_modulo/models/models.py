# -*- coding: utf-8 -*-
from odoo import models, fields, api
class mi_modulo(models.Model):
    _name = 'mi_modulo.mi_modulo'
    _description = 'Mi Modulo Odoo'
    name = fields.Char()
    description = fields.Text()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
