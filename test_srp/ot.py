from __future__ import unicode_literals
import datetime

from frappe import _
import frappe
import frappe.database
import frappe.utils
from frappe.utils import cint, flt, get_datetime, datetime
import frappe.utils.user
from frappe import conf
from frappe.sessions import Session, clear_sessions, delete_session
from frappe.modules.patch_handler import check_session_stopped
from frappe.translate import get_lang_code
from frappe.utils.password import check_password, delete_login_failed_cache
from frappe.core.doctype.activity_log.activity_log import add_authentication_log
from frappe.twofactor import (should_run_2fa, authenticate_for_2factor,
	confirm_otp_token, get_cached_user_pass)

from six.moves.urllib.parse import quote

import frappe
from frappe.sessions import clear_sessions

import requests

@frappe.whitelist( allow_guest=True )
def out():
    # Specify the user session to log out
    user_session = "8ef1bb21263fb625df60cd7fd28740d261dfe7bf695938bc2ba1c62a"

    # Call the logout method of the Frappe API
        # Set the user session in frappe.local
    frappe.local.session = {"session_id": user_session}

    # Call the logout method of frappe.local
    frappe.local.logout()

    # Optional: Print a success message
    print("Logged out successfully")

    return "Logged out successfully"

    # # Set the ERPNext URL and session cookie
    # url = 'https://apitesting.srp.ai/api/method/frappe.core.doctype.session.session.logout'
    # cookie = 'your_session_cookie'

    # # Make the API request to log out the user
    # response = requests.post(url, cookies={'session_id': cookie})

    # # Check the response status code
    # if response.status_code == 200:
    # print('User logged out successfully')
    # else:
    # print('Failed to log out user')
























# def run_trigger(event='on_login'):
# 		for method in frappe.get_hooks().get(event, []):
# 			frappe.call(frappe.get_attr(method), login_manager=self)


# def clear_cookies():
# 	if hasattr(frappe.local, "session"):
# 		frappe.session.sid = ""
# 	frappe.local.cookie_manager.delete_cookie(["full_name", "user_id", "sid", "user_image", "system_user"])


# @frappe.whitelist( allow_guest=True )
# def logout():

#     # Specify the user for whom you want to log out
#     user = frappe.session.user

#     # Clear sessions for the specified user
#     clear_sessions(user)

#     # Optional: Print a success message
#     print(f"Logged out user: {user}")
# # 	# if not user: user = frappe.session.user
# # 	#     run_trigger('on_logout')

# # 	if user == frappe.session.user:
# # 		delete_session(frappe.session.sid, user=user, reason="User Manually Logged Out")
# # 		clear_cookies()
# # 	else:
# # 		clear_sessions(user)

# # def clear_cookies():
# # 	clear_cookies()
	

