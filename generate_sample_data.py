"""
Generate sample teacher salary data for visualization.
This creates realistic data based on typical teacher salary patterns across US states.
"""

import pandas as pd
import numpy as np

# State data with realistic salary ranges (2024 estimates)
STATES_DATA = {
    'New York': {'base_min': 58000, 'base_max': 95000, 'top_min': 95000, 'top_max': 130000, 'region': 'Northeast'},
    'California': {'base_min': 50000, 'base_max': 85000, 'top_min': 90000, 'top_max': 125000, 'region': 'West'},
    'Texas': {'base_min': 44000, 'base_max': 60000, 'top_min': 62000, 'top_max': 85000, 'region': 'South'},
    'Florida': {'base_min': 40000, 'base_max': 55000, 'top_min': 58000, 'top_max': 75000, 'region': 'South'},
    'Illinois': {'base_min': 45000, 'base_max': 65000, 'top_min': 70000, 'top_max': 95000, 'region': 'Midwest'},
    'Pennsylvania': {'base_min': 46000, 'base_max': 62000, 'top_min': 68000, 'top_max': 92000, 'region': 'Northeast'},
    'Ohio': {'base_min': 40000, 'base_max': 58000, 'top_min': 62000, 'top_max': 82000, 'region': 'Midwest'},
    'Georgia': {'base_min': 42000, 'base_max': 57000, 'top_min': 60000, 'top_max': 78000, 'region': 'South'},
    'North Carolina': {'base_min': 38000, 'base_max': 52000, 'top_min': 55000, 'top_max': 72000, 'region': 'South'},
    'Michigan': {'base_min': 42000, 'base_max': 58000, 'top_min': 63000, 'top_max': 84000, 'region': 'Midwest'},
    'Massachusetts': {'base_min': 50000, 'base_max': 75000, 'top_min': 85000, 'top_max': 115000, 'region': 'Northeast'},
    'New Jersey': {'base_min': 52000, 'base_max': 78000, 'top_min': 88000, 'top_max': 120000, 'region': 'Northeast'},
    'Virginia': {'base_min': 42000, 'base_max': 58000, 'top_min': 62000, 'top_max': 80000, 'region': 'South'},
    'Washington': {'base_min': 48000, 'base_max': 68000, 'top_min': 75000, 'top_max': 98000, 'region': 'West'},
    'Arizona': {'base_min': 40000, 'base_max': 54000, 'top_min': 58000, 'top_max': 72000, 'region': 'West'},
    'Tennessee': {'base_min': 40000, 'base_max': 54000, 'top_min': 58000, 'top_max': 74000, 'region': 'South'},
    'Indiana': {'base_min': 40000, 'base_max': 55000, 'top_min': 60000, 'top_max': 76000, 'region': 'Midwest'},
    'Missouri': {'base_min': 38000, 'base_max': 52000, 'top_min': 56000, 'top_max': 71000, 'region': 'Midwest'},
    'Maryland': {'base_min': 50000, 'base_max': 68000, 'top_min': 75000, 'top_max': 100000, 'region': 'South'},
    'Wisconsin': {'base_min': 42000, 'base_max': 57000, 'top_min': 62000, 'top_max': 80000, 'region': 'Midwest'},
    'Minnesota': {'base_min': 44000, 'base_max': 60000, 'top_min': 68000, 'top_max': 88000, 'region': 'Midwest'},
    'Colorado': {'base_min': 42000, 'base_max': 58000, 'top_min': 65000, 'top_max': 82000, 'region': 'West'},
    'Alabama': {'base_min': 40000, 'base_max': 52000, 'top_min': 56000, 'top_max': 68000, 'region': 'South'},
    'South Carolina': {'base_min': 38000, 'base_max': 50000, 'top_min': 54000, 'top_max': 68000, 'region': 'South'},
    'Louisiana': {'base_min': 42000, 'base_max': 54000, 'top_min': 58000, 'top_max': 70000, 'region': 'South'},
    'Kentucky': {'base_min': 40000, 'base_max': 52000, 'top_min': 56000, 'top_max': 70000, 'region': 'South'},
    'Oregon': {'base_min': 44000, 'base_max': 60000, 'top_min': 68000, 'top_max': 88000, 'region': 'West'},
    'Oklahoma': {'base_min': 36000, 'base_max': 48000, 'top_min': 52000, 'top_max': 62000, 'region': 'South'},
    'Connecticut': {'base_min': 48000, 'base_max': 72000, 'top_min': 82000, 'top_max': 110000, 'region': 'Northeast'},
    'Iowa': {'base_min': 38000, 'base_max': 52000, 'top_min': 58000, 'top_max': 74000, 'region': 'Midwest'},
}


def generate_district_data(state, state_info, num_districts=5):
    """Generate sample district data for a given state."""
    np.random.seed(hash(state) % 2**32)  # Consistent data per state

    districts = []
    for i in range(num_districts):
        district_name = f"{state} District {i+1}"

        # Starting salary (with some variation)
        starting_salary = np.random.randint(
            state_info['base_min'],
            state_info['base_max']
        )

        # Top salary (with some variation)
        top_salary = np.random.randint(
            state_info['top_min'],
            state_info['top_max']
        )

        # Years to reach top (typically 15-25 years)
        years_to_top = np.random.randint(15, 26)

        # Calculate median salary (roughly 60-70% between starting and top)
        median_salary = int(starting_salary + (top_salary - starting_salary) * np.random.uniform(0.6, 0.7))

        # Budget share for teacher salaries (typically 40-60% of education budget)
        budget_share = np.random.uniform(0.40, 0.60)

        # Number of teachers
        num_teachers = np.random.randint(50, 1000)

        # Student-teacher ratio
        student_teacher_ratio = np.random.uniform(12, 22)

        districts.append({
            'state': state,
            'region': state_info['region'],
            'district': district_name,
            'starting_salary': starting_salary,
            'median_salary': median_salary,
            'top_salary': top_salary,
            'years_to_top': years_to_top,
            'budget_share_pct': round(budget_share * 100, 1),
            'num_teachers': num_teachers,
            'student_teacher_ratio': round(student_teacher_ratio, 1),
            'avg_raise_pct': round(((top_salary / starting_salary) ** (1/years_to_top) - 1) * 100, 2)
        })

    return districts


def generate_all_data():
    """Generate complete dataset for all states."""
    all_districts = []

    for state, state_info in STATES_DATA.items():
        districts = generate_district_data(state, state_info)
        all_districts.extend(districts)

    df = pd.DataFrame(all_districts)
    return df


def save_data():
    """Generate and save the sample data."""
    df = generate_all_data()
    df.to_csv('teacher_salary_data.csv', index=False)
    print(f"Generated {len(df)} district records across {df['state'].nunique()} states")
    print(f"\nData saved to: teacher_salary_data.csv")
    print(f"\nSample statistics:")
    print(f"  Starting salary range: ${df['starting_salary'].min():,} - ${df['starting_salary'].max():,}")
    print(f"  Top salary range: ${df['top_salary'].min():,} - ${df['top_salary'].max():,}")
    print(f"  Median years to top: {df['years_to_top'].median():.0f}")
    return df


if __name__ == '__main__':
    df = save_data()
    print("\nFirst few rows:")
    print(df.head())
