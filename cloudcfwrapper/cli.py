import os
import sys
import click


CONTEXT_SETTINGS = dict(auto_envvar_prefix='CFWRAPPER')


class Context(click.Context):
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg, *args):
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)


@click.command()
@click.argument('filename')
def wrapcmd(filename):
    if not filename.startswith('/'):
        filename = os.path.join(
            os.getcwd(),
            filename
        )

    if not os.path.exists(filename):
        print '404 File Not Found: {}'.format(filename)
        sys.exit(404)

    with open(filename) as f:
        content = f.readlines()

    for line in content:
        line = line.rstrip('\n')
        line = line.replace('"', '\\"')
        line = '"%s\\n",' % line
        print line
