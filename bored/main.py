
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import MyAppError
from .controllers.base import Base
from .controllers.new import New
from .controllers.fetch_and_store import DatabaseController

# configuration defaults
CONFIG = init_defaults('bored')
CONFIG['bored']['database_url'] = 'postgresql://roman:roman@localhost:5432/bored'


class MyApp(App):
    """Bored API Wrapper primary application."""

    class Meta:
        label = 'bored'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            DatabaseController,
        ]

        # postgres controllers
        database_url = CONFIG


class MyAppTest(TestApp,MyApp):
    """A sub-class of MyApp that is better suited for testing."""

    class Meta:
        label = 'bored_1'


def main():
    with MyApp() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except MyAppError as e:
            print('MyAppError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
