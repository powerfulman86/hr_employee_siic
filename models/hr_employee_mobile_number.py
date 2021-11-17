# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import re
from odoo.exceptions import ValidationError


class TelecomCompany(models.Model):
    _name = 'telecom.company'
    _description = 'Telecom Companies'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    note = fields.Text(string="Note")
    company_id = fields.Many2one(comodel_name='res.partner',
                                 domain="[('is_company', '=', True),('type','=','contact')]", required='True')


class EmployeeMobileNumber(models.Model):
    _name = 'employee.mobile.number'
    _description = 'Employee Mobile Numbers'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Mobile Number", size=11, required=True)
    mobile_company_id = fields.Many2one(comodel_name='telecom.company', string='Company', required=True)
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', required=True)
    note = fields.Text(string="Note")

    @api.onchange('name')
    def check_phone_format(self):
        pattern = r"^[0-9]{11}"
        if self.name:
            if not re.match(pattern, self.name):
                raise ValidationError(_("Phone number Format isn't correct"))

    @api.constrains('name')
    def constraints_name(self):
        for rec in self:
            phone_number = self.env['employee.mobile.number'].search([('name', '=', rec.name)])
            if len(phone_number.ids) > 1:
                raise ValidationError(_("Can not Duplicate Phone Number"))

