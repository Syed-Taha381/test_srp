import frappe
from frappe import _

from werkzeug.utils import redirect

from urllib.parse import quote

import frappe
import frappe.database
import frappe.utils
import frappe.utils.user
from frappe import _, conf
from frappe.core.doctype.activity_log.activity_log import add_authentication_log
from frappe.modules.patch_handler import check_session_stopped
from frappe.sessions import Session, clear_sessions, delete_session
from frappe.translate import get_language
from frappe.twofactor import (
	authenticate_for_2factor,
	confirm_otp_token,
	get_cached_user_pass,
	should_run_2fa,
)
from frappe.utils import cint, date_diff, datetime, get_datetime, today
from frappe.utils.password import check_password
from frappe.website.utils import get_home_page



# from werkzeug.utils import redirect
import frappe
from frappe.utils import get_url

def override_on_logout():
    frappe.msgprint(_("Opening in a new tab..."))
    url = "http://stg.srp.ai/users/api/logout/method"
    # Emit JavaScript to open a new tab and navigate to the provided URL
    frappe.emit_js("window.open('{0}', '_blank')".format(url))
    # frappe.throw(_("Opening in a new tab..."))


    # Custom logout logic goes here
    # redirect_url = "http://stg.srp.ai/users/api/logout/method"  # Replace with your desired custom page URL

    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = redirect_url
    # frappe.local.request.path == "http://stg.srp.ai/users/api/logout/method"

    # Clear session and perform any other necessary cleanup


# def override_on_logout():
#     # Custom logout logic for ERPNext goes here

#     # Perform logout action in the other property software
#     other_software_logout_url = "http://stg.srp.ai/users/api/logout/method"
    
#     # Make an API call to trigger the logout in the other software
#     response = requests.get(other_software_logout_url)
    
#     if response.status_code == 200:
#         # Logout was successful in the other software
#         frappe.local.response["type"] = "redirect"
#         frappe.local.response["location"] = other_software_logout_url
#     else:
#         # Handle error if logout in the other software failed
#         frappe.throw("Logout from the other software failed")

# # Override the on_logout method of User
# frappe.get_hooks().update({
#     "on_logout": override_on_logout
# })
# # from console import console
# @frappe.whitelist( allow_guest=True )
# def override_on_logout():
#     # frappe.local.login_manager.logout()
#     redirect_url = "http://stg.srp.ai/users/api/logout/method"
#     # frappe.local.response["type"] = "redirect"
#     # frappe.local.response["location"] = redirect_url
#     # return redirect(redirect_url)

#     frappe.local.flags.redirect_location = redirect_url

#     # Return None to indicate successful execution of the hook
    


    
    # return frappe.utils.get_url(redirect_url)
    # Custom logout logic goes here
    # redirect_url = "http://stg.srp.ai/users/api/logout/method"
    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = redirect_url

    


# @frappe.whitelist( allow_guest=True )
# def override_on_logout():
#     # console("rehan").log()    
#     # print("rehan")
#     # Custom logout logic goes here
#     logout_url = "http://stg.srp.ai/users/api/logout/method"
#     redirect_to_login(logout_url)
#     # frappe.utils.redirect(logout_url)

# # Register the hook
# def setup_hooks():
#     hooks = {
#         "on_logout": override_on_logout
#     }
#     return hooks    

    

    # Call the clear_user_cache function from app.overrides module
    # from app.overrides import clear_user_cache
    # clear_user_cache()

# def override_logout():
#     # frappe.local.login_manager.logout()
# 	redirect_url = "https://google.com"
# 	frappe.local.response["type"] = "redirect"
# 	frappe.local.response["location"] = redirect_url


# frappe.get_hooks().update({
#     "on_logout": override_on_logout,
#     "on_session_logout": override_logout
# })

