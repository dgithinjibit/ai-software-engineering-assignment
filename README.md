# AI in Software Engineering - Practical Assignment

This repository contains the complete implementation of the AI in Software Engineering assignment, demonstrating practical applications of AI tools in modern software development workflows.

## Project Overview

This assignment explores three key areas:
1. **AI-Powered Code Completion**: Comparing manual vs AI-assisted code implementations
2. **Automated Testing with AI**: Building intelligent test automation frameworks
3. **Predictive Analytics**: Using machine learning for resource allocation

## Repository Structure

```
.
├── task1_code_completion/       # Code completion comparison
├── task2_automated_testing/     # Selenium test automation
├── task3_predictive_analytics/  # ML predictive model
├── part3_ethical_reflection/    # Ethics discussion
├── bonus_task/                  # Innovation proposal
├── huggingface_space/          # Interactive demo
└── docs/                        # Documentation
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Chrome/Chromium browser (for Task 2)
- Git

### Installation

1. Clone the repository:
```bash
git clone
cd directory
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Individual Tasks

#### Task 1: Code Completion
```bash
cd task1_code_completion
python sorting_comparison.py
```

#### Task 2: Automated Testing
```bash
cd task2_automated_testing
python login_test_automation.py
```

#### Task 3: Predictive Analytics
```bash
cd task3_predictive_analytics
python predictive_model.py
```

### Running the Hugging Face Space

```bash
cd huggingface_space
python app.py
```

Then open your browser to `http://localhost:7860`

## Tasks Breakdown

### Task 1: AI-Powered Code Completion (20%)
- Manual vs AI sorting implementation
- Performance benchmarking
- Efficiency analysis (200 words)

**Key Findings**: AI-suggested implementation using Python's built-in `sorted()` is 100-150x faster than manual bubble sort for datasets of 1000+ items.

### Task 2: Automated Testing with AI (20%)
- Selenium-based login test automation
- Valid/invalid credential testing
- AI-enhanced test coverage analysis (150 words)

**Key Findings**: Automated testing achieves 100% repeatability and 4-5x faster execution compared to manual testing.

### Task 3: Predictive Analytics (20%)
- Random Forest classifier for priority prediction
- Breast cancer dataset adaptation
- Model evaluation (accuracy, F1-score)

**Key Results**:
- Accuracy: ~85-90%
- F1-Score (Macro): ~0.85
- Feature importance analysis included

### Part 3: Ethical Reflection (10%)
Discussion of:
- Dataset biases
- Fairness considerations
- IBM AI Fairness 360 integration

### Bonus Task (10%)
Innovative AI tool proposal for automated documentation generation.

## Technologies Used

- **Python 3.8+**
- **Selenium WebDriver**: Test automation
- **Scikit-learn**: Machine learning
- **Pandas & NumPy**: Data processing
- **Matplotlib & Seaborn**: Visualization
- **Gradio/Streamlit**: Interactive demos

## Results Summary

| Task | Metric | Result |
|------|--------|--------|
| Task 1 | Speedup (AI vs Manual) | 100-150x |
| Task 2 | Test Pass Rate | 100% |
| Task 3 | Model Accuracy | 85-90% |
| Task 3 | F1-Score | 0.85 |

## Documentation

Detailed documentation for each task can be found in their respective directories:
- [Task 1 Documentation](task1_code_completion/README.md)
- [Task 2 Documentation](task2_automated_testing/README.md)
- [Task 3 Documentation](task3_predictive_analytics/README.md)

## Hugging Face Space

Interactive demo available at: [[Hugging Face Space URL](https://huggingface.co/spaces/dgith/week4)]

## Contributing

This is an academic assignment. For questions or suggestions, please open an issue.

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Author

Daniel Githinji
dgithinji331@gmail.com

## Acknowledgments

- Scikit-learn documentation
- Selenium documentation
- IBM AI Fairness 360 toolkit
- Course instructors and teaching assistants

## References

1. Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python
2. Selenium Documentation: https://www.selenium.dev/documentation/
3. IBM AI Fairness 360: https://aif360.mybluemix.net/

---

Last Updated: October 2025
