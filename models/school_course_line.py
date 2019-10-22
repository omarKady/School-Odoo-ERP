from odoo import models,fields


class SchoolCourseLine(models.Model):
    _name = 'school.course.line'

    student_id = fields.Many2one('school.student')
    course_id = fields.Many2one('school.course')

    grade = fields.Selection([
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
        ('e','E'),
    ])