
import os
import inspect


INSTANCE_CONFIG_PATH = os.path.abspath(inspect.getfile(inspect.currentframe()))
INSTANCE_ROOT = os.path.normpath(os.path.join(INSTANCE_CONFIG_PATH, os.pardir))

SVN_ROOT = os.path.join(os.path.expanduser('~/svn'))

DOCUMENT_WALLET_ROOT = os.path.join(INSTANCE_ROOT, 'wallet')
DOCSTORE_ROOT = os.path.join(INSTANCE_ROOT, 'docstore')
REFDOC_ROOT = os.path.join(INSTANCE_ROOT, 'refdocs')

# gEDA Configuration
GAF_ROOT = os.path.expanduser('~/gEDA2')

# Network Configuration
NETWORK_PROXY_TYPE = None
NETWORK_PROXY_IP = '192.168.1.254'
NETWORK_PROXY_PORT = '3128'
NETWORK_PROXY_USER = None
NETWORK_PROXY_PASS = None

ENABLE_REDIRECT_CACHING = False
TRY_REPLICATOR_CACHE_FIRST = False

# Database Configuration
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_USER = 'tendril'
DATABASE_PASS = 'tendril'
DATABASE_DB = 'tendril'

SECRET_KEY = 'SOMESECRECT'

# E-mail Configuration
MAIL_USERNAME = '{{ cookiecutter.tendril_email_user }}'
MAIL_PASSWORD = '{{ cookiecutter.tendril_email_pass }}'
MAIL_DEFAULT_SENDER = '{{ cookiecutter.tendril_email_name }}'
MAIL_SERVER = '{{ cookiecutter.tendril_email_smtp_server }}'
MAIL_PORT = '{{ cookiecutter.tendril_email_smtp_port }}'
MAIL_USE_SSL = True
MAIL_USE_TLS = False

# Default Admin Configuration
ADMIN_USERNAME = '{{ cookiecutter.admin_username }}'
ADMIN_FULLNAME = '{{ cookiecutter.admin_name }}'
ADMIN_EMAIL = '{{ cookiecutter.admin_email }}'
ADMIN_PASSWORD = 'CHANGEME'

# Currency Configuration
BASE_CURRENCY = '{{ cookiecutter.base_currency_code }}'
BASE_CURRENCY_SYMBOL = '{{ cookiecutter.base_currency_symbol }}'

# Company Configuration
COMPANY_LOGO_PATH = os.path.join(INSTANCE_ROOT, '_static', 
				 'logo-w-200px.png')
COMPANY_BLACK_LOGO_PATH = os.path.join(INSTANCE_ROOT, '_static', 
				       'logo-b-200px.png')
COMPANY_PO_LCO_PATH = os.path.join(INSTANCE_ROOT, '_static/po')
COMPANY_GOVT_POINT = "{{ cookiecutter.company_govt_point }}"
COMPANY_PO_POINT = "{{ cookiecutter.company_po_point }}"
COMPANY_NAME = "{{ cookiecutter.company_name }}"
COMPANY_NAME_SHORT = "{{ cookiecutter.company_name }}"
COMPANY_EMAIL = "{{ cookiecutter.company_contact_email }}"
COMPANY_ADDRESS_LINE = "{{ cookiecutter.company_address_line }}"
COMPANY_IEC = "{{ cookiecutter.company_iec }}"

DOCUMENT_WALLET = {}

INVENTORY_LOCATIONS = [
    'Company Inventory',
]

ELECTRONICS_INVENTORY_DATA = [
]

# Vendor Details
_vendor_map_folder = os.path.join(INSTANCE_ROOT, 'sourcing', 'maps')

VENDORS_DATA = [
]
