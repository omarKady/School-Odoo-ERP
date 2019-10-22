from odoo import models,fields


class SchoolCourse(models.Model):
    _name = 'school.course'
    name = fields.Char()
