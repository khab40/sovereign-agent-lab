"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  I’m calling to confirm tonight’s booking.
How many guests are you confirming for tonight's event?
Your input ->  120 guests.
And how many of those guests will need vegan meals?
Your input ->  20.
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  250 pounds.
Thank you — booking confirmed. 120 guests, 20 requiring vegan meals, £250 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->  /stop
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  I’m calling to confirm tonight’s booking.
How many guests are you confirming for tonight's event?
Your input ->  120.
And how many of those guests will need vegan meals?
Your input ->  20.
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  350 pounds.
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £350 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
Your input ->  /stop
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "Deposit is too high, 300 pounds is the limit"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  I’m calling to confirm tonight’s booking.
How many guests are you confirming for tonight's event?
Your input ->  120.
And how many of those guests will need vegan meals?
Your input ->  Before that, is there parking nearby?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->  Do you have AV equipment?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->    /stop
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM answered that it was not trained to help with these out of scope questions.
Suggested to contact event organizer directly.
Still was ready to answer on relevant questions.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM handles the out-of-scope request by explicitly deflecting it into a separate flow and giving a narrow,
policy-safe response. That makes the behaviour predictable and auditable.
In Exercise 2 Scenario 3, the LangGraph agent was more open-ended: it reasoned through the problem,
explored alternatives, and could explain failure.
So CALM is stricter and safer for boundary enforcement, while LangGraph is more flexible for ambiguous or broader tasks.
CALM was locally less helpful, but globally safer because the system’s job is booking confirmation, not general event support.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Changed now.hour > 16 or (now.hour == 16 and now.minute >= 45) to True, run re-train command, made re-test with server and chat client.
New Guard was triggered and agent gave expected response about cutoff time.
Testing by forcing the cutoff proves the guard branch works, but a fuller test should check before-cutoff, exactly-at-cutoff, after-cutoff, and timezone behavior.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
CALM removes a lot of the old Rasa plumbing. Instead of writing intent examples, regex-style slot parsing,
and many dialogue rules, the LLM now handles flow selection and extracts values like guest counts from natural speech.
Python still handles the important deterministic part: business rules such as capacity, deposit limit, vegan ratio,
and cutoff time. That is necessary because those checks must be auditable and guaranteed.
The gain is much simpler development and more natural language flexibility.
The cost is that some understanding steps are now probabilistic, so I trusted the old rule-based approach more
for exact classification and parsing, even though it required much more setup.
CALM reduces boilerplate, but failures may be harder to debug because slot extraction and flow selection depend on LLM behavior.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM still has noticeable setup cost: multiple Rasa config files, model training, an action server, two terminals,
and a Rasa Pro licence.
That is more overhead than LangGraph, which is much faster to wire together for open-ended tasks.
However, the setup buys controlled behaviour. The CALM agent is not supposed to improvise broadly, invent new workflows,
or call tools outside the defined flow structure.
For the booking confirmation use case, that restriction is a feature, not a weakness, because the goal is reliability,
auditable behaviour, and strict enforcement of business rules rather than creative autonomy.
The extra setup buys operational guarantees: auditable flow boundaries, repeatable business-rule enforcement, and safer behavior under out-of-scope inputs.
"""
