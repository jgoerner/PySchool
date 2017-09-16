import click


@click.command()
def hello():
    click.echo("Hello World")


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello_2(name, count):
    for _ in range(count):
        print("Hello {}".format(name))


if __name__ == "__main__":
    hello_2()
