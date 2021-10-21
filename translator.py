#!/usr/bin/env python3
import json
import subprocess
import time

INPUT_FILE = "nimi_lili.json"
OUTPUT_FILE = "nimi_pi_toki_mute.json"

LANGS = ["es", "ja", "tl"]
LANGS_NAME_EN = ["SPANISH", "JAPANESE", "TAGALOG"]
TO_EXEC = ["/bin/trans", "-b", "-t"]


def subprocess_translate():
    to_load = open(INPUT_FILE, "r").read()
    nimi_mute = json.loads(to_load)
    for lang in LANGS:
        for nimi, nimi_meanings in nimi_mute.items():
            for i, meaning in enumerate(nimi_meanings["meanings"]):
                reply = subprocess.check_output(TO_EXEC + [lang, meaning["def"]])
                if reply:
                    reply = reply.decode().strip()
                    nimi_mute[nimi]["meanings"][i][lang] = reply
                    print("OK! %s->%s: %s -> %s" % (nimi, lang, meaning["def"], reply))
                else:
                    print("NO! %s->%s: %s -> %s" % (nimi, lang, meaning["def"], reply))
                time.sleep(10)  # dodge rate limiter

    with open(OUTPUT_FILE, "w") as f:
        f.write(json.dumps(nimi_mute))


def main():
    subprocess_translate()


if __name__ == "__main__":
    main()
