activate_this = {{ cookiecutter.ven_activate }}
execfile(activate_this, dict(__file__=activate_this))

from tendril.frontend.app import app as application
from tendril.frontend.app import db
from tendril.frontend.startup.init_app import init_app

init_app(application, db)


