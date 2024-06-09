from PIL import Image, ImageMath


def create_image(width: int, height: int, expression1: str, expression2: str) -> None:
    expression = f"{expression1} + 8388065495809286503 + {expression2}" # DEC -> HEX -> TEXT
    
    try:
        img = ImageMath.eval(expression, a=Image.new('L', (width, height), 128))

    except TypeError as e: print("\n", e); exit()
    except NameError as e: print("\n", e); exit()
    except SyntaxError as e: print("\n", e); exit()
    except AttributeError: exit()

    img = img.convert('L')
    img.save('image.png')

def main():
    print(
        """
        Welcome to The Star, where you can create an image ASAP!
        """
    )

    create_image(
        int(input("width: ")), 
        int(input("height: ")),
        input("first expression (mathematical operations on images): "),
        input("second expression: "),
    )

if __name__ == "__main__":
    main()
