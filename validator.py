import settings


class Validate:

    @staticmethod
    def validate_algo_index(algo_index):
        return isinstance(algo_index, int) and algo_index in range(1, len(settings.ALGO))

    @staticmethod
    def validate_pwd_length(pwd_length):
        return isinstance(pwd_length, int) and pwd_length in range(4, settings.PASSWORD_MAX_LENGTH+1)


