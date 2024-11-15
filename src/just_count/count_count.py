from just_count.square import square
import click


@click.command()
@click.argument("number", default=5)
def main(number):
    print(f"The square of {number} is {square(number)}")


if __name__ == "__main__":
    main()
