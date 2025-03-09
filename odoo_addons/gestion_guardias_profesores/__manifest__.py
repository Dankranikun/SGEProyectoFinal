{
    'name': 'Gestión de Guardias de Profesores',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de guardias realizadas por profesores en centros educativos.',
    'author': 'Pablo Orbea Benitez',
    'website': 'https://iescanadadelaencina.edu.es',
    'depends': ['base', 'hr'],
    'data': [
    'security/ir.model.access.csv',
    'data/guardia_data.xml',
    'views/hr_employee_views.xml',
    'views/guardia_views.xml',
    'views/guardia_menu.xml',
    'report/guardia_report.xml',
],
    'installable': True,
    'application': True,
}