from flask import Flask
import routes

app = Flask(__name__)
# Génére les Routes pour l'api
routes.get_routes_api(app)
# Génére les Routes pour le website
routes.get_routes_website(app)
# Génére les Routes pour les erreurs
routes.init_error_handlers(app)

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.run(debug=True)
