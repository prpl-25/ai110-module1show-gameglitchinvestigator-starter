# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game was straightforward, I enter a guess and the game prompts me to either go higher or lower to find the secret number. The developer debug info is used to understand if the logic is working correctly.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints were not accurate. The secret number for 43 but it kept telling me to go higher when it should have told me to go lower.
  2. The new game button does not work. After playing one game, I was not able to restart and play a new game. I had to refresh to play a new game.
  3. The hints are backwards - for a guess that is lower than the number, it tells me to go lower and for a guess that's higher than the number it tells me to higher.
  4. The hard difficulty level is easier than normal as it considers lesser numbers. It only considers numbers 1-50.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 - I used Claude Code to inspect, debug, and fix this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggested I swap the hints in "check_guess()" for when the guess is lesser than and greater than the secret number to fix the backward hints bug. I verified that the return statements were incorrect and tested the application after the fix to see if it fixed the bug, and it did.
  - Another bug I fixed was the swapped difficulty levels of "hard" and "normal". I interchanged the ranges so "normal" has 1-50 and "hard" has 1-100.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
 - Created pytest cases and ran all of them. If all tests passed, the bug is fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
 - Ran a test to check if check_guess(40, 50) returns "too low"
- Did AI help you design or understand any tests? How?
 - Yes, AI helped design the pytest cases and also explain te functionality. It also refactored logic_utils to have all the functions so the pytest cases can be run successfully.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


## TF hint
- To help guide students better, I would 