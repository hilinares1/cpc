# -*- coding: utf-8 -*-
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api, tools, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo.exceptions import Warning
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_sku_code = fields.Char('SKU')
    model = fields.Char('Model')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')