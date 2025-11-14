{
    'name': 'Modulo2',
    'version': '1.0',
    'summary': 'Este es el segundo modulo',
    'description': 'Descripcion del segundo modulo',
    'author': 'Tu Nombre',
    'website': 'https://tuwebsite.com',
    'depends': ['base', 'animal', 'product', 'point_of_sale'],
    'data': [
        'views/custom_animal_views.xml',
        'views/custom_felf.xml',
    ],
    'installable': True,
    'application': True,
}
