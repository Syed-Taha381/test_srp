import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def my_custom_logout():
    frappe.local.login_manager.logout()
    redirect_url = "https://apitesting.srp.ai/#login"
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = redirect_url
    return frappe.utils.get_url(redirect_url)

