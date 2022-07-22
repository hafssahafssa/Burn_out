from odoo import models, fields, api


class InheritSurvey(models.Model):
    _inherit = 'survey.survey'

