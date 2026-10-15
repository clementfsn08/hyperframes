"""Generate the voiceover line by line with a Microsoft neural voice (edge-tts),
keeping per-word timings, then lay the lines on one track with fixed gaps.

Writes assets/vo/line-NN.mp3, assets/vo/voiceover.wav and assets/vo/timings.json
(line start/end and every word's start/end on the final track, in seconds).

Run from the project root:  python3 tools/voiceover.py
Needs: pip install edge-tts ; ffmpeg on PATH ; network access to speech.platform.bing.com.
"""
import asyncio
import json
import os
import subprocess

import edge_tts

VOICE = "fr-FR-VivienneMultilingualNeural"
RATE = "+4%"
LEAD_IN = 0.45  # silence before the first line
OUT = "assets/vo"

# (spoken text, pause after the line in seconds). The brand is written
# "école en main" so the voice pronounces it as three words.
LINES = [
    ("Suivez votre enfant… de près.", 0.55),
    ("Avec école en main, chaque parent voit les notes, les absences et la scolarité de son enfant, directement sur son téléphone.", 0.55),
    ("Et vous, vous dirigez une école… pas une pile de cahiers.", 0.5),
    ("Tout part d'une seule saisie : l'enseignant entre ses notes, elles sont validées. C'est tout.", 0.5),
    ("Plus rien à recopier au secrétariat : bulletins, tableaux d'honneur, certificats… prêts en un clic, à votre logo.", 0.5),
    ("Chaque versement a son reçu numéroté, et vous voyez les impayés en temps réel.", 0.45),
    ("Même pendant un délestage, votre école continue.", 0.6),
    ("École en main. Toute votre école, dans votre main. Essai gratuit de quatorze jours, sur école en main point com.", 1.2),
]


async def synth(text, path):
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    com = edge_tts.Communicate(text, VOICE, rate=RATE, boundary="WordBoundary", proxy=proxy)
    words = []
    with open(path, "wb") as f:
        async for chunk in com.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 1e7
                words.append({"w": chunk["text"], "s": round(start, 3), "e": round(start + chunk["duration"] / 1e7, 3)})
    return words


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


async def main():
    os.makedirs(OUT, exist_ok=True)
    timings, t = [], LEAD_IN
    inputs, filters = [], []
    for i, (text, pause) in enumerate(LINES, 1):
        path = f"{OUT}/line-{i:02d}.mp3"
        words = await synth(text, path)
        d = duration(path)
        timings.append({"line": i, "text": text, "start": round(t, 3), "end": round(t + d, 3),
                        "words": [{**w, "s": round(w["s"] + t, 3), "e": round(w["e"] + t, 3)} for w in words]})
        inputs += ["-i", path]
        filters.append(f"[{i - 1}:a]adelay={int(t * 1000)}|{int(t * 1000)}[a{i}]")
        t += d + pause
    total = round(t, 3)
    mix = ";".join(filters) + ";" + "".join(f"[a{i}]" for i in range(1, len(LINES) + 1)) + \
        f"amix=inputs={len(LINES)}:normalize=0,apad=whole_dur={total},loudnorm=I=-16:TP=-1.5:LRA=7[out]"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", mix, "-map", "[out]",
                    "-ar", "48000", "-ac", "1", f"{OUT}/voiceover.wav"], check=True)
    json.dump({"voice": VOICE, "rate": RATE, "total": total, "lines": timings},
              open(f"{OUT}/timings.json", "w"), ensure_ascii=False, indent=1)
    for l in timings:
        print(f"L{l['line']} {l['start']:6.2f}–{l['end']:6.2f}  {l['text'][:60]}")
    print("total", total)


asyncio.run(main())
