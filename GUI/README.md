# GUI

Desktop applications built with Tkinter and PyQt5.

## Prerequisites

```bash
pip install -e ".[gui]"
```

> **Note:** Tkinter is bundled with Python on Windows and macOS. On Linux:
> ```bash
> sudo apt-get install python3-tk
> ```

## Scripts

| Script | Description | Run |
|--------|-------------|-----|
| `todo.py` | Feature-rich To-Do List manager with JSON persistence | `python todo.py` |
| `clock.py` | Analogue clock with Tkinter Canvas | `python clock.py` |
| `notepad.py` | Basic text editor | `python notepad.py` |
| `paint.py` | Drawing/paint application | `python paint.py` |
| `file_explorer.py` | Tkinter file explorer | `python file_explorer.py` |
| `A_basic_gui_calculator.py` | GUI calculator | `python A_basic_gui_calculator.py` |
| `tick_cross.py` | Tic Tac Toe (GUI) | `python tick_cross.py` |
| `snake_ladder.py` | Snake and Ladder board game | `python snake_ladder.py` |
| `youtube_download.py` | YouTube video downloader | `python youtube_download.py` |
| `spelling.py` | Spell checker with suggestions | `python spelling.py` |
| `spinner.py` | Fidget spinner animation | `python spinner.py` |
| `Quiz.py` | Interactive quiz application | `python Quiz.py` |
| `Form.py` | Data entry form | `python Form.py` |
| `clender.py` | GUI calendar | `python clender.py` |
| `search_applications.py` | Search installed applications | `python search_applications.py` |
| `graphics.py` | Turtle graphics patterns | `python graphics.py` |
| `Pikachu.py` | Pikachu drawn with Turtle | `python Pikachu.py` |
| `doraemon.py` | Doraemon drawn with Turtle | `python doraemon.py` |
| `rainbow.py` | Rainbow drawn with Turtle | `python rainbow.py` |
| `happy_birth_day.py` | Birthday message animation | `python happy_birth_day.py` |

## Running Tests

```bash
pytest ../tests/test_gui/ -v
```
