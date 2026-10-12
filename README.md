# Peephole math

Peephole math puts the viewer where the eyes are: household heights become
labeled eye levels and a second-viewer verdict, door thickness becomes the
right barrel length, and the hall's geometry becomes the span in view.

Live site: https://ilanis-agent.github.io/peepholemath/

## The three tools

- **Height plan** - eye level at a labeled 93% of height; a child eye level at
  or above the labeled 130 cm band shares the adult viewer, below it earns a
  second lower viewer.
- **Barrel plan** - door thickness in mm maps to labeled barrel ranges:
  standard 35-55, long 55-75, extra-long 75-100.
- **View plan** - distance x a labeled coverage ratio becomes the span in
  centimeters, read as a narrow slice, a workable view or a wide sweep.

## Limits

Every norm is labeled and illustrative. Posture, door construction and viewer
models move the real numbers; drilling is permanent, so measure the door and
check the manufacturer's range first.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (13 cases, 59 checks)

Run the tests: `python3 oracle.py && node test.js`
