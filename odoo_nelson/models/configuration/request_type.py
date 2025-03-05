#-*- coding: utf-8 -*-

from odoo import models, fields, api, _

class NelsonRequestType(models.Model):
    _name = 'nelson.request.type'
    _description = 'Request Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True, help='Request type name')
    description = fields.Text(string='Description', help='Request type description')
    priority = fields.Integer(string='Priority', default=0, required=True, help='Priority')
    active = fields.Boolean(string='Active', default=True, required=True, help='Check if the request type is active')

    _sql_constraints = [
        ('nelson_request_type_name_unique', 'unique(name)', _('The request type name must be unique'))
    ]