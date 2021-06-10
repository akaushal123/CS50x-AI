from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence_0 = And(AKnave, AKnight)
knowledge0 = And(
    # TODO
    # Deduced Info
    Or(AKnight, AKnave),
    # Info from given statement
    Implication(AKnight, sentence_0)
)

# Puzzle 1
# A says "We are both knaves."
sentence_0 = And(AKnave, BKnave)
# B says nothing.
knowledge1 = And(
    # TODO
    # Deduced Info
    Or(AKnight, AKnave),
    Or(BKnave, BKnight),
    # Info from given statement
    Implication(AKnight, sentence_0),
    Implication(AKnave, Not(sentence_0))
)

# Puzzle 2
# A says "We are the same kind."
sentence_0 = Or(And(AKnave, BKnave), And(AKnight, BKnight))
# B says "We are of different kinds."
sentence_1 = Or(And(AKnave, BKnight), And(AKnight, BKnave))
knowledge2 = And(
    # TODO
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # Info deduced
    Implication(AKnight, sentence_0),
    Implication(AKnave, Not(sentence_0)),
    Implication(BKnight, sentence_1),
    Implication(BKnave, Not(sentence_1))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
sentence_0 = Or(AKnave, AKnight)
# B says "A said 'I am a knave'."
sentence_1 = And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))
# B says "C is a knave."
sentence_2 = CKnave
# C says "A is a knight."
sentence_3 = AKnight
knowledge3 = And(
    # TODO
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # Info Deduced
    Implication(AKnight, sentence_0),
    Implication(AKnave, Not(sentence_0)),
    Implication(BKnight, sentence_1),
    Implication(BKnave, Not(sentence_1)),
    Implication(BKnight, sentence_2),
    Implication(BKnave, Not(sentence_2)),
    Implication(CKnight, sentence_3),
    Implication(CKnave, Not(sentence_3))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
