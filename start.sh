#!/bin/bash

echo "Teacher Salary Comparison Tool - Quick Start"
echo "=============================================="
echo ""

# Check if data file exists
if [ ! -f "teacher_salary_data.csv" ]; then
    echo "Generating sample data..."
    python generate_sample_data.py
    echo ""
fi

echo "Starting dashboard..."
echo "Once started, open your browser to: http://127.0.0.1:8050"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
