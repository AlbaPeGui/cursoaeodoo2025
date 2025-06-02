from odoo import models, fields


class MusicSchoolLesson(models.Model):
    _name = 'music.school.lesson'
    _description = 'lessons'

    name = fields.Char(string="Name", required=True, translate=True)

    teacher_id = fields.Many2one(
        comodel_name='music.school.teacher',
        string="Teacher",
        help="Teacher responsible for this lesson"
    )
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        help="Course containing this lesson"
    )
    classroom_id = fields.Many2one(
        string="Classroom",
        comodel_name="music.school.classroom",
        help="Class associated with this lesson",
    )
    start_date_time = fields.Datetime(
        string="Start Date/Time",
    )
    duration = fields.Char(
        string="Duration",
    )
    notes = fields.Text(
        string="Notes",
    )
    color = fields.Integer(
        string="Color",
        help="Color associated with the course for calendar views"
    )
