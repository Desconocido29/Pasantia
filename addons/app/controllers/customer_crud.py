from odoo import http
from odoo.http import request, Response
import json

class CustomerCRUD(http.Controller):

    @http.route('/customers/create', type='http', auth='public', methods=["POST"], csrf=False)
    def create_customer(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')

        if not name:
            return "Error: falta el nombre"

        customer = request.env['res.partner'].sudo().create({
            'name': name,
            'email': email,
        })
        return f"Cliente creado exitoso: {customer.name} | ID: {customer.id}"


    @http.route('/customers/update', type='http', auth='public', csrf=False)
    def update_customer(self, **kwargs):
        customer_id = kwargs.get('id')
        if not customer_id:
            return "Error: falta el ID"

        customer = request.env['res.partner'].sudo().browse(int(customer_id))

        if not customer.exists():
            return f"Cliente con ID {customer_id} no existe"

        customer.write({
            'name': kwargs.get('name', customer.name),
            'email': kwargs.get('email', customer.email),
        })
        return f"Cliente actualizado: {customer.name} | ID: {customer.id}"

    @http.route('/customers/delete', type='http', auth='public',csrf=False)
    def delete_customer(self, **kwargs):
        customer_id = kwargs.get('id')
        if not customer_id:
            return "Error: falta el ID"

        customer = request.env['res.partner'].sudo().browse(int(customer_id))

        if not customer.exists():
            return f"Cliente con ID {customer_id} no existe"

        customer.unlink()
        return f"Cliente eliminado | ID: {customer_id}"


    @http.route('/customers/get', type='http', auth='public')
    def get_customer(self, **kw):
        customer_id = int(kw.get('id', 0))
        customer = request.env['res.partner'].sudo().browse(customer_id)

        if not customer.exists():
            data = {
                'error': True,
                'message': f'Cliente con ID {customer_id} no encontrado'
            }
            return Response(json.dumps(data), content_type='application/json')

        data = {
            'id': customer.id,
            'name': customer.name,
            'email': customer.email,
        }

        return Response(json.dumps(data), content_type='application/json')
