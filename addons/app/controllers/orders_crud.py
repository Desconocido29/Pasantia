from odoo import http
from odoo.http import request, Response
import json

class OrdersCrud(http.Controller):

    # Ruta para obtener una orden de compra
    @http.route('/orders/get', type='http', auth='public')
    def get_order(self, **kwargs):
        order_id_str = kwargs.get('id')
        if not order_id_str:
            return Response("Falta el parámetro 'id'", status=400)

        try:
            order_id = int(order_id_str)
        except ValueError:
            return Response("El parámetro 'id' debe ser un número entero", status=400)

        order = request.env['purchase.order'].sudo().browse(order_id)

        if not order.exists():
            return Response(f"Error: Order con ID {order_id} no existe", status=404)

        data = {
            'order_id': order.id,
            'referencia': order.name,
            'proveedor': order.partner_id.name,
            'comprador': order.user_id.name
        }
        return Response(json.dumps(data), content_type='application/json;charset=utf-8')


    # Ruta para crear una orden de compra
    @http.route('/orders/create', type='http', auth='public', methods=["POST"], csrf=False)
    def create_order(self, **kwargs):
        # Detecta si es JSON o x-www-form-urlencoded
        if request.httprequest.content_type == 'application/json':
            try:
                data = json.loads(request.httprequest.data.decode('utf-8'))
            except Exception:
                return Response("Error al parsear JSON", status=400)
        else:
            data = kwargs

        # Validación de parámetros
        try:
            partner_id = int(data.get('partner_id'))
            product_id = int(data.get('product_id'))
            product_qty = float(data.get('product_qty'))
            price_unit = float(data.get('price_unit'))
        except Exception as e:
            return Response(f'Error en parámetros: {str(e)}', status=400)

        partner = request.env['res.partner'].sudo().browse(partner_id)
        product = request.env['product.product'].sudo().browse(product_id)

        if not partner.exists():
            return Response(f'Proveedor con ID {partner_id} no existe', status=404)
        if not product.exists():
            return Response(f'Producto con ID {product_id} no existe', status=404)

        # Crear la orden de compra
        order = request.env['purchase.order'].sudo().create({
            'partner_id': partner.id,
            'order_line': [(0, 0, {
                'name': product.name,
                'product_id': product.id,
                'product_qty': product_qty,
                'price_unit': price_unit,
            })]
        })

        data = {
            'order_id': order.id,
            'referencia': order.name,
            'proveedor': order.partner_id.name,
            'comprador': order.user_id.name
        }
        return Response(json.dumps(data), content_type='application/json;charset=utf-8')
