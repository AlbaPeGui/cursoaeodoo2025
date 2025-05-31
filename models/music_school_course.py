from odoo import models, fields
from datetime import date


class MusicSchoolCourse(models.Model):
    _name = 'music.school.course'
    _description = 'Instruments'

    name = fields.Char(string="Name", required=True, translate=True)
    description = fields.Text(string="Description")
    
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('inprogress', 'In progress'),
            ('finished', 'Finished'),
        ],
        string="Status",
        required=True,
    )
    instrument_id = fields.Many2one(
        comodel_name='music.school.instrument',
        string="Instrument",
        help="Instrument used in the course"
    )
    teacher_id = fields.Many2one(
        comodel_name='music.school.teacher',
        string="Teacher",
        help="Teacher responsible for this course"
    )

    level = fields.Integer(
        string="Level",
    )
    startdate = fields.Date(
        string="Start Date",
    )
    closedate = fields.Date(
        string="Close Date",
    )
    capacity = fields.Integer(
        string="Capacity",
    )

    def finished_course(self):
        for record in self:
            record.status = 'finished'
            record.closedate = date.today()
