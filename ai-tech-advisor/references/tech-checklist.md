# Technology Evaluation Checklist

Use this checklist when evaluating each technology in the recommended stack.

## Required Checks

| # | Check | How to Verify | Pass Criteria |
|---|-------|--------------|---------------|
| 1 | Community Size | GitHub stars, npm/PyPI downloads, Stack Overflow | > 5k stars OR > 100k monthly downloads |
| 2 | Active Maintenance | Last commit, last release, open issues | Last release within 6 months |
| 3 | Documentation | Official docs exist, complete, with examples | Covers all major features |
| 4 | License | Check LICENSE file or registry | Allows commercial use (MIT, Apache 2.0, BSD) |
| 5 | AI Compatibility | Well-represented in AI training data | Major frameworks pass automatically |
| 6 | Learning Curve for AI | Can AI generate correct code without frequent errors | Clear conventions AI can follow |
| 7 | Ecosystem | Mature companion libraries exist | UI libs, testing tools, ORMs available |
| 8 | Chinese Resources | Chinese docs, tutorials, community | At least some Chinese documentation |

## Risk Levels

- **LOW:** All checks pass — proceed confidently
- **MEDIUM:** 1-2 checks fail — note risks, proceed with mitigation
- **HIGH:** 3+ checks fail — strongly recommend alternative

## Quick Verification Commands

**npm packages:**
```
npm view [name] version        # Latest version
npm view [name] license        # License
npm view [name] description    # What it does
```

**Python packages:**
```
pip show [name]                # Version, license, description
```

**GitHub:** Check stars, recent commits, open issues at github.com/[org]/[name]
