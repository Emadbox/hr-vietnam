# -*- coding: utf-8 -*-
# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeeRelation(models.Model):
    _name = 'hr.employee.relation'

    name = fields.Char('Name', required=True)
