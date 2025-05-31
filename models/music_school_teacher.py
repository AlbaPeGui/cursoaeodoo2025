from odoo import models, fields


class MusicSchoolTeacher(models.Model):
    _name = 'music.school.teacher'
    _description = 'teachers'

    name = fields.Char(string="Name", required=True, translate=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
