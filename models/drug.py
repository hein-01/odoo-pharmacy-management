from odoo import fields, models, api
from datetime import date, datetime

class Drug(models.Model):
    _inherit = "product.template"

    expiry_date = fields.Date(string="Expiry Date")
    due = fields.Integer(compute="_compute_due")
    due_label = fields.Char(string="Days Left", compute="_compute_due")
    cards_per_bu = fields.Integer(string="တစ်ဗူးရှိကဒ်ပေါင်း")
    tablets_per_card = fields.Integer(string="တစ်ကဒ်ရှိအလုံးရေ")
    quantity_available = fields.Char(string="လက်ကျန်", compute="_compute_quantity_available")
    margin = fields.Float(string="Margin(%)")
    list_price = fields.Float(
      compute="_compute_list_price",
    )

    @api.depends('standard_price', 'margin')
    def _compute_list_price(self):
        for record in self:
            if record.margin:
                record.list_price = record.standard_price * (1 + record.margin / 100)
            else:
                record.list_price = record.standard_price

    @api.depends('expiry_date')
    def _compute_due(self):
        for record in self:
            record.due = (record.expiry_date - fields.Date.today()).days if record.expiry_date else 0
            record.due_label = str(record.due)




    def _compute_quantity_available(self):
        for record in self:
            record.qty_available = int(record.qty_available)
            if record.qty_available != 0 and record.tablets_per_card != 0 and record.cards_per_bu != 0:
                if record.qty_available < record.tablets_per_card:
                    record.quantity_available = f"{int(record.qty_available)}လုံး"
                elif record.qty_available > record.tablets_per_card:
                    lone = int(record.qty_available % record.tablets_per_card)
                    card = int(record.qty_available // record.tablets_per_card)
                    if card > record.cards_per_bu:
                        bu = int(card // record.cards_per_bu)
                        card = int(card % record.cards_per_bu)
                        record.quantity_available = f"{bu}ဗူး,{card}ကတ်,{lone}လုံး"
                    elif card == record.cards_per_bu:
                        card = 0
                        bu = 1
                        record.quantity_available = f"{bu}ဗူး,{card}ကတ်,{lone}လုံး"
                    else:
                        card = int((record.qty_available // record.tablets_per_card))
                        record.quantity_available = f"{card}ကတ်,{lone}လုံး"
            else:
                record.quantity_available = ""
