**# Issues Found and Fixed**



**| Issue | Type | Line(s) | Description | Fix Approach |**

**|-------|------|---------|-------------|--------------|**

**| eval() on a string | Security (Bandit B307, Medium) | 39 | Executes arbitrary code passed in as `expr` | Replaced with `balance \* rate` using a numeric rate |**

**| os.system with string concatenation | Security (Bandit B605, High) | 55 | Shell command built from `filename`, allowing command injection | Removed the shell call and used `print` |**

**| Weak MD5 hash for PINs | Security (Bandit B324, High) | 44 | MD5 is broken and unsuitable for security | Switched to SHA-256 |**

**| Hardcoded admin token, printed to console | Security (Bandit B105, Low) | 59, 67 | Secret stored in source and leaked in output | Read from the `BANK\_ADMIN\_TOKEN` environment variable; print only whether it is set |**

**| random for PIN generation | Security (Bandit B311, Low) | 48 | `random` is predictable | Used `secrets.randbelow` |**

**| Bare except with pass | Bug (Bandit B110, Flake8 E722, Pylint W0702) | 22-23 | Silently hides all errors, so a failed deposit looks successful | Explicit account check; returns True/False |**

**| Mutable default argument | Bug (Pylint W0102) | 11 | `transactions=\[]` is shared across calls | Default to `None` and create a new list inside |**

**| File opened without `with` or encoding | Bug (Pylint R1732, W1514) | 52-54 | File may not close on error; platform-dependent encoding | Used `with open(..., encoding="utf-8")` |**

**| Missing docstrings, camelCase name | Style (Pylint C0116, C0103) | 11, 19, 26, 37, 43, 47, 51, 58 | No documentation; `createAccount` breaks snake\_case | Added docstrings; renamed to `create\_account` |**

**| Unused import and variables | Style (Pylint W0611/W0612, Flake8 F401/F841) | 6, 27, 38 | `sys`, `service\_fee` and `bal` are never used | Removed them |**

**| Comparison to None with == | Style (Flake8 E711, Pylint C0121) | 28 | Should use identity check | Changed to `is None` |**

**| Line too long, no final newline | Style (Flake8 E501, W292) | 15, 70 | Exceeds 79 characters; file does not end with a newline | Wrapped the f-string; added the final newline |**

**| Unnecessary else after return | Style (Pylint R1705) | 30-34 | Redundant nesting | Removed the else |**



**## Results**

**- Pylint: 5.62/10 before, 10.00/10 after**

**- Bandit: 6 issues (2 High, 1 Medium, 3 Low) before, 0 after**

**- Flake8: 7 issues before, 0 after**



**## Bugs the tools did not flag**

**- `withdraw` defined a service fee but never charged it (removed the unused variable).**

**- The admin token was printed to the console.**

**- `deposit`, `withdraw` and `create\_account` accept negative amounts.**

