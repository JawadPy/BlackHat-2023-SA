# The Star
The Star is the card of hope. In the darkest of nights there is a light that shines the path to home.The Star is inspiration, motivation and gives us strength to move forward.
- Cypherpunk 2077 (Tarot cards)

## Solution
First, I want you to read: https://pillow.readthedocs.io/en/stable/releasenotes/9.0.0.html#restrict-builtins-available-to-imagemath-eval
This can give you a clear idea about what's going on here.

You have only one hint: `8388065495809286503` can be converted to hex, and then you can convert it to text. You will find that the result is `the flag` (integer > hex > text), which means your flag is in the expression variable. By this information, you may run `Image Generator.exe` and enter the following inputs:
- 1
- 1
- print(
- )

Then you will have your flag on the screen, but why?

In PIL library before version 9.0.0, it allowed you to perform Python code inside the ImageMath.eval(). So, you may print that value of the flag instead of executing some math expressions. Read more about it here: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-22817

...
