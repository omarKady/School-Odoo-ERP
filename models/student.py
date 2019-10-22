from odoo import models,fields,api

class Student(models.Model):
    _name = 'school.student'

    @api.depends('gender')
    def _compute_salary(self):
        for record in self:
            if record.gender == 'm':
                record.salary = 5000
            else:
                record.salary = 2000

    @api.onchange('track_id')
    def onchange_track_id(self):
        self.name = 'hany'
        self.age = 25

    @api.onchange('gender')
    def onchange_gender(self):
        domain = [('desc', '!=', False)]
        if self.gender == 'f':
            domain = []
        # if gender = male there is no filter "view all tracks"
        return {
            'domain': {'track_id':domain}
        }

    name = fields.Char(required=True)
    age = fields.Integer()
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([
        ('m','Male'),
        ('f','Female'),
    ])
    desc = fields.Text()
    join_date = fields.Datetime()
    date_of_birth = fields.Date()
    is_accepted = fields.Boolean()
    salary = fields.Float(compute=_compute_salary, store=True)
    track_id = fields.Many2one('school.track',string='Student Track')
    track_desc = fields.Text(related='track_id.desc',store=True,readonly=True)
    skill_ids = fields.Many2many('school.skill')
    course_line_ids = fields.One2many('school.course.line', 'student_id')
    state = fields.Selection([
        ('apply','Applied'),
        ('iq', 'Passed IQ'),
        ('tech', 'Passed Technical'),
        ('refused', 'Refused'),
        ('accepted', 'Accepted'),
    ],default='apply')

    def change_state(self):
        newstate = self.env.context['state']
        self.state = newstate

    def pass_tech(self):
        self.state = 'tech'
