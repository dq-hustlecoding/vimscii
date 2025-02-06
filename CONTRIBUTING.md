# Contributing to VIMSCII

First off, thank you for considering contributing to VIMSCII! It's people like you that make VIMSCII such a great tool.

## How Can I Contribute?

### Adding New Stages

1. Create a new `.txt` file in the appropriate category under `stages/`
   ```
   stages/
   ├── basic/
   ├── animals/
   ├── objects/
   └── advanced/
   ```

2. Stage File Guidelines:
   - Keep ASCII art reasonable in size (max 20x20 recommended)
   - Use basic ASCII characters for better compatibility
   - Test your stage before submitting
   - File name should be descriptive (e.g., `simple_house.txt`, `cat.txt`)

3. Example Stage Format:
   ```
   # Name: Simple Triangle
   # Category: Basic
   # Difficulty: Beginner
   # Estimated Time: 30s
   
     /\
    /  \
   /____\
   ```

### Code Contributions

1. Set up your environment:
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/vimscii.git
   cd vimscii

   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Code Style Guidelines:
   - Follow PEP 8 guidelines
   - Use meaningful variable and function names
   - Add comments for complex logic
   - Include docstrings for functions and classes

4. Testing:
   - Test your changes thoroughly
   - Ensure all existing tests pass
   - Add new tests if needed

### Submitting Changes

1. Push your changes to your fork
2. Create a Pull Request with a clear description
3. Link any relevant issues
4. Wait for review and address any feedback

## Pull Request Process

1. Update the README.md if needed (e.g., new features, changed commands)
2. Update the documentation if you're changing functionality
3. The PR will be merged once you have the sign-off of at least one maintainer

## Creating Issues

### Bug Reports
- Use the bug report template
- Include clear reproduction steps
- Provide your environment details
- Add screenshots if applicable

### Feature Requests
- Use the feature request template
- Clearly describe the problem you're solving
- Suggest a solution if you have one
- Consider alternatives

### New Stage Suggestions
- Use the new stage template
- Include the ASCII art
- Specify difficulty level
- Suggest category placement

## Community

- Be respectful and inclusive
- Help others when you can
- Stay focused on the project goals

## Questions?

- Check existing issues and discussions first
- Open a new discussion if you can't find an answer
- Join our community chat (if available)

Thank you for contributing to VIMSCII! 🎯