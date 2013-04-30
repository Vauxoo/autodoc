# -*- encoding: utf-8 -*-
from osv import osv
from osv import fields
from tools.translate import _
from tools.convert import xml_import


class ir_ui_menu_cms(osv.osv):
    """
    Especial Menus to be used on CMS.
    """
    _inherit = 'ir.ui.menu'
    _columns = {
        'external_link':fields.char('External Link', 
                        size=254, required=False, readonly=False),
        'for_cms':fields.boolean('For CMS', required=False),
    }
    
    def get_main_cms_menus(cr, uid, context=None):
        return self.search(cr, uid, [], context=context and context or {})        

ir_ui_menu_cms()
