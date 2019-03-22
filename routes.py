import middlewares.api as api
import middlewares.website as website
import middlewares.errors as errors

# Fonction qui instancie les différentes Routes API
def get_routes_api(app):
    app.add_url_rule('/api/candidates', 'get_candidates', api.get_candidates, methods=['GET'])
    app.add_url_rule('/api/candidates/<int:id>', 'get_candidate', api.get_candidat, methods=['GET'])
    app.add_url_rule('/api/candidates', 'add_candidate', api.add_candidat, methods=['POST'])
    app.add_url_rule('/api/candidates/<int:id>', 'update_candidate', api.update_candidat, methods=['PUT'])
    app.add_url_rule('/api/candidates/<int:id>', 'delete_candidate', api.delete_candidat, methods=['DELETE'])

    app.add_url_rule('/api/interviews', 'get_interviews', api.get_interviews, methods=['GET'])
    app.add_url_rule('/api/interviews/<int:id>', 'get_interview', api.get_interview, methods=['GET'])

    app.add_url_rule('/api/positions', 'get_positions', api.get_positions, methods=['GET'])
    app.add_url_rule('/api/positions/<int:id>', 'get_position', api.get_position, methods=['GET'])

    app.add_url_rule('/api/initdb', 'initdb', api.init_database, methods=['GET'])
    app.add_url_rule('/api/filldb5', 'filldb5', api.fill_database, methods=['GET'])

# Fonction qui instancie les différentes Routes du Website
def get_routes_website(app):
    app.add_url_rule('/index', 'html_index', website.page_index, methods=['GET'])
    app.add_url_rule('/about', 'html_about', website.page_about, methods=['GET'])
    app.add_url_rule('/candidates', 'html_candidates', website.page_candidates, methods=['GET'])
    app.add_url_rule('/interviews', 'html_interviews', website.page_interviews, methods=['GET'])
    app.add_url_rule('/positions', 'html_positions', website.page_positions, methods=['GET'])

# Fonction qui instancie les différentes Routes d'erreur
def init_error_handlers(app):
    app.errorhandler(404)(errors.handle_error_404)
    app.errorhandler(500)(errors.handle_error_500)
    app.add_url_rule('/crash', 'html_crash', errors.crash)
