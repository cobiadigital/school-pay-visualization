"""
Teacher Salary Comparison Dashboard
Interactive Dash application for comparing teacher salaries across states and districts.
"""

import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load data
try:
    df_general = pd.read_csv('teacher_salary_data.csv')
except FileNotFoundError:
    print("General data file not found. Please run: python generate_sample_data.py")
    exit(1)

# Load Alabama-specific data if available
try:
    df_alabama = pd.read_csv('alabama_teacher_salaries.csv')
    # Merge datasets - remove Alabama from general data if it exists, add detailed Alabama data
    df_general = df_general[df_general['state'] != 'Alabama']
    df = pd.concat([df_general, df_alabama], ignore_index=True)
    has_alabama_data = True
    print("✓ Loaded Alabama district data with real salary information")
except FileNotFoundError:
    df = df_general
    has_alabama_data = False
    print("Note: Alabama detailed data not found. Run: python generate_alabama_data.py")

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Teacher Salary Comparison Tool"

# Calculate state-level aggregates
state_summary = df.groupby('state').agg({
    'starting_salary': 'mean',
    'median_salary': 'mean',
    'top_salary': 'mean',
    'years_to_top': 'mean',
    'budget_share_pct': 'mean',
    'student_teacher_ratio': 'mean',
    'avg_raise_pct': 'mean',
    'region': 'first'
}).reset_index()

state_summary.columns = ['state', 'avg_starting_salary', 'avg_median_salary',
                         'avg_top_salary', 'avg_years_to_top', 'avg_budget_share_pct',
                         'avg_student_teacher_ratio', 'avg_raise_pct', 'region']

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("🎓 Teacher Salary Comparison Tool", className="text-center mb-4 mt-4"),
            html.P("Compare teacher compensation across states and districts nationwide",
                   className="text-center text-muted mb-4")
        ])
    ]),

    # Filters
    dbc.Row([
        dbc.Col([
            html.Label("Select Region(s):"),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': 'All Regions', 'value': 'ALL'}] +
                        [{'label': region, 'value': region} for region in sorted(df['region'].unique())],
                value='ALL',
                multi=False,
                clearable=False
            )
        ], width=4),
        dbc.Col([
            html.Label("Select State(s):"),
            dcc.Dropdown(
                id='state-filter',
                options=[{'label': 'All States', 'value': 'ALL'}] +
                        [{'label': state, 'value': state} for state in sorted(df['state'].unique())],
                value='ALL',
                multi=True,
                placeholder="Select states to compare..."
            )
        ], width=8),
    ], className="mb-4"),

    # Alabama Data Info Banner (shown when Alabama data is loaded)
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("📍 Alabama District Data Available", className="alert-heading"),
                html.P([
                    "Real salary data for 9 Alabama districts including Baldwin County, Mobile County, ",
                    "Saraland, Orange Beach, Gulf Shores, Birmingham, Montgomery, Hoover, and Huntsville. ",
                    "Select 'Alabama' in the state filter to view detailed comparisons."
                ], className="mb-2"),
                html.Small("Data sources: Official district salary schedules, Alabama Dept of Education, Indeed, Glassdoor, Salary.com (2024-2025)",
                          className="text-muted")
            ], color="info", dismissable=True, id="alabama-alert", is_open=has_alabama_data)
        ])
    ], className="mb-3"),

    # Key Metrics Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Avg Starting Salary", className="card-title text-center"),
                    html.H2(id="metric-starting", className="text-center text-success")
                ])
            ])
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Avg Top Salary", className="card-title text-center"),
                    html.H2(id="metric-top", className="text-center text-primary")
                ])
            ])
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Years to Top", className="card-title text-center"),
                    html.H2(id="metric-years", className="text-center text-warning")
                ])
            ])
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Budget Share", className="card-title text-center"),
                    html.H2(id="metric-budget", className="text-center text-info")
                ])
            ])
        ], width=3),
    ], className="mb-4"),

    # Charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='salary-comparison-chart')
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='salary-range-chart')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='budget-share-chart')
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='years-to-top-chart')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='raise-progression-chart')
        ], width=6)
    ], className="mb-4"),

    # Data table
    dbc.Row([
        dbc.Col([
            html.H4("District-Level Data", className="mb-3"),
            html.Div(id='data-table')
        ])
    ], className="mb-4"),

], fluid=True)


# Callbacks
@callback(
    [Output('state-filter', 'options'),
     Output('state-filter', 'value')],
    Input('region-filter', 'value')
)
def update_state_options(selected_region):
    """Update state dropdown based on region selection."""
    if selected_region == 'ALL':
        states = sorted(df['state'].unique())
    else:
        states = sorted(df[df['region'] == selected_region]['state'].unique())

    options = [{'label': 'All States', 'value': 'ALL'}] + \
              [{'label': state, 'value': state} for state in states]

    return options, 'ALL'


@callback(
    [Output('metric-starting', 'children'),
     Output('metric-top', 'children'),
     Output('metric-years', 'children'),
     Output('metric-budget', 'children'),
     Output('salary-comparison-chart', 'figure'),
     Output('salary-range-chart', 'figure'),
     Output('budget-share-chart', 'figure'),
     Output('years-to-top-chart', 'figure'),
     Output('raise-progression-chart', 'figure'),
     Output('data-table', 'children')],
    [Input('region-filter', 'value'),
     Input('state-filter', 'value')]
)
def update_dashboard(selected_region, selected_states):
    """Update all dashboard components based on filters."""

    # Filter data
    filtered_df = df.copy()

    if selected_region != 'ALL':
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    if selected_states != 'ALL' and selected_states:
        if isinstance(selected_states, str):
            selected_states = [selected_states]
        filtered_df = filtered_df[filtered_df['state'].isin(selected_states)]

    # Calculate metrics
    avg_starting = f"${filtered_df['starting_salary'].mean():,.0f}"
    avg_top = f"${filtered_df['top_salary'].mean():,.0f}"
    avg_years = f"{filtered_df['years_to_top'].mean():.1f} yrs"
    avg_budget = f"{filtered_df['budget_share_pct'].mean():.1f}%"

    # Prepare state-level data for charts
    chart_data = filtered_df.groupby('state').agg({
        'starting_salary': 'mean',
        'median_salary': 'mean',
        'top_salary': 'mean',
        'years_to_top': 'mean',
        'budget_share_pct': 'mean',
        'avg_raise_pct': 'mean',
        'region': 'first'
    }).reset_index()

    # Sort by starting salary for better visualization
    chart_data = chart_data.sort_values('starting_salary', ascending=True)

    # Chart 1: Starting vs Top Salary Comparison
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        name='Starting Salary',
        x=chart_data['state'],
        y=chart_data['starting_salary'],
        marker_color='lightblue'
    ))
    fig1.add_trace(go.Bar(
        name='Top Salary',
        x=chart_data['state'],
        y=chart_data['top_salary'],
        marker_color='darkblue'
    ))
    fig1.update_layout(
        title='Starting vs Top Salary by State',
        xaxis_title='State',
        yaxis_title='Salary ($)',
        barmode='group',
        hovermode='x unified',
        height=400
    )

    # Chart 2: Salary Range (Top - Starting)
    chart_data['salary_range'] = chart_data['top_salary'] - chart_data['starting_salary']
    chart_data_sorted_range = chart_data.sort_values('salary_range', ascending=True)

    fig2 = px.bar(
        chart_data_sorted_range,
        x='salary_range',
        y='state',
        orientation='h',
        color='region',
        title='Salary Growth Potential by State (Top - Starting)',
        labels={'salary_range': 'Salary Range ($)', 'state': 'State'},
        height=400
    )

    # Chart 3: Budget Share Percentage
    chart_data_sorted_budget = chart_data.sort_values('budget_share_pct', ascending=True)

    fig3 = px.bar(
        chart_data_sorted_budget,
        x='budget_share_pct',
        y='state',
        orientation='h',
        color='region',
        title='Teacher Salary Budget Share by State',
        labels={'budget_share_pct': 'Budget Share (%)', 'state': 'State'},
        height=400
    )

    # Chart 4: Years to Reach Top Salary
    chart_data_sorted_years = chart_data.sort_values('years_to_top', ascending=True)

    fig4 = px.bar(
        chart_data_sorted_years,
        x='years_to_top',
        y='state',
        orientation='h',
        color='region',
        title='Years to Reach Top Salary by State',
        labels={'years_to_top': 'Years', 'state': 'State'},
        height=400
    )

    # Chart 5: Salary Progression Comparison
    fig5 = go.Figure()

    # Show progression for up to 10 states
    states_to_show = chart_data.head(10)['state'].tolist()

    for state in states_to_show:
        state_data = chart_data[chart_data['state'] == state].iloc[0]
        years = np.arange(0, int(state_data['years_to_top']) + 1)

        # Calculate salary progression (simplified linear progression)
        salaries = state_data['starting_salary'] + \
                   (state_data['top_salary'] - state_data['starting_salary']) * \
                   (years / state_data['years_to_top'])

        fig5.add_trace(go.Scatter(
            x=years,
            y=salaries,
            mode='lines+markers',
            name=state,
            hovertemplate='<b>%{fullData.name}</b><br>Year: %{x}<br>Salary: $%{y:,.0f}<extra></extra>'
        ))

    fig5.update_layout(
        title='Salary Progression Over Career (Top 10 States by Starting Salary)',
        xaxis_title='Years of Experience',
        yaxis_title='Salary ($)',
        hovermode='x unified',
        height=400
    )

    # Data Table
    # Include data_source column if it exists (for Alabama districts)
    base_columns = ['state', 'district', 'starting_salary', 'median_salary',
                   'top_salary', 'years_to_top', 'budget_share_pct',
                   'student_teacher_ratio']

    if 'data_source' in filtered_df.columns:
        display_columns = base_columns + ['data_source']
        display_df = filtered_df[display_columns].copy()
        display_df.columns = ['State', 'District', 'Starting Salary', 'Median Salary',
                             'Top Salary', 'Years to Top', 'Budget Share %',
                             'Student:Teacher Ratio', 'Data Source']
    else:
        display_df = filtered_df[base_columns].copy()
        display_df.columns = ['State', 'District', 'Starting Salary', 'Median Salary',
                             'Top Salary', 'Years to Top', 'Budget Share %', 'Student:Teacher Ratio']

    # Format currency columns
    for col in ['Starting Salary', 'Median Salary', 'Top Salary']:
        display_df[col] = display_df[col].apply(lambda x: f'${x:,.0f}')

    table = dbc.Table.from_dataframe(
        display_df.head(20),
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        size='sm'
    )

    return (avg_starting, avg_top, avg_years, avg_budget,
            fig1, fig2, fig3, fig4, fig5, table)


if __name__ == '__main__':
    print("Starting Teacher Salary Comparison Dashboard...")
    print("Open your browser to: http://127.0.0.1:8050")
    app.run(debug=True, host='0.0.0.0', port=8050)
