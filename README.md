# Teacher Salary Comparison Tool

An interactive dashboard for comparing teacher salaries across states and districts nationwide. Built with Dash and Plotly.

## Features

- **State-by-State Comparison**: Compare starting salaries, top salaries, and salary progression across all US states
- **Regional Analysis**: Filter and analyze data by geographic region (Northeast, South, Midwest, West)
- **Budget Insights**: View what percentage of education budgets go to teacher salaries
- **Career Progression**: Visualize how salaries increase over a teacher's career
- **Interactive Filters**: Select specific states or regions to focus your analysis
- **Detailed Metrics**: Explore district-level data with sortable tables
- **✨ Real Alabama Data**: Detailed salary information for 9 Alabama school districts with verified sources

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
python generate_alabama_data.py
```

This creates:
- `teacher_salary_data.csv` - Sample data for 30 states and 150 districts
- `alabama_teacher_salaries.csv` - Real Alabama district salary data (9 districts)

**Or use the quick start script:**
```bash
./start.sh
```

### 3. Run the Dashboard

```bash
python app.py
```

### 4. Open in Browser

Navigate to: **http://127.0.0.1:8050**

## Project Structure

```
school-pay-visualization/
├── app.py                              # Main Dash application
├── generate_sample_data.py             # National sample data generator
├── generate_alabama_data.py            # Alabama district data generator
├── start.sh                            # Quick start script
├── requirements.txt                    # Python dependencies
├── teacher_salary_data.csv             # Generated national sample data
├── alabama_teacher_salaries.csv        # Generated Alabama district data
├── alabama_teacher_salaries_detailed.csv # Detailed Alabama data with salary schedules
└── README.md                           # This file
```

## Data Sources

### General Sample Data

The sample data is based on realistic teacher salary patterns across US states as of 2024. The data generator creates:

- **Starting Salary**: Entry-level teacher pay by state/district
- **Median Salary**: Mid-career teacher compensation
- **Top Salary**: Maximum salary for experienced teachers
- **Years to Top**: Time required to reach maximum pay
- **Budget Share**: Percentage of education budget for teacher salaries
- **Student-Teacher Ratio**: Average students per teacher
- **Annual Raise %**: Average yearly salary increase

### Alabama District Data (Real Data)

The dashboard includes **real salary data** for 9 Alabama school districts (2024-2025 school year):

**Districts Included:**
- Baldwin County Schools
- Mobile County Public Schools
- Saraland City Schools
- Orange Beach City Schools
- Gulf Shores City Schools
- Birmingham City Schools
- Montgomery Public Schools
- Hoover City Schools
- Huntsville City Schools

**Data Sources:**
- Official district salary schedules from school board websites
- Alabama Department of Education FY 2024-2025 State Minimum Salary Schedule
- Indeed, Glassdoor, and Salary.com aggregated salary data
- We Teach Alabama resources

**Salary Ranges:**
- Starting salaries: $45,000 - $49,500
- Average salaries: $47,543 - $56,583
- Top salaries: $65,000 - $84,716

Select "Alabama" in the state filter to view detailed comparisons. The data table includes source attribution for each district.

### Using Additional Real Data

To add more states with real NCES (National Center for Education Statistics) data:

1. Visit: https://nces.ed.gov/ccd/tcssurv.asp
2. Download the Teacher Compensation Survey data files
3. Create a similar data generation script like `generate_alabama_data.py`
4. Update `app.py` to load your additional CSV files

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
