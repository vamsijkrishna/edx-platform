# We intentionally define lots of variables that aren't used, and
# want to import all variables from base settings files
# pylint: disable=W0401, W0614

from .dev import *
from .dev import SUBDOMAIN_BRANDING, VIRTUAL_UNIVERSITIES


MICROSITE_CONFIGURATION = {
	"openedx" : {
		"domain_prefix":"openedx",
		"university":"openedx",
		"platform_name": "Open edX",
		"logo_image_url": "openedx/images/header-logo.png",
		"show_only_org_on_student_dashboard": True,
		"email_from_address": "openedx@edx.org",
	    "payment_support_email": "openedx@edx.org",
	    "ENABLE_MKTG_SITE":  False,
	    "SITE_NAME": "openedx.localhost",
	    "course_org_filter": "CDX",
	    "show_only_org_on_student_dashboard": True,
	    "course_about_show_social_links": False,
	    "css_overrides_file": "openedx/css/openedx.css",
	    "show_partners": False,
	    "show_homepage_promo_video": False,
	    "course_index_overlay_text": "Explore free courses from leading universities.",
	    "course_index_overlay_logo_file": "openedx/images/header-logo.png",
	    "homepage_overlay_html": "<h1>Take an Open edX Course</h1>"
    },
    "forum_academy":
{
	"domain_prefix":"forumacademy",
	"university":"forum_academy",
	"platform_name": "Forum Academy",
	"logo_image_url": "forum_academy/images/header-logo.png",
	"show_only_org_on_student_dashboard": True,
	"email_from_address": "forumacademy@weforum.org",
    "payment_support_email": "forumacademy@weforum.org",
    "ENABLE_MKTG_SITE":  False,
    "SITE_NAME": "forumacademy.localhost",
    "course_org_filter": "ForumAcademyX",
    "show_only_org_on_student_dashboard": True,
    "course_about_show_social_links": True,
    "css_overrides_file": "forum_academy/css/forumacademy.css",
    "show_partners": False,
    "show_homepage_promo_video": False,
    "homepage_promo_video_youtube_id": "eC925sjmRgA",
    "course_index_overlay_text": "Developing Leaders in the Global Public Interest",
    "course_index_overlay_logo_file": "static/forum_academy/images/footer_logo.png",
    "homepage_overlay_html": "<h1>Developing Leaders in the Global Public Interest</h1>",
    "course_about_facebook_link": "https://www.facebook.com/worldeconomicforum",
    "course_about_twitter_account": "@davos",
    "favicon_path": "forum_academy/images/favicon.ico"
}
}

if len(MICROSITE_CONFIGURATION.keys()) > 0:
    enable_microsites(MICROSITE_CONFIGURATION, SUBDOMAIN_BRANDING, VIRTUAL_UNIVERSITIES)