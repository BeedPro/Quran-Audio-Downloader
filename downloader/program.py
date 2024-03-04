from constants import Constants
import textwrap

constants = Constants()
QARIS_DATA = constants.QURANIC_AUDIO_DATA["qaris"]["entities"].items()


def output_table(sectionId):
    for key, value in QARIS_DATA:
        name = value["name"]
        relativePath = value["relativePath"]
        sectionId = value["sectionId"]
        if sectionId == 1:
            print(name)


def main():
    output_table(1)


if __name__ == "__main__":
    main()
