from flask import Blueprint, Blueprint, request
from flask_restx import Api, Resource

blueprint = Blueprint('myapi', __name__)
api = Api(blueprint)

parser = api.parser()
parser.add_argument('message', type=str, help='message to send', required=True, location='form')

@api.route('/echo')
class Echo(Resource):
    @api.expect(parser)
    @api.response(200, 'OK OK')
    @api.response(400, 'NOT VERY GOOD')
    def post(self):
        args = parser.parse_args()
        print(args)
        return 'echo ' + request.form.get('message')

