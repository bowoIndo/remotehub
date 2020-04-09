from odoo import http
from odoo.http import request


class Register(http.Controller):

    @http.route('/web/register', auth='public',methods=['POST'])
    def web_register(self, **kw):
        qq=0
        return "Hello, world"

    @http.route('/register', auth='public')
    def register(self, **kw):
        qq=0
        return "Hello, world"

    # create user dari data anggota dan sincronisasi dengan data yang ada
    @http.route('/create_user', auth='public') 
    def register(self, **kw):
        """
        1. ambil data anggota, 
        2. di looping bagian emailnya
        3. di insert ke user emaiilnya
        4. bila sudah di insert di many2one ke model anggota field : email_odoo
        5. 
        """

        for x in request.env['anggota'].search([]):
            email = x.email
            name = x.full_name
            user_baru = request.env['res.users'].create({'login': email,'name':name, 'email':email})
            x.email_odoo = user_baru

        return "create user"

    @http.route('/redirect', auth='public')
    def index(self, **kw):
        return "<script> window.location.href = 'http://www.w3schools.com'; </script>"


