# custom_methods.py
from frappe import modules
from frappe import _


@frappe.whitelist()
def logout_method():
    return "Rehan"
    # Perform any required actions or cleanup before logging out
    # This method will be called when the logout button is clicked

    # Redirect to the desired logout URL
    # logout_url = "http://stg.srp.ai/users/api/logout/method"
    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = logout_url
