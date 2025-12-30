#!/bin/bash

echo "Teacher Salary Comparison Tool - Quick Start"
echo "=============================================="
echo ""

# Check if general data file exists
if [ ! -f "teacher_salary_data.csv" ]; then
    echo "Generating general sample data..."
    python generate_sample_data.py
    echo ""
fi

# Check if Alabama data file exists
if [ ! -f "alabama_teacher_salaries.csv" ]; then
    echo "Generating Alabama district data..."
    python generate_alabama_data.py
    echo ""
fi

echo "Starting dashboard..."
echo "Once started, open your browser to: http://127.0.0.1:8050"
echo ""
echo "Features:"
echo "  - Compare teacher salaries across 30 states"
echo "  - View detailed Alabama district data (9 districts)"
echo "  - Interactive filters and visualizations"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
