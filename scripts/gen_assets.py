"""Generate the SVG assets for the devvicha GitHub profile README.

Usage: python scripts/gen_assets.py assets data/whisper-trainer-state.json

Every asset has a dark and a light variant so the README can swap them with
<picture> and prefers-color-scheme. Animations are pure CSS inside the SVG
(GitHub runs them when the SVG is shown as an image) and switch off under
prefers-reduced-motion. The loss chart is plotted from the real training log.
"""
import json
import math
import os
import random
import sys
from html import escape

OUT = sys.argv[1]
TRAINER_STATE = sys.argv[2]
os.makedirs(os.path.join(OUT, "cards"), exist_ok=True)

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", text="#e6edf3",
                 muted="#9198a1", faint="#21262d", gold="#FFBE29", teal="#2DD4BF",
                 glow_a=0.20, glow_b=0.13, chip_bg="#1f2630"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d1d9e0", text="#1f2328",
                  muted="#59636e", faint="#e6eaef", gold="#B45309", teal="#0F766E",
                  glow_a=0.10, glow_b=0.08, chip_bg="#eef1f4"),
}

REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def write(name, svg):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)


def est_width(text, size, mono=False):
    """Rough rendered width; deliberately generous so layouts never collide."""
    if mono:
        return len(text) * size * 0.62
    w = 0.0
    for ch in text:
        if ch in "il.,:;|'!·":
            w += 0.30
        elif ch in "mwMW":
            w += 0.86
        elif ch.isupper() or ch.isdigit():
            w += 0.64
        elif ch == " ":
            w += 0.28
        else:
            w += 0.54
    return w * size


def wrap(text, size, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if est_width(trial, size) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# --------------------------------------------------------------------------- header
def header(theme):
    t = THEMES[theme]
    W, H = 1000, 300
    rnd = random.Random(7)

    # Waveform: an envelope shaped like a spoken phrase, bars desynced.
    bars = []
    n, bw, gap = 34, 4.2, 3.4
    x0, cy = 692, 134
    for i in range(n):
        env = 0.25 + 0.75 * abs(math.sin(i / n * math.pi * 2.3)) * (0.55 + 0.45 * math.sin(i / n * math.pi))
        h = 12 + 90 * env * (0.75 + 0.25 * rnd.random())
        dur = 0.55 + rnd.random() * 0.9
        delay = -rnd.random() * 2
        x = x0 + i * (bw + gap)
        bars.append(
            f'<rect class="bar" x="{x:.1f}" y="{cy - h / 2:.1f}" width="{bw}" height="{h:.1f}" rx="2.1" '
            f'fill="url(#waveAll)" style="animation-duration:{dur:.2f}s;animation-delay:{delay:.2f}s"/>'
        )

    phrases = [
        "voice agents that speak Sinhala, Tamil and English",
        "WhatsApp AI agents serving 10K+ customers a day",
        "vision systems that measure garments",
        "ML pipelines that keep retraining themselves",
    ]
    rot = []
    for i, p in enumerate(phrases):
        # An invisible copy of "I build " keeps each phrase aligned after the
        # static prefix whatever font the viewer has.
        rot.append(
            f'<text class="lead rot" x="56" y="188" style="animation-delay:{i * 3}s">'
            f'<tspan fill-opacity="0">I build </tspan><tspan class="hl">{escape(p)}</tspan></text>'
        )

    chips_data = ["AI/ML Engineer @ Surge Robotics", "Production WhatsApp AI agents", "SICET 2026 author"]
    chips, cx = [], 56
    for i, c in enumerate(chips_data):
        w = est_width(c, 13) + 26
        chips.append(
            f'<g class="fade" style="animation-delay:{0.6 + i * 0.15:.2f}s">'
            f'<rect x="{cx:.1f}" y="226" width="{w:.1f}" height="28" rx="14" fill="{t["chip_bg"]}" stroke="{t["border"]}"/>'
            f'<text class="chip" x="{cx + w / 2:.1f}" y="244.5" text-anchor="middle">{escape(c)}</text></g>'
        )
        cx += w + 10

    desc = ("Vichaksha Geekiyanage, AI/ML engineer in Sri Lanka. Builds voice agents that speak Sinhala, "
            "Tamil and English, WhatsApp AI agents serving 10K+ customers a day, garment measuring vision systems "
            "and self retraining ML pipelines.")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Vichaksha Geekiyanage · AI/ML Engineer</title>
<desc id="d">{escape(desc)}</desc>
<defs>
  <radialGradient id="g1" cx="88%" cy="18%" r="55%"><stop offset="0" stop-color="{t["teal"]}" stop-opacity="{t["glow_a"]}"/><stop offset="1" stop-color="{t["teal"]}" stop-opacity="0"/></radialGradient>
  <radialGradient id="g2" cx="4%" cy="105%" r="50%"><stop offset="0" stop-color="{t["gold"]}" stop-opacity="{t["glow_b"]}"/><stop offset="1" stop-color="{t["gold"]}" stop-opacity="0"/></radialGradient>
  <linearGradient id="wave" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox"><stop offset="0" stop-color="{t["teal"]}"/><stop offset="1" stop-color="{t["gold"]}"/></linearGradient>
  <linearGradient id="waveAll" x1="692" y1="0" x2="944" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{t["teal"]}"/><stop offset="1" stop-color="{t["gold"]}"/></linearGradient>
  <clipPath id="clip"><rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18"/></clipPath>
</defs>
<style>
  .sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
  .eyebrow{{font-family:{MONO};font-size:13px;font-weight:600;letter-spacing:3px;fill:{t["gold"]}}}
  .name{{font-family:{SANS};font-size:50px;font-weight:700;letter-spacing:-1px;fill:{t["text"]}}}
  .lead{{font-family:{SANS};font-size:21px;fill:{t["muted"]}}}
  .hl{{fill:{t["teal"]};font-weight:600}}
  .chip{{font-family:{SANS};font-size:13px;font-weight:600;fill:{t["text"]}}}
  .small{{font-family:{MONO};font-size:12px;letter-spacing:1px;fill:{t["muted"]}}}
  .quote{{font-family:{SANS};font-size:15px;font-style:italic;fill:{t["muted"]}}}
  .rot{{opacity:0;animation:rot 12s linear infinite both}}
  @keyframes rot{{0%{{opacity:0}}3%{{opacity:1}}22%{{opacity:1}}25%{{opacity:0}}100%{{opacity:0}}}}
  .bar{{transform-box:fill-box;transform-origin:center;animation:eq 1s ease-in-out infinite alternate}}
  @keyframes eq{{0%{{transform:scaleY(.18)}}100%{{transform:scaleY(1)}}}}
  .fade{{opacity:0;animation:fade .7s ease-out forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  .blink{{animation:blink 1.2s ease-in-out infinite}}
  @keyframes blink{{50%{{opacity:.15}}}}
  @media (prefers-reduced-motion: reduce){{*{{animation:none!important}} .rot{{opacity:0}} .rot:first-of-type{{opacity:1}} .fade{{opacity:1}}}}
</style>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="{t["bg"]}"/>
  <rect width="{W}" height="{H}" fill="url(#g1)"/>
  <rect width="{W}" height="{H}" fill="url(#g2)"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{t["border"]}"/>

<text class="eyebrow" x="56" y="76">AI/ML ENGINEER · VOICE AI · COMPUTER VISION</text>
<text class="name" x="54" y="136">Vichaksha Geekiyanage</text>
<text class="lead" x="56" y="188">I build</text>
<g>{"".join(rot)}</g>
{"".join(chips)}

<circle class="blink" cx="698" cy="72" r="4.5" fill="{t["gold"]}"/>
<text class="small" x="711" y="76">LISTENING</text>
<text class="small" x="944" y="76" text-anchor="end">si · ta · en</text>
<g>{"".join(bars)}</g>
<text class="quote" x="944" y="212" text-anchor="end">“Ayubowan! How can I help you today?”</text>
</svg>
'''


# --------------------------------------------------------------------------- cards
CARDS = [
    dict(id="whatsapp", accent="gold", live=True, eyebrow="IN PRODUCTION · LLM AGENTS", title="WhatsApp AI Agents",
         desc="Order taking agents with idempotent ingestion, SQL audit trails, human takeover and LLM monitoring.",
         metric="10K+", label="customers served every day",
         chips=["PostgreSQL", "Prisma", "Redis", "NestJS", "Fiddler AI"]),
    dict(id="asr", accent="teal", eyebrow="RESEARCH · SICET 2026", title="Sinhala Lyrical ASR",
         desc="Whisper large v2 adapted with LoRA to transcribe Sinhala songs, powering lyric search and copyright detection.",
         metric="15.7M", label="trainable params, about 1% of the 1.55B model",
         chips=["PyTorch", "Hugging Face", "PEFT", "Elasticsearch"]),
    dict(id="garment", accent="teal", eyebrow="COMPUTER VISION · INDUSTRY + ACADEMIA", title="Garment Measurement",
         desc="Measures garments from a live camera feed using pose keypoints and ChArUco calibration, retrained continuously.",
         metric="18", label="keypoint skeleton for long sleeve garments",
         chips=["YOLOv8 pose", "OpenCV", "PyQt", "MLflow", "GoPro"]),
    dict(id="voice", accent="gold", eyebrow="VOICE AI · REALTIME", title="Multilingual Voice Agents",
         desc="Booking and banking agents that talk in Sinhala, Tamil and English, with RAG, tool calls and self healing streams.",
         metric="3", label="languages: Sinhala · Tamil · English",
         chips=["Gemini Live", "React", "Node.js", "WebSockets", "FAISS"]),
    dict(id="smartdesk", accent="gold", eyebrow="IOT · DEVICE TO APP", title="Smart Desk Assistant",
         desc="An ESP32-S3 node streams air quality, noise and light over MQTT/TLS to a backend, a mobile app and AI insights.",
         metric="4", label="layers: firmware, cloud, API, mobile",
         chips=["ESP32-S3", "FreeRTOS", "MQTT", "PostgreSQL", "Expo"]),
    dict(id="hrms", accent="teal", eyebrow="BACKEND · MICROSERVICES", title="SmartForce HRMS",
         desc="An HR platform split into independent services for employees, payroll, leave, attendance, assets and projects.",
         metric="10", label="Spring Boot services",
         chips=["Java", "Spring Boot", "MongoDB", "REST APIs"]),
]


def card(c, theme):
    t = THEMES[theme]
    W, H = 480, 256
    acc = t[c["accent"]]
    other = t["teal" if c["accent"] == "gold" else "gold"]
    lines = wrap(c["desc"], 14.5, W - 60)
    assert len(lines) <= 2, (c["id"], lines)
    desc = "".join(
        f'<text class="desc" x="28" y="{110 + i * 21}">{escape(l)}</text>' for i, l in enumerate(lines)
    )
    metric_y = 172
    # chips, dropping from the end if they would overflow
    chips, cx = [], 28
    for ch in c["chips"]:
        w = est_width(ch, 12) + 20
        if cx + w > W - 24:
            break
        chips.append(
            f'<rect x="{cx:.1f}" y="206" width="{w:.1f}" height="24" rx="12" fill="{t["chip_bg"]}" stroke="{t["border"]}"/>'
            f'<text class="chip" x="{cx + w / 2:.1f}" y="222" text-anchor="middle">{escape(ch)}</text>'
        )
        cx += w + 7
    if c.get("live"):
        corner = (f'<circle class="pulse" cx="{W - 84}" cy="40" r="4" fill="{acc}"/>'
                  f'<circle cx="{W - 84}" cy="40" r="4" fill="{acc}"/>'
                  f'<text class="eye" x="{W - 28}" y="44" text-anchor="end">LIVE</text>')
    else:
        corner = f'<text class="arrow" x="{W - 26}" y="47" text-anchor="end">↗</text>'
    metric_w = est_width(c["metric"], 32) + 12
    alt = f'{c["title"]}: {c["desc"]} {c["metric"]} {c["label"]}.'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(alt)}">
<defs>
  <clipPath id="c"><rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14"/></clipPath>
  <linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{acc}"/><stop offset="1" stop-color="{other}" stop-opacity="0.15"/></linearGradient>
  <radialGradient id="glow" cx="100%" cy="0%" r="70%"><stop offset="0" stop-color="{acc}" stop-opacity="{t["glow_b"]}"/><stop offset="1" stop-color="{acc}" stop-opacity="0"/></radialGradient>
</defs>
<style>
  .eye{{font-family:{MONO};font-size:11.5px;font-weight:600;letter-spacing:1.6px;fill:{acc}}}
  .title{{font-family:{SANS};font-size:25px;font-weight:700;fill:{t["text"]}}}
  .desc{{font-family:{SANS};font-size:14.5px;fill:{t["muted"]}}}
  .metric{{font-family:{SANS};font-size:32px;font-weight:800;fill:{acc}}}
  .label{{font-family:{SANS};font-size:13px;fill:{t["muted"]}}}
  .chip{{font-family:{SANS};font-size:12px;font-weight:600;fill:{t["text"]}}}
  .arrow{{font-family:{SANS};font-size:20px;fill:{t["muted"]};animation:nudge 2.4s ease-in-out infinite}}
  @keyframes nudge{{0%,70%,100%{{transform:translate(0,0)}}85%{{transform:translate(2px,-2px)}}}}
  .pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 1.8s ease-out infinite}}
  @keyframes pulse{{0%{{transform:scale(1);opacity:.7}}100%{{transform:scale(3.2);opacity:0}}}}
  .sweep{{animation:sweep 3.5s ease-in-out infinite}}
  @keyframes sweep{{0%{{transform:translateX(-140px)}}60%,100%{{transform:translateX({W + 20}px)}}}}
  {REDUCED}
</style>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{t["panel"]}"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <rect width="{W}" height="4" fill="url(#bar)"/>
  <rect class="sweep" width="120" height="4" fill="{acc}" opacity="0.55"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="{t["border"]}"/>
<text class="eye" x="28" y="44">{escape(c["eyebrow"])}</text>
{corner}
<text class="title" x="28" y="80">{escape(c["title"])}</text>
{desc}
<text class="metric" x="28" y="{metric_y + 6}">{escape(c["metric"])}</text>
<text class="label" x="{28 + metric_w:.1f}" y="{metric_y}">{escape(c["label"])}</text>
{"".join(chips)}
</svg>
'''


# --------------------------------------------------------------------------- journey
JOURNEY = [
    ("2020 – 22", ["A/L Physical Science,", "Nalanda College", "People's Bank, teller & admin", "Speaker: ML & Automation"]),
    ("2023", ["easyPark IoT parking", "Sign language detection", "AIESEC team lead"]),
    ("2024", ["IEEE IES Secretary, UoK", "Robot Battle coordinator", "Sinhala ASR research starts"]),
    ("2025", ["Joined Surge Robotics", "Associate AI/ML Engineer", "Voice and WhatsApp agents"]),
    ("2026", ["WhatsApp AI agents in prod", "SICET 2026 paper", "IEEE GenAI Challenge talk", "BSc (Hons) completed"]),
]


def journey(theme):
    t = THEMES[theme]
    W, H = 1000, 250
    xs = [110 + i * 195 for i in range(len(JOURNEY))]
    ly = 86
    cols = []
    for i, ((year, lines), x) in enumerate(zip(JOURNEY, xs)):
        last = i == len(JOURNEY) - 1
        col = t["gold"] if last else t["teal"]
        texts = "".join(
            f'<text class="{"ev strong" if j == 0 else "ev"}" x="{x}" y="{ly + 44 + j * 22}" text-anchor="middle">{escape(l)}</text>'
            for j, l in enumerate(lines)
        )
        pulse = f'<circle class="pulse" cx="{x}" cy="{ly}" r="7" fill="{col}"/>' if last else ""
        cols.append(
            f'<g class="fade" style="animation-delay:{0.25 + i * 0.3:.2f}s">'
            f'<text class="year" x="{x}" y="{ly - 22}" text-anchor="middle" fill="{col}">{escape(year)}</text>'
            f'{pulse}<circle cx="{x}" cy="{ly}" r="7" fill="{t["panel"]}" stroke="{col}" stroke-width="3"/>'
            f'<circle cx="{x}" cy="{ly}" r="2.6" fill="{col}"/>{texts}</g>'
        )
    alt = "Journey: " + " | ".join(f"{y}: {', '.join(l)}" for y, l in JOURNEY)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(alt)}">
<defs><linearGradient id="ln" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="960" y2="0"><stop offset="0" stop-color="{t["teal"]}" stop-opacity="0.35"/><stop offset="0.8" stop-color="{t["teal"]}"/><stop offset="1" stop-color="{t["gold"]}"/></linearGradient></defs>
<style>
  .year{{font-family:{MONO};font-size:15px;font-weight:700;letter-spacing:1px}}
  .ev{{font-family:{SANS};font-size:13.5px;fill:{t["muted"]}}}
  .strong{{fill:{t["text"]};font-weight:600}}
  .draw{{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1.8s ease-out forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  .fade{{opacity:0;animation:fade .6s ease-out forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  .pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}}
  @keyframes pulse{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(2.6);opacity:0}}}}
  @media (prefers-reduced-motion: reduce){{*{{animation:none!important}} .fade{{opacity:1}} .draw{{stroke-dashoffset:0}}}}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}"/>
<path class="draw" pathLength="1" d="M40 {ly} H960" stroke="url(#ln)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
{"".join(cols)}
</svg>
'''


# --------------------------------------------------------------------------- loss chart
def loss_chart(theme):
    t = THEMES[theme]
    state = json.load(open(TRAINER_STATE))
    pts = [(h["step"], h["loss"]) for h in state["log_history"] if "loss" in h]
    max_step = state["max_steps"]
    epochs = state["num_train_epochs"]
    W, H = 1000, 360
    X0, X1, Y0, Y1 = 78, 960, 78, 290
    lo, hi = math.log10(0.07), math.log10(3.0)  # log scale: the useful part of the curve is below 0.5

    def sx(s):
        return X0 + (X1 - X0) * s / max_step

    def sy(v):
        v = min(max(v, 0.07), 3.0)
        return Y1 - (Y1 - Y0) * (math.log10(v) - lo) / (hi - lo)

    raw = " ".join(f"{sx(s):.1f},{sy(v):.1f}" for s, v in pts)
    ema, smooth = None, []
    for s, v in pts:
        ema = v if ema is None else 0.88 * ema + 0.12 * v
        smooth.append((s, ema))
    sm = "M" + " L".join(f"{sx(s):.1f},{sy(v):.1f}" for s, v in smooth)
    area = sm + f" L{sx(smooth[-1][0]):.1f},{Y1} L{sx(smooth[0][0]):.1f},{Y1} Z"

    grid = ""
    for v in (0.1, 0.2, 0.5, 1.0, 2.0):
        y = sy(v)
        grid += (f'<line x1="{X0}" x2="{X1}" y1="{y:.1f}" y2="{y:.1f}" stroke="{t["faint"]}"/>'
                 f'<text class="tick" x="{X0 - 12}" y="{y + 4:.1f}" text-anchor="end">{v:g}</text>')
    grid += f'<text class="tick" x="{X0 - 12}" y="{Y0 - 10}" text-anchor="end">log</text>'
    for s in (0, 5000, 10000, 15000, 20000):
        grid += f'<text class="tick" x="{sx(s):.1f}" y="{Y1 + 22}" text-anchor="middle">{s // 1000}k</text>'
    per_epoch = max_step / epochs
    for e in range(epochs):
        if e:
            x = sx(e * per_epoch)
            grid += f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{Y0 - 6}" y2="{Y1}" stroke="{t["border"]}" stroke-dasharray="4 5"/>'
        grid += f'<text class="tick" x="{sx((e + 0.5) * per_epoch):.1f}" y="{Y0 - 10}" text-anchor="middle">epoch {e + 1}</text>'

    s0, v0 = pts[0]
    s1, v1 = pts[-1]
    first, final = f"{v0:.2f}", f"{v1:.2f}"
    samples = round(per_epoch * state["train_batch_size"] / 1000)
    alt = (f"Training loss of Whisper large v2 with LoRA on Sinhala song audio falls from {first} to {final} "
           f"over {max_step:,} steps and {epochs} epochs.")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(alt)}">
<defs>
  <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["teal"]}" stop-opacity="0.22"/><stop offset="1" stop-color="{t["teal"]}" stop-opacity="0"/></linearGradient>
</defs>
<style>
  .title{{font-family:{SANS};font-size:17px;font-weight:700;fill:{t["text"]}}}
  .sub{{font-family:{SANS};font-size:13px;fill:{t["muted"]}}}
  .tick{{font-family:{MONO};font-size:11.5px;fill:{t["muted"]}}}
  .ann{{font-family:{MONO};font-size:13px;font-weight:700}}
  .draw{{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 2.6s cubic-bezier(.3,.6,.2,1) .2s forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  .late{{opacity:0;animation:fade .6s ease-out 2.6s forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  @media (prefers-reduced-motion: reduce){{*{{animation:none!important}} .draw{{stroke-dashoffset:0}} .late{{opacity:1}}}}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t["panel"]}" stroke="{t["border"]}"/>
<text class="title" x="{X0 - 40}" y="34">Training loss · Whisper large v2 + LoRA, Sinhala songs</text>
<line x1="{X1 - 300}" x2="{X1 - 278}" y1="29" y2="29" stroke="{t["teal"]}" stroke-width="2.6"/><text class="sub" x="{X1 - 270}" y="34">smoothed</text>
<line x1="{X1 - 186}" x2="{X1 - 164}" y1="29" y2="29" stroke="{t["muted"]}" stroke-opacity="0.5"/><text class="sub" x="{X1 - 156}" y="34">raw, every 25 steps</text>
{grid}
<polyline points="{raw}" fill="none" stroke="{t["muted"]}" stroke-opacity="0.45" stroke-width="1"/>
<path class="late" d="{area}" fill="url(#fill)"/>
<path class="draw" pathLength="1" d="{sm}" fill="none" stroke="{t["teal"]}" stroke-width="2.6" stroke-linejoin="round"/>
<circle cx="{sx(s0):.1f}" cy="{sy(v0):.1f}" r="4.5" fill="{t["gold"]}"/>
<text class="ann" x="{sx(s0) + 12:.1f}" y="{sy(v0) + 5:.1f}" fill="{t["gold"]}">{first}</text>
<g class="late"><circle cx="{sx(s1):.1f}" cy="{sy(v1):.1f}" r="4.5" fill="{t["gold"]}"/>
<text class="ann" x="{sx(s1) - 4:.1f}" y="{sy(v1) - 14:.1f}" text-anchor="end" fill="{t["gold"]}">{final} after {epochs} epochs</text></g>
<text class="sub" x="{X0 - 40}" y="{H - 18}">{max_step:,} steps · batch {state["train_batch_size"]} · about {samples}K clips per epoch · LoRA r=32, α=64 on q/v projections · logged in trainer_state.json</text>
</svg>
'''


for th in ("dark", "light"):
    write(f"header-{th}.svg", header(th))
    write(f"journey-{th}.svg", journey(th))
    write(f"whisper-loss-{th}.svg", loss_chart(th))
    for c in CARDS:
        write(f"cards/{c['id']}-{th}.svg", card(c, th))
print("ok")
