{
    'name': 'Animal Hola',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'estamos probando algo muy inportante',
    'description': 'Esto es una practica',
    'author': 'Junior Jaime',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'product', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/views_ani.xml',
        'reports/animal_report.xml',
    ],
    'installable': True,
    'application': True,
    'controllers': ['controllers/animal_api.py'],
}
