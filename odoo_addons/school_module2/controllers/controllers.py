# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolModule2(http.Controller):
#     @http.route('/school_module2/school_module2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_module2/school_module2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_module2.listing', {
#             'root': '/school_module2/school_module2',
#             'objects': http.request.env['school_module2.school_module2'].search([]),
#         })

#     @http.route('/school_module2/school_module2/objects/<model("school_module2.school_module2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_module2.object', {
#             'object': obj
#         })

