from services.test.impl import ApiService
class Test:
    @staticmethod
    def echo_test():
        msg = "my first test"
        assert ApiService.echo(msg) == msg #+"..."
    @staticmethod
    def log_test():
        assert ApiService.level_logs("my first test") == "OK"