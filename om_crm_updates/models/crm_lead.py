from odoo import api, fields, models, _



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_won_stage = fields.Boolean(related='stage_id.is_won', store=True)
    hide_proceed = fields.Boolean(string='Hide Proceed Button', compute='_check_hide_proceed', store=True)

    def change_stage(self):
        for lead in self:
            next_stage_id = lead.stage_id.id+1
        next_stage = self.env['crm.stage'].browse(next_stage_id).name
        self.write({'stage_id': next_stage_id})

    @api.depends('stage_id')
    def _check_hide_proceed(self):
        for rec in self:
            if not rec.stage_id.is_won:
                next_stage_won = self.env['crm.stage'].browse(rec.stage_id.id+1).is_won
            if rec.stage_id.is_won or next_stage_won:
                rec.hide_proceed = True
            else:
                rec.hide_proceed = False