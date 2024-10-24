from rest_framework.exceptions import APIException


class CompanyNotInHeader(APIException):
    status_code = 400
    default_detail = 'Empresa não informada no cabeçalho.'
    default_code = 'company_not_in_header'
