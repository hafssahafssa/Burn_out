from odoo import fields, models, api


class InheritEmployee(models.Model):
    _inherit = 'hr.employee'


