def main(characters):
    v, h = characters[0], characters[1]
    print()
    print(" ", v, " ")
    print(h," ",h)
    print(" ", v, " ")
    print(h," ",h)
    print(" ", v, " ")

if __name__ == "__main__":
    characters = ['\u25AD', '\u25AF']
    main(characters)