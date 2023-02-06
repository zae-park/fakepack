import os
import click


@click.command()
@click.argument('name', nargs=1)
@click.argument('url', nargs=1)
def fake(name, url):
    print(f'{name} - {url}')


@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def copy(src, dst):
    """Move file SRC to DST."""
    for fn in src:
        click.echo('move %s to folder %s' % (fn, dst))


@click.command()
def dummy():
    """Move file SRC to DST."""
    print('dummy')
