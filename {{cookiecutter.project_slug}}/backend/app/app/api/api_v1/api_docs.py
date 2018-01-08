# Import installed packages
from apispec import APISpec
from flask_apispec import FlaskApiSpec

# Import app code
from ...main import app
from ...core import config

security_definitions = {
    'bearer': {
        'type': 'oauth2',
        'flow': 'password',
        'tokenUrl': f'{config.API_V1_STR}/login/access-token',
        'refreshUrl': f'{config.API_V1_STR}/login/refresh-token',
    }
}

app.config.update({
    'APISPEC_SPEC':
    APISpec(
        title='{{cookiecutter.project_name}}',
        version='v1',
        plugins=('apispec.ext.marshmallow', ),
        securityDefinitions=security_definitions),
    'APISPEC_SWAGGER_URL':
    f'{config.API_V1_STR}/swagger/'
})
docs = FlaskApiSpec(app)

security_params = [{'bearer': []}]

authorization_headers = {
    'Authorization': {
        'description':
        'Authorization HTTP header with JWT token, like: Authorization: Bearer asdf.qwer.zxcv',
        'in':
        'header',
        'type':
        'string',
        'required':
        True
    }
}
