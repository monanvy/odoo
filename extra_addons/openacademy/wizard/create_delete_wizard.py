# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
	_name = 'openacademy1.wizard'
	
	#Delete All
	@api.multi
	def action_delete(self):
		context = dict(self._context or {})
		active_ids = context.get('active_ids', [])
		list_ids = []
		Sessions = self.env['openacademy.session']
		for record in self.env['openacademy.course'].browse(active_ids):
			list_ids.append(record.id)
		Sessions.search([('course_id', 'in', list_ids)]).unlink()
		return True
	
	#Create All
	def action_create(self):
		context = dict(self._context or {})
		active_ids = context.get('active_ids', [])
		for record in self.env['openacademy.course'].browse(active_ids):
			if not record.session_ids:
				self.env['openacademy.session'].create({
					'course_id': record.id,
					'name': "Testing"})