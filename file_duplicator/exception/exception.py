class InvalidTokenException(Exception):
    def __init__(self, token, additional_except=Exception.args):
        self.token = token
        self.additional_except = additional_except


class NonUniqueMappingException(Exception):
    def __init__(self, token, additional_except=Exception.args):
        self.token = token
        self.additional_except = additional_except


class TokenCountUnequalException(Exception):
    def __init__(self, left_token_count, right_token_count, additional_except=Exception.args):
        self.left_token_count = left_token_count
        self.right_token_count = right_token_count
        self.additional_except = additional_except
