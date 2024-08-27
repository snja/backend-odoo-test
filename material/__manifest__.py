{
    "name": "Backend Odoo Test",
    "version": "1.0.0",
    "category": "inventory",
    "summary": "backend odoo test",
    "description": """
    backend odoo test
    """,
    "author": "Susanto",
    "depends": ["web","base_setup"],
    "data": [
        "security/ir.model.access.csv",
        "views/material_action.xml",
        "views/material_menuitem.xml",
        "views/material_view.xml"
    ],
    "installable": True,
    "application": True,
    "license": "OEEL-1",
}