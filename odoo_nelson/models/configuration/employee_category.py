#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class NelsonEmployeeCategory(models.Model):
    _name = 'nelson.employee.category'
    _description = 'Employee Category'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True, help='Employee category name')
    description = fields.Text(string='Description', help='Employee category description')
    priority = fields.Integer(string='Priority', default=0, required=True, help='Priority')
    active = fields.Boolean(string='Active', default=True, required=True, help='Check if the employee category is active')

    is_secretary = fields.Boolean(string='Is Secretary or Assistant', default=False, help='Check if the employee category is a secretary or an assistant')
    is_leader = fields.Boolean(string='Is Leader', default=False, help='Check if the employee category is a leader')
    is_administrator = fields.Boolean(string='Is Administrator', default=False, help='Check if the employee category is an administrator')

    _sql_constraints = [
        ('nelson_employee_category_name_unique', 'unique(name)', _('The employee category name must be unique'))
    ]

    @api.constrains('priority')
    def _priority_constraint(self):
        for record in self:
            if record.priority < 0:
                raise models.ValidationError(_('The priority must be greater than zero'))