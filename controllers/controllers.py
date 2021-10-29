# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployeeSiic(http.Controller):
#     @http.route('/hr_employee_siic/hr_employee_siic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee_siic/hr_employee_siic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee_siic.listing', {
#             'root': '/hr_employee_siic/hr_employee_siic',
#             'objects': http.request.env['hr_employee_siic.hr_employee_siic'].search([]),
#         })

#     @http.route('/hr_employee_siic/hr_employee_siic/objects/<model("hr_employee_siic.hr_employee_siic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee_siic.object', {
#             'object': obj
#         })
