# VIMSCII 🎯
> Master Vim commands while creating ASCII art!

VIMSCII is a terminal-based game that helps you practice Vim commands while creating ASCII art. Race against time, perfect your Vim skills, and compete with your own records!

## Features

⌨️ Authentic Vim-like interface and commands  
🎨 Create ASCII art with familiar Vim controls  
⚡ Challenge yourself with time trials  
🏆 Local record tracking system  
🎮 Expandable stages through simple text files

## Installation

1. Set up a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the game:
```bash
python src/game.py
```

### How to Play

1. Select a stage from the menu
2. Create the ASCII art shown on the right side
3. Use Vim commands to edit and navigate
4. Submit your work with `:wq` when ready
5. Beat your previous records!

### Controls

#### Mode Switching
- `ESC` - Enter Normal mode
- `i` - Enter Insert mode
- `:` - Enter Command mode

#### Navigation (Normal Mode)
- `h` - Move left
- `j` - Move down
- `k` - Move up
- `l` - Move right

#### Commands
- `:wq` - Submit your work (saves only if correct)
- `:q!` - Quit without saving

### Records

Your completion times are automatically saved in `vimscii_records.txt` with the following format:
```
2024-02-06 15:30:22 | Triangle | 12.45s
```

## Project Structure

```
vimscii/
├── src/
│   ├── game.py          # Main game logic
│   ├── stage.py         # Stage management
│   └── records.py       # Record keeping
├── stages/              # ASCII art stages
│   └── basic/
│       └── triangle.txt
└── requirements.txt
```

## Contributing

### Adding New Stages

1. Create a new `.txt` file in an appropriate category under `stages/`
2. Add your ASCII art
3. Test the stage by playing it
4. Submit a pull request

### Stage Guidelines

- Keep ASCII art reasonable in size (max 20x20 recommended)
- Use basic ASCII characters for better compatibility
- Test your stage thoroughly before submitting
- Consider the difficulty level when choosing a category

### Code Style

This project uses [Black](https://github.com/psf/black) for code formatting. Please ensure your code adheres to the Black style guidelines.

To format your code, run:

```bash
pip install black
black .
```

Or, to check which files need formatting without applying changes:

```bash
black --check .
```

You can also configure your editor to run Black automatically on save. For VS Code, add the following to your `settings.json`:

```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

## Development

The game is built with:
- [blessed](https://github.com/jquast/blessed) for terminal UI
- Pure Python for game logic
- Text files for stage storage and record keeping

## Roadmap

- [ ] Additional Vim commands (dd, yy, etc.)
- [ ] More complex ASCII art stages
- [ ] Stage categories by difficulty
- [ ] Stage completion statistics
- [ ] Time-based achievements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Vim and the ASCII art community
- Built with [blessed](https://github.com/jquast/blessed) library
- Thanks to all ASCII art contributors