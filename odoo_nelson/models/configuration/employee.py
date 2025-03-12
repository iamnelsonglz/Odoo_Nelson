#-*- coding: utf-8 -*-
from odoo import models, fields, api, _

# Constants
HR_EMPLOYEE_MODEL = 'hr.employee'

class NelsonEmployee(models.Model):
    _name = 'nelson.employee'
    _description = 'Employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'id'
    _order = 'id asc'

    employee_id = fields.Many2one(HR_EMPLOYEE_MODEL, string='Employee ID', required=True, help='Employee ID')
    employee_category_id = fields.Many2one('nelson.employee.category', string='Employee Category', required=True, help='Employee Category')
    department_id = fields.Many2one('nelson.department', string='Department', required=True, help='Department')
    active = fields.Boolean(string='Active', default=True, help='Active')

    # def test(self):
    #     print('Test')
