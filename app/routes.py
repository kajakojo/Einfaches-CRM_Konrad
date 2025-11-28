from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Customer, Order, Contact, User, Project, Task, ActivityLog
from datetime import datetime, timedelta
from sqlalchemy import func

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Statistiken sammeln
    stats = {
        'total_customers': Customer.query.count(),
        'total_projects': Project.query.count(),
        'active_projects': Project.query.filter_by(status='aktiv').count(),
        'open_tasks': Task.query.filter(Task.status.in_(['offen', 'in_bearbeitung'])).count(),
        'overdue_tasks': Task.query.filter(Task.due_date < datetime.now(), Task.status != 'erledigt').count(),
        'total_revenue': db.session.query(func.sum(Order.total)).scalar() or 0
    }
    
    # Letzte Aufgaben
    recent_tasks = Task.query.filter(Task.status != 'erledigt').order_by(Task.due_date.asc()).limit(5).all()
    
    # Letzte Aktivitäten
    recent_activities = ActivityLog.query.order_by(ActivityLog.created_at.desc()).limit(5).all()
    
    # Diagramm-Daten vorbereiten
    # Monatliche Umsätze (letzte 6 Monate)
    revenue_data = []
    revenue_labels = []
    for i in range(5, -1, -1):
        month_start = datetime.now().replace(day=1) - timedelta(days=30*i)
        month_name = month_start.strftime('%B')
        # Vereinfachte Demo-Daten (später aus DB)
        revenue_data.append((i + 1) * 1500 + (i % 2) * 500)
        revenue_labels.append(month_name[:3])
    
    # Projektstatus-Verteilung
    project_statuses = db.session.query(Project.status, func.count(Project.id)).group_by(Project.status).all()
    project_labels = [s[0].capitalize() for s in project_statuses] or ['Geplant', 'Aktiv', 'Pausiert', 'Abgeschlossen']
    project_data = [s[1] for s in project_statuses] or [2, 3, 1, 4]
    
    # Aktivitäts-Daten (letzte 7 Tage)
    activity_data = []
    activity_labels = []
    for i in range(6, -1, -1):
        day = datetime.now() - timedelta(days=i)
        day_start = day.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day.replace(hour=23, minute=59, second=59, microsecond=999999)
        count = ActivityLog.query.filter(ActivityLog.created_at >= day_start, ActivityLog.created_at <= day_end).count()
        activity_data.append(count)
        activity_labels.append(day.strftime('%d.%m'))
    
    chart_data = {
        'revenue_labels': revenue_labels,
        'revenue_data': revenue_data,
        'project_labels': project_labels,
        'project_data': project_data,
        'activity_labels': activity_labels,
        'activity_data': activity_data
    }
    
    return render_template('index.html', 
                         stats=stats, 
                         recent_tasks=recent_tasks, 
                         recent_activities=recent_activities,
                         chart_data=chart_data)

# Customer routes
@bp.route('/customers')
def list_customers():
    customers = Customer.query.all()
    return render_template('customers/list.html', customers=customers)

@bp.route('/customers/create', methods=['GET', 'POST'])
def create_customer():
    if request.method == 'POST':
        customer = Customer(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone']
        )
        db.session.add(customer)
        db.session.commit()
        flash('Customer created successfully!')
        return redirect(url_for('main.list_customers'))
    return render_template('customers/create.html')

@bp.route('/customers/<int:id>')
def view_customer(id):
    customer = Customer.query.get_or_404(id)
    return render_template('customers/view.html', customer=customer)

# Order routes
@bp.route('/orders')
def list_orders():
    orders = Order.query.all()
    return render_template('orders/list.html', orders=orders)

@bp.route('/orders/create', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        order = Order(
            customer_id=request.form['customer_id'],
            total=float(request.form['total']),
            description=request.form['description'],
            status=request.form['status']
        )
        db.session.add(order)
        db.session.commit()
        flash('Order created successfully!')
        return redirect(url_for('main.list_orders'))
    customers = Customer.query.all()
    return render_template('orders/create.html', customers=customers)

# Contact routes
@bp.route('/contacts')
def list_contacts():
    contacts = Contact.query.all()
    return render_template('contacts/list.html', contacts=contacts)

@bp.route('/contacts/create', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        contact = Contact(
            customer_id=request.form['customer_id'],
            type=request.form['type'],
            notes=request.form['notes']
        )
        db.session.add(contact)
        db.session.commit()
        flash('Contact record created successfully!')
        return redirect(url_for('main.list_contacts'))
    customers = Customer.query.all()
    return render_template('contacts/create.html', customers=customers)

@bp.route('/contacts/<int:id>')
def view_contact(id):
    contact = Contact.query.get_or_404(id)
    return render_template('contacts/view.html', contact=contact)

@bp.route('/orders/<int:id>')
def view_order(id):
    order = Order.query.get_or_404(id)
    return render_template('orders/view.html', order=order)

# Project routes
@bp.route('/projects')
def list_projects():
    projects = Project.query.all()
    return render_template('projects/list.html', projects=projects)

@bp.route('/projects/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        project = Project(
            project_name=request.form['project_name'],
            customer_id=request.form.get('customer_id'),
            description=request.form.get('description'),
            status=request.form.get('status', 'geplant'),
            progress=int(request.form.get('progress', 0)),
            start_date=datetime.strptime(request.form['start_date'], '%Y-%m-%d') if request.form.get('start_date') else None,
            end_date=datetime.strptime(request.form['end_date'], '%Y-%m-%d') if request.form.get('end_date') else None
        )
        db.session.add(project)
        db.session.commit()
        flash('Projekt erfolgreich erstellt!')
        return redirect(url_for('main.list_projects'))
    customers = Customer.query.all()
    return render_template('projects/create.html', customers=customers)

@bp.route('/projects/<int:id>')
def view_project(id):
    project = Project.query.get_or_404(id)
    tasks = Task.query.filter_by(project_id=id).all()
    return render_template('projects/view.html', project=project, tasks=tasks)

# Task routes
@bp.route('/tasks')
def list_tasks():
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks, now=datetime.now)

@bp.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        # Leere Strings in None umwandeln für Foreign Keys
        assigned_to = request.form.get('assigned_to')
        project_id = request.form.get('project_id')
        
        task = Task(
            title=request.form['title'],
            description=request.form.get('description'),
            project_id=int(project_id) if project_id and project_id.strip() else None,
            assigned_to=int(assigned_to) if assigned_to and assigned_to.strip() else None,
            priority=request.form.get('priority', 'mittel'),
            status=request.form.get('status', 'offen'),
            due_date=datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form.get('due_date') else None
        )
        db.session.add(task)
        db.session.commit()
        flash('Aufgabe erfolgreich erstellt!')
        return redirect(url_for('main.list_tasks'))
    projects = Project.query.all()
    users = User.query.all()
    return render_template('tasks/create.html', projects=projects, users=users)

@bp.route('/tasks/<int:id>')
def view_task(id):
    task = Task.query.get_or_404(id)
    return render_template('tasks/view.html', task=task, now=datetime.now)


# ===================================================================
# RECHNUNGSWESEN & CONTROLLING ROUTES - Neue Erweiterung
# ===================================================================

@bp.route('/accounting')
def accounting_overview():
    """Übersicht Rechnungswesen & Controlling"""
    from app.models import BalanceSheet, IncomeStatement, SalesData, CostCenter
    
    customers_with_data = Customer.query.join(IncomeStatement).distinct().all()
    
    # Statistiken
    stats = {
        'balance_sheets': BalanceSheet.query.count(),
        'income_statements': IncomeStatement.query.count(),
        'sales_records': SalesData.query.count(),
        'cost_centers': CostCenter.query.count()
    }
    
    return render_template('accounting/overview.html', 
                         customers=customers_with_data,
                         stats=stats)


@bp.route('/accounting/balance-sheet')
def balance_sheet_analysis():
    """Bilanzanalyse"""
    from app.models import BalanceSheet
    
    customer_id = request.args.get('customer_id', type=int)
    year = request.args.get('year', datetime.now().year, type=int)
    
    query = BalanceSheet.query
    if customer_id:
        query = query.filter_by(customer_id=customer_id)
    if year:
        query = query.filter_by(year=year)
    
    balance_sheets = query.all()
    customers = Customer.query.all()
    
    # Kennzahlen berechnen
    analysis = []
    for bs in balance_sheets:
        analysis.append({
            'customer': bs.customer.name if bs.customer else 'N/A',
            'year': bs.year,
            'quarter': bs.quarter or 'Jahr',
            'total_assets': bs.total_assets,
            'equity': bs.equity,
            'liabilities': bs.liabilities,
            'equity_ratio': bs.equity_ratio,
            'debt_ratio': bs.debt_ratio
        })
    
    return render_template('accounting/balance_sheet.html',
                         analysis=analysis,
                         customers=customers,
                         selected_customer=customer_id,
                         selected_year=year)


@bp.route('/accounting/income-statement')
def income_statement_analysis():
    """GuV-Analyse"""
    from app.models import IncomeStatement
    
    customer_id = request.args.get('customer_id', type=int)
    year = request.args.get('year', datetime.now().year, type=int)
    
    query = IncomeStatement.query
    if customer_id:
        query = query.filter_by(customer_id=customer_id)
    if year:
        query = query.filter_by(year=year)
    
    income_statements = query.all()
    customers = Customer.query.all()
    
    # Kennzahlen
    analysis = []
    for inc in income_statements:
        analysis.append({
            'customer': inc.customer.name if inc.customer else 'N/A',
            'year': inc.year,
            'quarter': inc.quarter or 'Jahr',
            'revenue': inc.revenue,
            'gross_profit': inc.gross_profit,
            'ebit': inc.ebit,
            'vat_payable': inc.vat_payable,
            'gross_margin': inc.gross_margin
        })
    
    # Chart-Daten
    chart_labels = [f"{a['customer']} Q{a['quarter']}" for a in analysis]
    chart_revenue = [a['revenue'] for a in analysis]
    chart_profit = [a['ebit'] for a in analysis]
    
    return render_template('accounting/income_statement.html',
                         analysis=analysis,
                         customers=customers,
                         selected_customer=customer_id,
                         selected_year=year,
                         chart_labels=chart_labels,
                         chart_revenue=chart_revenue,
                         chart_profit=chart_profit)


@bp.route('/accounting/market-analysis')
def market_analysis():
    """Marktanalyse mit Umsatzdaten"""
    from app.models import SalesData
    
    customer_id = request.args.get('customer_id', type=int)
    product_group = request.args.get('product_group')
    
    query = SalesData.query
    if customer_id:
        query = query.filter_by(customer_id=customer_id)
    if product_group:
        query = query.filter_by(product_group=product_group)
    
    sales_data = query.order_by(SalesData.date.desc()).all()
    customers = Customer.query.all()
    
    # Produktgruppen für Filter
    product_groups = db.session.query(SalesData.product_group).distinct().all()
    product_groups = [p[0] for p in product_groups if p[0]]
    
    # Chart-Daten: Umsatz über Zeit
    chart_labels = [sd.date.strftime('%d.%m.%Y') for sd in sales_data[:12]]
    chart_revenue = [sd.sales_revenue for sd in sales_data[:12]]
    chart_volume = [sd.sales_volume for sd in sales_data[:12]]
    
    return render_template('accounting/market_analysis.html',
                         sales_data=sales_data,
                         customers=customers,
                         product_groups=product_groups,
                         selected_customer=customer_id,
                         selected_product=product_group,
                         chart_labels=chart_labels,
                         chart_revenue=chart_revenue,
                         chart_volume=chart_volume)


@bp.route('/accounting/cost-centers')
def cost_centers():
    """Kostenstellencontrolling"""
    from app.models import CostCenter
    
    customer_id = request.args.get('customer_id', type=int)
    year = request.args.get('year', datetime.now().year, type=int)
    
    query = CostCenter.query
    if customer_id:
        query = query.filter_by(customer_id=customer_id)
    if year:
        query = query.filter_by(year=year)
    
    cost_centers_data = query.all()
    customers = Customer.query.all()
    
    # Gesamtstatistiken
    total_budget = sum([cc.budget for cc in cost_centers_data])
    total_actual = sum([cc.actual_costs for cc in cost_centers_data])
    total_variance = total_budget - total_actual
    
    return render_template('accounting/cost_centers.html',
                         cost_centers=cost_centers_data,
                         customers=customers,
                         selected_customer=customer_id,
                         selected_year=year,
                         total_budget=total_budget,
                         total_actual=total_actual,
                         total_variance=total_variance)