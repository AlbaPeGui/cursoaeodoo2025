from odoo import models, fields


class MusicSchoolClassroom(models.Model):
    _name = 'music.school.classroom'
    _description = 'classrooms'

    name = fields.Char(string="Name", required=True, translate=True)
    capacity = fields.Char(string="capacity", required=True)
    location = fields.Char(string="location", required=True)
