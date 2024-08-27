import json
from odoo import http
from werkzeug.wrappers import Response


class ResponceJson(Response):

    def __init__(self, success=True, msg="success", data={}) -> None:
        super().__init__(
            status=200 if success else 400,
            content_type="application/json; charset=utf-8", 
            response=json.dumps({
                "success": success,
                "message": msg,
                "data":data
                })
            )
        


class MaterialController(http.Controller):

    @http.route("/material", auth="public")
    def index(self, **params):
        materials = http.request.env['material'].sudo().search([])
        code = params.get("code")
        if code:
            dat = [m.to_dict() for m in materials if m.code==code]
            if dat:
                dat = dat[0]
            else:
                return ResponceJson(False, "not found!", {})
        else:
            dat = [m.to_dict() for m in materials]
        return ResponceJson(data=dat)

    