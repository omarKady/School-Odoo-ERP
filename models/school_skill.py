from odoo import models,fields


class SchoolSkill(models.Model):
    _name = 'school.skill'
    name = fields.Char()
