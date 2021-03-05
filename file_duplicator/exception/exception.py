

class InvalidTokenException(Exception):
    def __init__(self, token, additional_except=Exception.args):
        self.token = token
        self.additional_except = additional_except
