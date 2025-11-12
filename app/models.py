from datetime import datetime
from app.extensions import db

# ===================================================================
# SMARTCRM MODELS - Erweiterte Datenstruktur
# ===================================================================

class User(db.Model):
    """Benutzer/Mitarbeiter-Modell mit Rollenverwaltung"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))  # Für zukünftige Auth
    role = db.Column(db.String(20), default='employee')  # admin, manager, employee, customer
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    assigned_customers = db.relationship('Customer', backref='assigned_user', lazy=True, foreign_keys='Customer.assigned_to')
    assigned_tasks = db.relationship('Task', backref='assignee', lazy=True)
    activities = db.relationship('ActivityLog', backref='user', lazy=True)
    
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Customer(db.Model):
    """Kunden-Modell (erweitert)"""
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Company name
    contact_person = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(50))
    address = db.Column(db.Text)
    notes = db.Column(db.Text)
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    orders = db.relationship('Order', backref='customer', lazy=True)
    projects = db.relationship('Project', backref='customer', lazy=True)


class Project(db.Model):
    """Projekt-Modell"""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='geplant')  # geplant, aktiv, pausiert, abgeschlossen
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    assigned_team = db.Column(db.Text)  # JSON oder komma-separierte IDs
    progress = db.Column(db.Integer, default=0)  # 0-100%
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    tasks = db.relationship('Task', backref='project', lazy=True)


class Task(db.Model):
    """Aufgaben-Modell"""
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    status = db.Column(db.String(20), default='offen')  # offen, in_bearbeitung, erledigt
    due_date = db.Column(db.Date)
    priority = db.Column(db.String(20), default='mittel')  # niedrig, mittel, hoch
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Order(db.Model):
    """Auftrags-Modell (bestehend)"""
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Contact(db.Model):
    """Kontakt-Modell (bestehend)"""
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    type = db.Column(db.String(50))  # email, phone, meeting, etc.
    date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    customer = db.relationship('Customer', backref='contacts', lazy=True)


class ActivityLog(db.Model):
    """Aktivitätsprotokoll für Audit-Trail"""
    __tablename__ = 'activity_log'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    action = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ===================================================================
# RECHNUNGSWESEN & CONTROLLING MODELS - Neue Erweiterung
# ===================================================================

class BalanceSheet(db.Model):
    """Bilanz-Daten für Unternehmensanalyse"""
    __tablename__ = 'balance_sheets'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.Integer)  # 1-4 oder NULL für Jahresbilanz
    
    # Aktiva
    current_assets = db.Column(db.Float, default=0)  # Umlaufvermögen
    fixed_assets = db.Column(db.Float, default=0)   # Anlagevermögen
    
    # Passiva
    equity = db.Column(db.Float, default=0)          # Eigenkapital
    liabilities = db.Column(db.Float, default=0)     # Fremdkapital
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    customer = db.relationship('Customer', backref='balance_sheets', lazy=True)
    
    @property
    def total_assets(self):
        return self.current_assets + self.fixed_assets
    
    @property
    def equity_ratio(self):
        """Eigenkapitalquote in %"""
        if self.total_assets > 0:
            return (self.equity / self.total_assets) * 100
        return 0
    
    @property
    def debt_ratio(self):
        """Verschuldungsgrad in %"""
        if self.equity > 0:
            return (self.liabilities / self.equity) * 100
        return 0


class IncomeStatement(db.Model):
    """GuV - Gewinn- und Verlustrechnung"""
    __tablename__ = 'income_statements'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.Integer)
    
    # Erlöse
    revenue = db.Column(db.Float, default=0)             # Umsatzerlöse
    revenue_vat = db.Column(db.Float, default=0)         # Umsatzsteuer
    
    # Aufwendungen
    cost_of_goods = db.Column(db.Float, default=0)       # Wareneinsatz
    input_vat = db.Column(db.Float, default=0)           # Vorsteuer
    personnel_costs = db.Column(db.Float, default=0)     # Personalkosten
    other_expenses = db.Column(db.Float, default=0)      # Sonstige Aufwendungen
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    customer = db.relationship('Customer', backref='income_statements', lazy=True)
    
    @property
    def gross_profit(self):
        """Rohgewinn"""
        return self.revenue - self.cost_of_goods
    
    @property
    def ebit(self):
        """Betriebsergebnis (EBIT)"""
        return self.revenue - self.cost_of_goods - self.personnel_costs - self.other_expenses
    
    @property
    def vat_payable(self):
        """Zahllast (Umsatzsteuer - Vorsteuer)"""
        return self.revenue_vat - self.input_vat
    
    @property
    def gross_margin(self):
        """Rohertragsmarge in %"""
        if self.revenue > 0:
            return (self.gross_profit / self.revenue) * 100
        return 0


class SalesData(db.Model):
    """Umsatzdaten für Marktanalyse"""
    __tablename__ = 'sales_data'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date = db.Column(db.Date, nullable=False)
    product_group = db.Column(db.String(100))
    sales_volume = db.Column(db.Float, default=0)        # Absatzmenge
    sales_revenue = db.Column(db.Float, default=0)       # Umsatz
    market_share = db.Column(db.Float, default=0)        # Marktanteil in %
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Beziehungen
    customer = db.relationship('Customer', backref='sales_data', lazy=True)


class CostCenter(db.Model):
    """Kostenstellen für Controlling"""
    __tablename__ = 'cost_centers'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    code = db.Column(db.String(20), nullable=False)      # z.B. "K100"
    name = db.Column(db.String(255), nullable=False)     # z.B. "Produktion"
    budget = db.Column(db.Float, default=0)
    actual_costs = db.Column(db.Float, default=0)
    year = db.Column(db.Integer, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Beziehungen
    customer = db.relationship('Customer', backref='cost_centers', lazy=True)
    
    @property
    def variance(self):
        """Abweichung Budget vs. Ist"""
        return self.budget - self.actual_costs
    
    @property
    def variance_percentage(self):
        """Abweichung in %"""
        if self.budget > 0:
            return (self.variance / self.budget) * 100
        return 0