#!/usr/bin/env python
""" mi tawa e nasin lili. ni li ike mute. """
import argparse
import json
import os


def process_word(word: str) -> dict:
    # edge case: multi-word definitions (yupekosi), quotes in definition (pu)
    splits = word.split(" ")
    defin = " ".join(splits[:-1])
    score = splits[-1]
    return {"def": defin, "score": int(score)}


def process_definitions(defs: str) -> list:
    return [process_word(defin.strip()) for defin in defs.split(",")]


def process_line(line: str) -> dict:
    # edge case: files download in DOS format, spare whitespace, []
    if not line or line[0] == "#" or line == os.linesep:
        return {}
    word, *defs = line.split(":")
    defs = ":".join(defs).strip().replace("[", "").replace("]", "").replace('"', "")
    return {word: process_definitions(defs)}


def filter(
    nimi: dict,
    minscore: int = 0,
    minsize: int = 0,
    maxsize: int = 0,
    override: list = [],
):
    """
    don't use this unironically
    it isn't very representative of toki pona

    1. directly assign override words into nimi_sin
    2. remove words having fewer definitions than minsize
        - before score removal for fairness
    3. remove definitions scoring lower than minscore
    4. remove words having more definitions than maxsize
        - for words with altogether too many definitions for brevity
    5. assign remainder to nimi_sin
    """
    nimi_sin = {}
    for key in nimi:
        nimi_lipu = nimi[key]
        nlen = len(nimi_lipu)

        if override and key in override:
            nimi_sin[key] = nimi_lipu

        if minsize and nlen < minsize:
            continue

        nimi_lipu = [w for w in nimi_lipu if w["score"] >= minscore]

        if maxsize and nlen > maxsize:
            # assumption: nimi_lipu is score sorted
            nimi_lipu = nimi_lipu[:maxsize]

        if nimi_lipu:
            nimi_sin[key] = nimi_lipu

    return nimi_sin


def main(argv):
    word_files = ["./nimi_pu.txt", "./nimi_pi_pu_ala.txt", "./nimi_ku.txt"]

    nimi = {}
    for file in word_files:
        f = open(file, "r")
        [nimi.update(process_line(line)) for line in f]
        f.close()

    # loje and pu are the only nimi pu with one definition in `nimi_pu.txt`
    nimi = filter(
        nimi,
        minscore=argv.minscore,
        minsize=argv.minsize,
        maxsize=argv.maxsize,
        override=argv.override,
    )
    print(json.dumps(nimi))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "--minscore",
        "-s",
        dest="minscore",
        default=0,
        choices=range(0, 101),
        type=int,
        help="Remove words with lower than min-score frequency score",
        metavar="[0-100]",
    )
    PARSER.add_argument(
        "--minsize",
        "-n",
        dest="minsize",
        default=0,
        type=int,
        help="Remove words with fewer than min-size definitions",
        metavar="MIN",
    )
    PARSER.add_argument(
        "--maxsize",
        "-m",
        dest="maxsize",
        default=0,
        type=int,
        help="Reduce the number of definitions of a word to max-size",
        metavar="MAX",
    )
    PARSER.add_argument(
        "--override",
        "-o",
        dest="override",
        default=[],
        type=str,
        help="Ignore filtering behavior for given word(s)",
        metavar="OVERRIDE",
        nargs="*",
    )

    ARGV = PARSER.parse_args()

    main(ARGV)
