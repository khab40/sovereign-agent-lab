# Week 1 Submission Checklist

- [X] Fork `sovereign-agent-lab` and clone my fork
- [X] Create `.env` from `.env.example`
- [X] Add `NEBIUS_KEY` to `.env`
- [X] Add `RASA_PRO_LICENSE` to `.env` for Exercise 3
- [X] Run `make install`
- [X] Run `make smoke`
- [X] Run `make test` - failure!

## Exercise 1

- [X] Run `make ex1`
- [X] Check `week1/outputs/ex1_results.json` was created
- [X] Fill `week1/answers/ex1_answers.py`
- [X] Run `make grade-ex1`

## Exercise 2

- [X] Run `make ex2-a`
- [X] Implement `generate_event_flyer` in `sovereign_agent/tools/venue_tools.py`
- [X] Run `make test`
- [X] Run `make ex2-b`
- [X] Run `make ex2-c`
- [X] Run `make ex2-d`
- [X] Check `week1/outputs/ex2_results.json` was created
- [X] Fill `week1/answers/ex2_answers.py`
- [X] Run `make grade-ex2`

## Exercise 3

- [X] Run `make install-rasa`
- [X] Run `make ex3-train`
- [X] In terminal 1 run `make ex3-actions`
- [X] In terminal 2 run `make ex3-chat`
- [X] Complete happy-path conversation
- [X] Complete over-limit deposit conversation
- [X] Complete out-of-scope conversation
- [X] Paste real traces into `week1/answers/ex3_answers.py`
- [X] Uncomment Task B cutoff guard in `exercise3_rasa/actions/actions.py`
- [X] Run `make ex3-retrain`
- [X] Restart `make ex3-actions`
- [X] Rerun `make ex3-chat` and test cutoff guard
- [X] Finish `week1/answers/ex3_answers.py`
- [X] Run `make grade-ex3`

## Exercise 4

- [X] Run `make ex4`
- [X] Check `week1/outputs/ex4_results.json` was created
- [X] Edit `sovereign_agent/tools/mcp_venue_server.py`: change `The Albanach` from `available` to `full`
- [X] Run `make ex4` again and compare results
- [X] Revert the MCP change
- [X] Fill `week1/answers/ex4_answers.py`
- [X] Run `make grade-ex4`

## Final Submission

- [X] Run `make grade`
- [X] Run `make check-submit`
- [X] Confirm these exist:
- [X] `week1/outputs/ex1_results.json`
- [X] `week1/outputs/ex2_results.json`
- [X] `week1/outputs/ex4_results.json`
- [X] Confirm all `week1/answers/*.py` files are filled in
- [X] Confirm `generate_event_flyer` is implemented
- [X] Confirm the Exercise 3 cutoff guard is uncommented
- [X] Push my fork
- [X] Submit my fork URL in the course portal
