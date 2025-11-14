from odoo import http
from odoo.http import request

class AnimalAPI(http.Controller):

    # TEST para verificar si el controller funciona
    @http.route('/animal/test',  type='http', auth='public', methods=["GET"])
    def test(self):
        return "FUNCIONA 2"

    # Crear animal (JSON-RPC)
    @http.route('/animal', type='json', auth='public', methods=["POST"])
    def create_animal(self, **kw):
        params = kw.get("params", kw)   # acepta jsonrpc y json normal
        animal = request.env['animal.model'].sudo().create({
            'name': params.get('name'),
            'patas': params.get('patas'),
        })
        return {
            'id': animal.id,
            'name': animal.name,
            'patas': animal.patas
        }

    # Actualizar animal
    @http.route('/animal/update', type='json', auth='public', methods=["POST"])
    def update_animal(self, **kw):
        params = kw.get("params", kw)

        animal = request.env['animal.model'].sudo().browse(int(params.get('id')))

        if not animal.exists():
            return {'error': 'Animal no encontrado'}

        animal.write({
            'name': params.get('name'),
            'patas': params.get('patas'),
        })

        return {'ok': True}

    # Eliminar animal
    @http.route('/animal/delete', type='json', auth='public', methods=["POST"])
    def delete_animal(self, **kw):
        params = kw.get("params", kw)

        animal = request.env['animal.model'].sudo().browse(int(params.get('id')))

        if not animal.exists():
            return {'error': 'Animal no existe'}

        animal.unlink()
        return {'deleted': True}

    # Obtener animal por ID
    @http.route('/animal/get', type='json', auth='public', methods=["POST"])
    def get_animal(self, **kw):
        params = kw.get("params", kw)

        animal_id = int(params.get('id', 0))
        animal = request.env['animal.model'].sudo().browse(animal_id)

        if not animal.exists():
            return {'error': True, 'message': f'Animal con id {animal_id} no encontrado'}

        return {
            'id': animal.id,
            'name': animal.name,
            'patas': animal.patas,
            'cliente': animal.nombre_cliente.name if animal.nombre_cliente else "",
        }
