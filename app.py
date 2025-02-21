from flask import Flask
from flask_restful import Api
from user import Users, User, Search, Login, Sign, Delete, Search_all
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_jwt_extended import JWTManager



app = Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True
app.config["JWT_SECRET_KEY"] = "secret_key"
# Swagger setting
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

api.add_resource(Sign, '/signin')
docs.register(Sign)
api.add_resource(Users, '/user')
docs.register(Users)
api.add_resource(User, '/user/<int:id>')
docs.register(User)
api.add_resource(Delete, '/user/<int:user_id>/<int:order_id>')
docs.register(Delete)
api.add_resource(Search, '/search')
docs.register(Search)
api.add_resource(Search_all, '/search_all')
docs.register(Search_all)
api.add_resource(Login, '/login')
docs.register(Login)

if __name__ == '__main__':
    JWTManager().init_app(app)
    app.run()