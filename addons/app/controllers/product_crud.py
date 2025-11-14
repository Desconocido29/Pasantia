from odoo import http
from odoo.http import request, Response
import json

class productcrud (http.Controller):

    @http.route('/products/create', type='http', auth='public', methods=["POST"], csrf=False)
    def create_product(self, **kwargs):
        name = kwargs.get('name')
        price = kwargs.get('price')

        if not name:
            return "Error: missing name"

        product = request.env['product.template'].sudo().create({
            'name': name,
            'list_price': price,
        })
        return f"Product creado correctamente: {product.name} | ID: {product.id}"


    @http.route('/products/update', type='http', auth='public', csrf=False)
    def update_product(self, **kwargs):
        product_id = kwargs.get('id')
        if not product_id:
            return "Error: missing ID"

        product = request.env['product.template'].sudo().browse(int(product_id))

        if not product.exists():
            return f"Product con ID {product_id} no existe"

        product.write({
            'name': kwargs.get('name', product.name),
            'list_price': kwargs.get('price', product.list_price),
        })
        return f"Product updated: {product.name} | ID: {product.id}"

    @http.route('/products/delete', type='http', auth='public',csrf=False)
    def delete_product(self, **kwargs):
        product_id = kwargs.get('id')
        if not product_id:
            return "Error: missing ID"

        product = request.env['product.template'].sudo().browse(int(product_id))

        if not product.exists():
            return f"Product con ID {product_id} no existe"

        product.unlink()
        return f"Product eliminado | ID: {product_id}"

    @http.route('/products/get', type='http', auth='public')
    def get_product(self, **kw):
        product_id = int(kw.get('id', 0))
        product = request.env['product.template'].sudo().browse(product_id)

        if not product.exists():
            data = {
                'error': f'Product con ID {product_id} no existe'
            }
        else:
            data = {
                'id': product.id,
                'name': product.name,
                'price': product.list_price,
            }

        return Response(json.dumps(data), content_type='application/json;charset=utf-8')