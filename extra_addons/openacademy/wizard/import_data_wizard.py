# -*- coding: utf-8 -*-

import xlrd
import base64
from datetime import datetime
from odoo import models, fields, api, _


class ImportWizard(models.TransientModel):
    _name = 'import.wizard'
    _description = 'Import Wizard'

    name = fields.Binary(string='Import Excel')
    filename = fields.Char('Filename')

    error_file = fields.Binary(readonly=True)
    error_file_name = fields.Char('Filename')

    @api.multi
    def create_import_wizard(self):
        data = base64.b64decode(self.name)
        wb = xlrd.open_workbook(file_contents=data)
        #
        error = ''
        valid_lines = []
        for s in wb.sheets():
            for row in range(1, s.nrows):
                title = s.cell(row, 0).value

                validate_pass = True
                if not title:
                    validate_pass = False
                    error += '{0} {1}\n'.format(
                        _('Missing Title at row '), row + 1)
                if validate_pass:
                    vals = {
                        'name': title,
                    }
                    valid_lines.append(vals)
        if error:
            self.error_file = base64.encodestring(error)
            view_id = self.env.ref('openacademy.'
                                    'import_wizard_form')
            return {
                'type': 'ir.actions.act_window',
                'name': _('Data Import'),
                'res_model': 'import.wizard',
                'res_id': self.id,
                'view_id': view_id.id,
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new'
            }
        else:
            for i in range(1, len(valid_lines) + 1):
                _slice = valid_lines[:]
                self.import_data(_slice)
                

    @api.multi
    def import_data(self, _slice):
        Course = self.env['openacademy.course']
        for data in _slice:
            c = Course.search([
                ('name', '=', data.get('name', False))
                ])
            if c:
                c.write(data)
            else:
                c.create(data)