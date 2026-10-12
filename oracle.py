import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def height_plan(adultHeightCm, childHeightCm):
    if not (adultHeightCm > 0): return {"error": "adult height must be positive"}
    adultEye = round1(adultHeightCm * 0.93)
    if not (childHeightCm > 0):
        return {"adultEye": adultEye, "childEye": None, "viewers": 1, "verdict": "one viewer at adult eye level on the labeled band"}
    childEye = round1(childHeightCm * 0.93)
    if childEye >= 130:
        return {"adultEye": adultEye, "childEye": childEye, "viewers": 1, "verdict": "one viewer serves both on the labeled band"}
    return {"adultEye": adultEye, "childEye": childEye, "viewers": 2, "verdict": "fit a second lower viewer on the labeled band"}

def barrel_plan(doorMm):
    if not (doorMm > 0): return {"error": "door thickness must be positive"}
    if doorMm < 35: return {"error": "thinner than the labeled barrel range"}
    if doorMm > 100: return {"error": "thicker than the labeled barrel range"}
    if doorMm <= 55: barrel = "standard"
    elif doorMm <= 75: barrel = "long"
    else: barrel = "extra-long"
    return {"barrel": barrel, "verdict": barrel + " barrel on the labeled range"}

def span_plan(distanceCm, ratio):
    if not (distanceCm > 0) or not (ratio > 0):
        return {"error": "distance and ratio must be positive"}
    span = round1(distanceCm * ratio)
    if span < 40: verdict = "a narrow slice on the labeled ratio"
    elif span < 90: verdict = "a workable view on the labeled ratio"
    else: verdict = "a wide sweep on the labeled ratio"
    return {"span": span, "verdict": verdict}

def render_height(r, adultHeightCm, childHeightCm):
    if r["childEye"] is None:
        return "Adult eye level lands at a labeled " + fmt(r["adultEye"]) + " cm - " + r["verdict"] + "."
    return ("Adult eye level lands at a labeled " + fmt(r["adultEye"]) + " cm, child eye level at "
            + fmt(r["childEye"]) + " cm - " + r["verdict"] + ".")

def render_barrel(r, doorMm):
    return "A door " + fmt(doorMm) + " mm thick takes the " + r["verdict"] + "."

def render_span(r, distanceCm, ratio):
    return ("Standing " + fmt(distanceCm) + " cm back with a labeled " + fmt(ratio)
            + " coverage ratio, the viewer takes in " + plural(r["span"], "centimeter", "centimeters")
            + " of span - " + r["verdict"] + ".")

cases = []
for a in [(175, 120), (175, 145), (175, 0), (0, 120)]:
    r = height_plan(*a)
    cases.append({"fn": "heightPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_height(r, *a)})
for a in [(40,), (60,), (90,), (30,), (120,)]:
    r = barrel_plan(*a)
    cases.append({"fn": "barrelPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_barrel(r, *a)})
for a in [(100, 0.4), (60, 0.4), (250, 0.4), (0, 0.4)]:
    r = span_plan(*a)
    cases.append({"fn": "spanPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_span(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
