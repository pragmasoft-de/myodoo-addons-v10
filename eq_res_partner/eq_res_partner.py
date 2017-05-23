# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _

class eq_res_partner(models.Model):

    _inherit = 'res.partner'


    eq_firstname = fields.Char('Firstname')
    eq_name2 = fields.Char('Name2')
    eq_name3 = fields.Char('Name3')

    eq_house_no = fields.Char('House number')
    eq_citypart = fields.Char('District')
    eq_birthday = fields.Date('Birthday')
    eq_letter_salutation = fields.Char('Salutation')
    eq_foreign_ref = fields.Char('Foreign reference')
    eq_foreign_ref_purchase = fields.Char('Foreign reference purchase')


    #eq_complete_description = fields.Char(compute='_generate_complete_description', store=True)