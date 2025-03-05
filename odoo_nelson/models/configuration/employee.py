#-*- coding: utf-8 -*-
from odoo import models, fields, api, _

# Constants
HR_EMPLOYEE_MODEL = 'hr.employee'

class NelsonEmployee(models.Model):
    _name = 'nelson.employee'
    _description = 'Employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name'

    employee_id = fields.Many2one(HR_EMPLOYEE_MODEL, string='Employee ID', required=True, help='Employee ID')
    name = fields.Char(string='Name', related="employee_id.name", store=True, help='Name')
    employee_category_id = fields.Many2one('nelson.employee.category', string='Employee Category', required=True, help='Employee Category')
    department_id = fields.Many2one('nelson.department', string='Department', required=True, help='Department')
    active = fields.Boolean(string='Active', default=True, help='Active')
