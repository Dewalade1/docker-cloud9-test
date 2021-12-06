import click

@click.command()
def hello():
    click.echo("Hello World! I am here!!")
    click.echo("Who are you?")
    
if __name__ == "__main__":
    hello()