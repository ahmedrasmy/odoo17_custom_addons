# -*- coding: utf-8 -*-
# from odoo import http


# class CleopatraHospitalManagementSystem(http.Controller):
#     @http.route('/cleopatra_hospital_management_system/cleopatra_hospital_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cleopatra_hospital_management_system/cleopatra_hospital_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cleopatra_hospital_management_system.listing', {
#             'root': '/cleopatra_hospital_management_system/cleopatra_hospital_management_system',
#             'objects': http.request.env['cleopatra_hospital_management_system.cleopatra_hospital_management_system'].search([]),
#         })

#     @http.route('/cleopatra_hospital_management_system/cleopatra_hospital_management_system/objects/<model("cleopatra_hospital_management_system.cleopatra_hospital_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cleopatra_hospital_management_system.object', {
#             'object': obj
#         })

