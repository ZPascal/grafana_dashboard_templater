# Contributing

We welcome contributions! Here's how to get started.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/ZPascal/grafana_dashboard_templater.git
cd grafana_dashboard_templater
```

2. Install in development mode:
```bash
pip install ".[dev]"
```

## Running Tests

Run the test suite:

```bash
python3 -m unittest discover tests
```

### Test Coverage

We maintain 100% test coverage. When adding features or fixing bugs, include tests:

```bash
pytest tests/ --cov=grafana_dashboard --cov-report=html
```

## Code Quality

### Linting

We use ruff for code quality checks. Before committing:

```bash
ruff check .
```

Fix any issues reported by ruff.

### Style Guide

- Follow PEP 8
- Use meaningful variable and function names
- Add docstrings to public functions and classes
- Keep functions small and focused

## Documentation

- Update docstrings when changing public APIs
- Add examples to demonstrate new features
- Keep the [Examples](examples/index.md) section current

## Submitting Changes

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes and commit with clear messages
3. Push to your fork: `git push origin feature/my-feature`
4. Open a Pull Request with a clear description

## PR Requirements

- All tests must pass
- Code coverage must remain at 100%
- Ruff linting checks must pass
- Documentation must be updated
- Commits should be clear and atomic

## Questions?

If you have questions, feel free to open an issue or reach out to the maintainers.

Thank you for contributing!
