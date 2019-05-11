import random


def randomSeqGen(seedValue, seqLength, valueRange):
    random.seed(seedValue)
    randSeq = []
    for i in range(seqLength):
        num = random.randrange(valueRange[0], valueRange[1])
        randSeq += [num]
    return randSeq


def main():
    print(randomSeqGen(20, 10, (0, 100)))
    print(randomSeqGen(20, 10, (0, 100)))
    print(randomSeqGen(25, 10, (0, 100)))
    return


main()
