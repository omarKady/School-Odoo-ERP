from odoo import models,fields


class Schooltrack(models.Model):
    _name = 'school.track'
    _rec_name = 'track_name'

    track_name = fields.Char()
    desc = fields.Text()
    student_ids = fields.One2many('school.student', 'track_id')

    def open_students_action(self):
        #print(self.student_ids[0].track_id.track_name)
        #students = self.env['school.student'].search([('track_id', '=', self.id)])
        ids = []
        for student in self.student_ids:
            if len(student.name) < 5:
                ids.append(student.id)

        return {
            'name': 'Students Action',
            'type': 'ir.actions.act_window',
            'res_model': 'school.student',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', ids)]
        }
