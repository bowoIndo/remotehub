from odoo.exceptions import Warning
from odoo import models, fields, exceptions, api, _

class Anggota(models.Model):
    _name = 'anggota'


    name = fields.Char(string="NIK", readonly=True, required=True, copy=False, default='New')
    photo = fields.Binary("Photo")
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('self.service') or 'New'
        result = super(Anggota, self).create(vals)
        return result

    full_name = fields.Char('Full Name')
    email = fields.Char('Email')

    email_odoo = fields.Many2one('res.users', string='User Login')

    address = fields.Text('Address')
    phone = fields.Char('Phone Number')
    skill = fields.Text('Skill')
    income = fields.Char('Income')
    payment_method = fields.Char('Payment Method')
    job_function = fields.Text(
        string='Job Function'
    )
    ongoing_job = fields.Text(
        string='Present Job'
    )
    international_client = fields.Char(
        string='Do you have international client ? (stay abroad) *'
    )
    url_link_profile = fields.Text(
        string="url link profile at (upwork/fiver/freelancer/appen/lionbrige, etc) , use ' http:// ' at front . exp : http://linkedin.com/in/afa"
    )
    willing_to_share = fields.Char(
        string='Willing to share your experience and skill?'
    )
    comments = fields.Text(
        string='Comments (what is your goal and wish to this community) *'
    )
    desirable_seminar = fields.Text(
        string='Most desirable seminar/workshop SUBJECT you will attend *'
    )

class anggota_res_users(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, values):
        
        record = super(anggota_res_users, self).create(values)

        anggota_baru = self.env['anggota'].create({
            'email':record.email
        })

        anggota_baru.email_odoo = record

        return record

