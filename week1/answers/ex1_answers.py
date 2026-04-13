"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
In Part A, all three prompt formats produced correct answers, but they did not produce the same venue. The plain format returned The Haymarket Vaults, while the XML and sandwich formats returned The Albanach. Since both venues satisfy the assignment constraints, all three outputs were still valid. What I observed is that prompt structure changed which acceptable answer the model selected, even though it did not change correctness on this cleaner baseline dataset.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
No, both of them did not bring a wrong answer in this experiment. The Holyrood Arms is more likely to cause a wrong answer because it looks almost fully correct at a glance: capacity 160 and vegan yes both match the request, and only the status=full field makes it invalid.
"""
# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C ran because the larger model stayed correct in both Part A and Part B, so the script switched to the smaller 8B model to see whether the formatting effect would become visible there. In my run, Part C was also correct for PLAIN, XML, and SANDWICH, all returning The Haymarket Vaults. That means the smaller model still handled this prompt successfully, so my results do not show a clear formatting advantage here. The main conclusion is that this particular dataset remained easy enough that even the smaller model could isolate the correct venue despite the distractors.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the model has to pick the correct answer from 
several similar-looking options, especially when distractors are close to being valid. 
In those situations, structure helps the model separate constraints more clearly and 
reduces the chance of shallow pattern matching. In my run, formatting did not change 
correctness on the clean dataset, but it did change which valid answer was selected, 
which shows that presentation still influences model behaviour even when accuracy stays high.
"""

