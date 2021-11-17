# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    code = fields.Char(string="Code")

    age = fields.Integer(string="Age", compute="_calculate_age", readonly=True, store='True')
    hire_date = fields.Date(string='Hiring Date')

    @api.depends("birthday")
    def _calculate_age(self):
        for emp in self:
            if emp.birthday:
                dob = emp.birthday
                emp.age = int((datetime.today().date() - dob).days / 365)
            else:
                emp.age = 0

    @api.model
    def _cron_employee_age(self):
        self._calculate_age()

    def name_get(self):
        result = []
        for rec in self:
            name = ('[%s] %s' % (rec.code, rec.name))
            result.append((rec.id, name))
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        super(HrEmployee, self).name_search(name)
        # args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name),
                      ('code', operator, name), ]
        recs = self.search(domain, limit=limit)
        return recs.name_get()

    # course

    count_courses = fields.Integer("Number of courses", compute="_compute_count_courses")
    courses_ids = fields.One2many("hr.course.attendee", "employee_id", string="Courses", readonly=True, )

    @api.depends("courses_ids")
    def _compute_count_courses(self):
        for r in self:
            r.count_courses = len(r.courses_ids)

    def action_view_course(self):
        action = self.env.ref("hr_course.action_view_course")
        result = action.read()[0]
        result["domain"] = [("employee_id", "=", self.id)]
        return result
