# -*- coding: utf-8 -*-
# Copyright 2019 Odoo TEAM CI
{
	'name': 'Url Access Restriction',
	'version': '1',
	'category': 'Web',
	'sequence': 0,
	'author': 'OdooTeamCI',
	'summary':'Module Use of Url Access Restriction',
	'license': 'AGPL-3',
	'depends': ['web'],
	'data':['views/url_access_restriction.xml'],
	'qweb': ['static/src/xml/warning_message_page.xml'],
	'installable': True,
	'application': True
}
