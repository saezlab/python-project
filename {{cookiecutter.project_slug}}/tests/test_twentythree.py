import {{ cookiecutter.package_name }}

__all__ = ['Test23']


class Test23:

    def test_twentythree(self):

        assert {{ cookiecutter.package_name }}.twentythree() == 23
