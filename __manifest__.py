# -*- coding: utf-8 -*-
{
    "name": "Retail Promotions",
    "version": "1.0",
    "summary": "Modulo para gestionar descuentos promocionales en productos",
    "depends": ["base", "sale", "product"],
    "data": [
        "views/promotion_kanban_view.xml",        
        "views/promotion_list_view.xml",        
        "views/promotion_view.xml",
        "security/ir.model.access.csv",
    ],
    'license': 'LGPL-3',
}
