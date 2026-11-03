# Python Games

Three small command-line games for practicing Python fundamentals.

## What problem did I work on?

I used short games to practice reading input, validating choices, generating random values, and keeping score across repeated rounds.

## Games

- `number_guesser.py`: choose a positive upper limit, then guess the random number with higher/lower hints.
- `quiz_game.py`: answer four computer-hardware questions and receive a score and percentage.
- `rock_paper_scissors.py`: play repeated rounds against random computer choices and quit with Q. Ties do not change either score.

## Run locally

Requires Python 3. No external packages are needed.

```bash
python number_guesser.py
python quiz_game.py
python rock_paper_scissors.py
```

## How do I know it works?

Automated tests control user input and the random generator. They verify guessing hints and the attempt count, quiz scoring, a tied round, and winning/losing rounds.

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the same tests. These are small learning programs with terminal interaction; scores are not stored after a process exits.
