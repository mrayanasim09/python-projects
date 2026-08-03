# Changelog

All notable changes to the python-projects repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Production-grade package configuration with `pyproject.toml` and `setup.cfg`
- Pre-commit hooks for code quality automation
- Comprehensive CI/CD workflow for testing, linting, and security scanning
- Unit tests for Utilities module (24 test cases)
- Development guide documentation
- Proper package structure with `__init__.py` files including version info and `__all__` exports
- `.pre-commit-config.yaml` with Black, isort, Flake8, Bandit, and MyPy hooks
- GitHub Actions workflow for multi-Python version testing
- MANIFEST.in for proper package distribution
- Enhanced `.gitignore` for Python projects

### Fixed
- Corrected typos in module imports across all `__init__.py` files:
  - `brithday` → `birthday`
  - `broswer` → `browser`
  - `insta` → `inta`
  - `secert_code` → `secret_code`
- Updated import statements from bare `import` to proper relative imports (`from .module import *`)

### Changed
- Improved import structure in all package `__init__.py` files
- Enhanced documentation with DEVELOPMENT.md guide
- Updated requirements.txt with pinned secure versions

## [1.0.0] - 2024

### Added
- Initial release with 80+ Python projects
- Five main categories: Calculator, Game, GUI, Utilities, Machine Learning
- Comprehensive documentation (README, CONTRIBUTING, FAQ, etc.)
- Multiple CI/CD workflows (15+ GitHub Actions)
- CircleCI integration
- DeepSource code quality integration
- Community support channels (Discord, Reddit, LinkedIn)
- Security scanning with Bandit and Codacy
- Automated code formatting with Black
- Dependency management with Dependabot

### Project Categories

#### Calculator (18 projects)
- Mega Calculator, Quadratic Equation Solver, BMI Calculator
- Stock Analyzer, Special Relativity Calculator
- Number Base Converter, Integration/Differentiation
- Time converters, Grade Calculator, Sudoku Solver
- Mortgage Calculator, Roman Numeral Converter, ASCII Value Finder

#### Games (16 projects)
- Snake Game, Hangman, Tic Tac Toe (GUI & Terminal)
- 2048 Blocks, Master Mind, Color Guessing
- Twenty-One, Rock Paper Scissors, Dice Rolling
- Number Guessing, Typing Speed Test, Star Patterns

#### GUI (21 projects)
- Form applications, Calculators, Clocks
- Games: Tic Tac Toe, Snake & Ladder, Quiz
- Creative: Paint app, Turtle graphics (Pikachu, Doraemon, Rainbow)
- Tools: Notepad, File Explorer, YouTube Downloader, Todo List
- Calendar, Application Search, Birthday Message Generator

#### Machine Learning (11 projects)
- Computer Vision: Eye Blink Detection, Hand Gesture Brightness Control
- NLP: Text-to-Speech, Language Detector, Sentiment Analysis, Spam Detection
- Prediction: Crypto Price, Gold Price (Prophet library)
- Image Processing: Image to Sketch
- Tools: Phone Camera on PC

#### Utilities (22 projects)
- Network: WiFi Password Retriever, Site Connectivity Checker
- Web: Browser automation, Google Search, Instagram Info, GitHub API
- Security: Password Manager, Password Generator, Hash Cracker, Secret Code
- Tools: Countdown Timer, QR Code Generator, WhatsApp Spam Sender
- File Transfer via QR, Word/Letter Counter, Short Form Generator
- Birthday Finder (zodiac, birthstone, life path number)

### Technical Stack
- **GUI**: pygame, pyqt5, pyqtwebengine, tkcalendar, pillow
- **ML/AI**: opencv-python, mediapipe, prophet, seaborn, scikit-learn
- **Web**: requests, googlesearch-python, instaloader, pytube
- **Utilities**: qrcode, pyautogui, pyttsx3, pyshorteners
- **Math/Science**: matplotlib, sympy, numpy, openpyxl, yfinance
- **NLP**: textblob, vaderSentiment, langdetect, nltk

### Documentation
- README.md - Comprehensive project overview
- CONTRIBUTING.md - Contribution guidelines
- CODE_OF_CONDUCT.md - Community standards
- SECURITY.md - Vulnerability reporting
- FAQ.md - Common questions
- SUMMARY.md - Quick summary
- How_to_use.md - Installation and usage
- prerequisites.md - System requirements
- PULL_REQUEST_TEMPLATE.md - PR template

### Known Issues
- Some modules may require Python 3.10+ compatibility verification
- Limited test coverage (only Utilities module tested initially)
- Some external dependencies may require API keys or authentication

---

## Version History

- **1.0.0** - Initial production-ready release with comprehensive improvements
- **0.x.x** - Development versions (pre-release)

---

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
