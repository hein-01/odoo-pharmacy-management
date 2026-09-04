Odoo ORM မှာ Models တွေကို ပြင်ဆင်တာ၊ တိုးချဲ့တာနဲ့ ချိတ်ဆက်တည်ဆောက်တဲ့အခါ Inheritance အမျိုးအစား ၃ မျိုး ကို အသုံးပြုကြပါတယ်။
၁။ Class / Classical Inheritance (_inherit + မူရင်း Model Name) Database Table အသစ် မဆောက်ပါ။ မူရင်း Table ထဲသို့ Field အသစ်များကို Column များအဖြစ် တိုက်ရိုက် ထပ်မံ ပေါင်းထည့်ပေးလိုက်ခြင်း ဖြစ်ပါတယ်။ မူရင်း Odoo Modules (ဥပမာ - res.partner, sale.order, product.template) တွေထဲမှာ Custom Field တွေ၊ Custom Logic တွေ ထပ်ပေါင်းထည့်ချင်သည့်အခါ သုံးပါတယ်။
၂။ Prototype Inheritance (_inherit + _name အသစ်)
၃။ Delegation Inheritance (_inherits)
