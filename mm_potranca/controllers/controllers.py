# -*- coding: utf-8 -*-
# from odoo import http


# class MmPotranca(http.Controller):
#     @http.route('/mm_potranca/mm_potranca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mm_potranca/mm_potranca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mm_potranca.listing', {
#             'root': '/mm_potranca/mm_potranca',
#             'objects': http.request.env['mm_potranca.mm_potranca'].search([]),
#         })

#     @http.route('/mm_potranca/mm_potranca/objects/<model("mm_potranca.mm_potranca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mm_potranca.object', {
#             'object': obj
#         })
