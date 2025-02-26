# -*- coding: utf-8 -*-

{
    'name': "Lista de tareas",

    'summary': """
        Sencilla Lista de tareas""",

    'description': """
        Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """,

    'author': "Nicolás Pla Mollá",
    'website': "dankranikun.github.io",

    # Indicamos que es una aplicación
    'application': True,

    # Categoría en Odoo
    'category': 'Productivity',
    'version': '0.1',

    # Dependencias del módulo (necesita el módulo base)
    'depends': ['base'],

    # Archivos a cargar
    'data': [
        # Política de acceso
        'security/ir.model.access.csv',
        # Vistas y plantillas
        'views/views.xml',
    ],
}
