{
    'name': 'Ejemplo Bottom,',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Módulo para gestionar personas',
    'description': 'Ejemplo básico de módulo Odoo con modelo, vista y menú.',
    'author': 'Junior Jaime',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ejemplo_transient_views.xml',
        'views/ejemplo_animal_view.xml',
    ],
    'installable': True,
    'application': True,
}
