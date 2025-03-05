#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class NelsonDepartment(models.Model):
    _name = 'nelson.department'
    _description = 'Department'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True, help='Department name')
    description = fields.Text(string='Description', help='Department description')
    floor_number = fields.Integer(string='Floor Number', default=0, required=True, help='Floor number')
    active = fields.Boolean(string='Active', default=True, help='Check if the department is active')

    _sql_constraints = [
        ('nelson_department_name_unique', 'unique(name)', _('The department name must be unique'))
    ]

    @api.constrains('floor_number')
    def _floor_number_constraint(self):
        for record in self:
            if record.floor_number < -10 or record.floor_number > 10:
                raise models.ValidationError(_('The floor number must be between -10 and 10.')) 