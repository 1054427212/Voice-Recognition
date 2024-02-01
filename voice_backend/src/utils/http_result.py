from flask import jsonify
from src.carbon.utils.JSON_encoder import CustomJSONEncoder

json_encoder = CustomJSONEncoder


class HttpResult:
    @classmethod
    def success(cls, data, code=200, message='success', **kwargs):
        res = {
            'data': data,
            'code': code,
            'message': message
        }
        for key, value in kwargs.items():
            res[key] = value
        return jsonify(res)

    @classmethod
    def failure(cls, code=500, message='failure'):
        return jsonify(code=code, message=message)
