from rest_framework.authentication import TokenAuthentication


class PasanticAuthentication(TokenAuthentication):
    keyword = "PasanticAuth"
