**# Reflection**



**\*\*1. Which issues were the easiest and hardest to fix?\*\***

**The style issues (unused imports, `== None`, missing newline) were easiest because the tools name the exact line. The hardest was `eval()` in `compute\_bonus`. I could not just delete it; I had to change the function to take a numeric rate instead of an expression string, and update the caller.**



**\*\*2. Did the tools report any false positives?\*\***

**The hardcoded-password warning (B105) was only partly accurate, as it was a demo token rather than a real password, but keeping secrets in source code is a real risk, so fixing it was still right. Overall the findings were valid.**



**\*\*3. How would you integrate static analysis into your development workflow?\*\***

**Run Flake8 and Pylint locally or as a pre-commit hook, and run all three tools in a CI pipeline (for example GitHub Actions) on every pull request, failing the build on Bandit High issues or a low Pylint score.**



**\*\*4. What improvements did you see in code quality, readability and security?\*\***

**The Pylint score went from 5.62 to 10.00 and Bandit went from 6 findings to none. The code is easier to read thanks to docstrings and consistent naming, and it is more robust: no silent error swallowing, no shared mutable default, and the file is closed safely. It is more secure: no `eval`, no shell command, a stronger hash, a secure random source and no hardcoded secret.**

