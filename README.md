# Teacher Salary Comparison Tool

An interactive dashboard for comparing teacher salaries across states and districts nationwide. Built with Dash and Plotly.

## Features

- **State-by-State Comparison**: Compare starting salaries, top salaries, and salary progression across all US states
- **Regional Analysis**: Filter and analyze data by geographic region (Northeast, South, Midwest, West)
- **Budget Insights**: View what percentage of education budgets go to teacher salaries
- **Career Progression**: Visualize how salaries increase over a teacher's career
- **Interactive Filters**: Select specific states or regions to focus your analysis
- **Detailed Metrics**: Explore district-level data with sortable tables

## Screenshots

The dashboard includes:
- Key metrics cards (avg starting salary, top salary, years to top, budget share)
- Starting vs Top Salary comparison by state
- Salary growth potential analysis
- Budget share percentage visualization
- Years to reach top salary comparison
- Career salary progression charts
- Detailed district-level data table

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate Sample Data

```bash
python generate_sample_data.py
```

This creates `teacher_salary_data.csv` with realistic sample data for 30 states and 150 districts.

### 3. Run the Dashboard

```bash
python app.py
```

### 4. Open in Browser

Navigate to: **http://127.0.0.1:8050**

## Project Structure

```
school-pay-visualization/
├── app.py                      # Main Dash application
├── generate_sample_data.py     # Data generation script
├── requirements.txt            # Python dependencies
├── teacher_salary_data.csv     # Generated data (after running step 2)
└── README.md                   # This file
```

## Data Source

The sample data is based on realistic teacher salary patterns across US states as of 2024. The data generator creates:

- **Starting Salary**: Entry-level teacher pay by state/district
- **Median Salary**: Mid-career teacher compensation
- **Top Salary**: Maximum salary for experienced teachers
- **Years to Top**: Time required to reach maximum pay
- **Budget Share**: Percentage of education budget for teacher salaries
- **Student-Teacher Ratio**: Average students per teacher
- **Annual Raise %**: Average yearly salary increase

### Using Real Data

To use actual NCES (National Center for Education Statistics) data:

1. Visit: https://nces.ed.gov/ccd/tcssurv.asp
2. Download the Teacher Compensation Survey data files
3. Modify `app.py` to load your CSV files instead of the sample data

## Technologies Used

- **Dash**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **Bootstrap**: Responsive UI components

## Customization

### Add More States

Edit `generate_sample_data.py` and add entries to the `STATES_DATA` dictionary:

```python
'State Name': {
    'base_min': 40000,
    'base_max': 60000,
    'top_min': 70000,
    'top_max': 90000,
    'region': 'Region'
}
```

### Modify Visualizations

Edit `app.py` to customize:
- Chart types (bar, scatter, line, etc.)
- Color schemes
- Layout and styling
- Metrics displayed

### Change Port

In `app.py`, modify the last line:

```python
app.run_server(debug=True, host='0.0.0.0', port=YOUR_PORT)
```

## Troubleshooting

**Issue**: `FileNotFoundError: teacher_salary_data.csv`
- **Solution**: Run `python generate_sample_data.py` first

**Issue**: Port 8050 already in use
- **Solution**: Change the port in `app.py` or kill the process using port 8050

**Issue**: Module not found errors
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## License

See LICENSE file for details.

## Contributing

Contributions welcome! Feel free to:
- Add more data sources
- Improve visualizations
- Add new metrics
- Enhance UI/UX
