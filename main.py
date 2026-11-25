import os

JOKE = "I told the broccoli to stop stalking me — it said it was just branching out."

# Gate self-check (1-140 chars, single line, no leading/trailing whitespace):
# the entry text itself is unchanged by this check.
assert 1 <= len(JOKE) <= 140 and "\n" not in JOKE and JOKE.strip() == JOKE

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
