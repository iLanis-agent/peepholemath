(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function heightPlan(adultHeightCm, childHeightCm) {
    if (!(adultHeightCm > 0)) return { error: "adult height must be positive" };
    var adultEye = round1(adultHeightCm * 0.93);
    if (!(childHeightCm > 0)) return { adultEye: adultEye, childEye: null, viewers: 1, verdict: "one viewer at adult eye level on the labeled band" };
    var childEye = round1(childHeightCm * 0.93);
    if (childEye >= 130) return { adultEye: adultEye, childEye: childEye, viewers: 1, verdict: "one viewer serves both on the labeled band" };
    return { adultEye: adultEye, childEye: childEye, viewers: 2, verdict: "fit a second lower viewer on the labeled band" };
  }

  function barrelPlan(doorMm) {
    if (!(doorMm > 0)) return { error: "door thickness must be positive" };
    if (doorMm < 35) return { error: "thinner than the labeled barrel range" };
    if (doorMm > 100) return { error: "thicker than the labeled barrel range" };
    var barrel;
    if (doorMm <= 55) barrel = "standard";
    else if (doorMm <= 75) barrel = "long";
    else barrel = "extra-long";
    return { barrel: barrel, verdict: barrel + " barrel on the labeled range" };
  }

  function spanPlan(distanceCm, ratio) {
    if (!(distanceCm > 0) || !(ratio > 0)) return { error: "distance and ratio must be positive" };
    var span = round1(distanceCm * ratio);
    var verdict;
    if (span < 40) verdict = "a narrow slice on the labeled ratio";
    else if (span < 90) verdict = "a workable view on the labeled ratio";
    else verdict = "a wide sweep on the labeled ratio";
    return { span: span, verdict: verdict };
  }

  function renderHeight(r, adultHeightCm, childHeightCm) {
    if (r.childEye === null) return "Adult eye level lands at a labeled " + r.adultEye + " cm - " + r.verdict + ".";
    return "Adult eye level lands at a labeled " + r.adultEye + " cm, child eye level at " + r.childEye + " cm - " + r.verdict + ".";
  }

  function renderBarrel(r, doorMm) {
    return "A door " + doorMm + " mm thick takes the " + r.verdict + ".";
  }

  function renderSpan(r, distanceCm, ratio) {
    return "Standing " + distanceCm + " cm back with a labeled " + ratio + " coverage ratio, the viewer takes in " + plural(r.span, "centimeter", "centimeters") + " of span - " + r.verdict + ".";
  }

  var api = { heightPlan: heightPlan, barrelPlan: barrelPlan, spanPlan: spanPlan, renderHeight: renderHeight, renderBarrel: renderBarrel, renderSpan: renderSpan };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.PeepholeMath = api;
})(this);
