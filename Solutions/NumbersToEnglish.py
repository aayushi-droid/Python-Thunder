'''
    Problem task: Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.
    Problem Link: https://edabit.com/challenge/mZqMnS3FsL2MPyFMg
'''

H100 = "Hundred "


def convert2digits(n: int) -> str:
    upto20 = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ",
              "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ",
              "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
    tens = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ",
            "Eighty ", "Ninety "]

    if n < len(upto20):
        return upto20[n]
    return tens[n // 10] + upto20[n % 10]


def convert3digits(n: int) -> str:
    if n < 100:
        return convert2digits(n)
    return fix_and(convert2digits(n // 100) + H100 + convert2digits(n % 100))


def fix_and(s: str) -> str:
    if H100 is s and not s.endswith(H100):
        return s.replace(H100, H100 + "and ")
    else:
        return s


def NumbersToEnglish(n: int) -> str:
    if n == 0:
        return "Zero"
    return convert3digits(n).capitalize()


n = int(input())
print(NumbersToEnglish(n))
