import typer

app = typer.Typer()


@app.command(name="hi",help="this is hi")
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str = typer.Option("typer"), formal: bool = typer.Option(True)):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
