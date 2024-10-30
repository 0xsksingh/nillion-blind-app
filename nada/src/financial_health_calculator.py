from nada_dsl import *

def nada_main():
    # Define parties
    user = Party(name="Party1")
    advisor = Party(name="Party2")
    regulator = Party(name="Party3")  # Added regulator party
    
    # Secure inputs from user
    monthly_income = SecretInteger(Input(name="monthly_income", party=user))
    total_debt = SecretInteger(Input(name="total_debt", party=user))
    monthly_savings = SecretInteger(Input(name="monthly_savings", party=user))
    monthly_expenses = SecretInteger(Input(name="monthly_expenses", party=user))
    credit_score = SecretInteger(Input(name="credit_score", party=user))
    investment_amount = SecretInteger(Input(name="investment_amount", party=user))
    age = SecretInteger(Input(name="age", party=user))
    
    # Constants
    hundred = Integer(100)
    zero = Integer(0)
    
    # Financial ratios thresholds
    max_debt_ratio = Integer(36)
    min_savings_ratio = Integer(20)
    emergency_fund_months = Integer(6)
    high_risk_age = Integer(60)
    min_credit_score = Integer(650)
    
    # Penalty and bonus scores
    base_score = Integer(100)
    severe_penalty = Integer(50)
    moderate_penalty = Integer(30)
    minor_penalty = Integer(15)
    bonus_points = Integer(20)
    
    # Calculate core financial metrics
    debt_ratio = (total_debt * hundred) / monthly_income
    savings_ratio = (monthly_savings * hundred) / monthly_income
    disposable_income = monthly_income - monthly_expenses
    emergency_fund = monthly_expenses * emergency_fund_months
    
    # Risk Assessment
    age_risk = (age > high_risk_age).if_else(moderate_penalty, zero)
    credit_risk = (credit_score < min_credit_score).if_else(severe_penalty, zero)
    
    # Investment Profile Assessment
    conservative_allocation = Integer(70)  # 70% safe assets
    aggressive_allocation = Integer(30)    # 30% safe assets
    
    recommended_safe_allocation = (age > high_risk_age).if_else(
        conservative_allocation,
        aggressive_allocation
    )
    
    # Calculate penalties and bonuses
    debt_penalty = (debt_ratio > max_debt_ratio).if_else(moderate_penalty, zero)
    savings_bonus = (savings_ratio > min_savings_ratio).if_else(bonus_points, zero)
    emergency_fund_penalty = (monthly_savings < emergency_fund).if_else(minor_penalty, zero)
    disposable_penalty = (disposable_income < zero).if_else(severe_penalty, zero)
    
    # Calculate comprehensive financial health score
    financial_health_score = (
        base_score 
        - debt_penalty 
        + savings_bonus 
        - emergency_fund_penalty 
        - disposable_penalty 
        - age_risk 
        - credit_risk
    )
    
    # Risk level (0-100, higher means more risky)
    risk_level = (
        (debt_ratio * Integer(40) / hundred) +  # 40% weight to debt
        (age_risk * Integer(30) / hundred) +    # 30% weight to age risk
        (credit_risk * Integer(30) / hundred)   # 30% weight to credit risk
    )
    
    return [
        # User outputs
        Output(financial_health_score, "health_score", user),
        Output(debt_ratio, "debt_ratio", user),
        Output(savings_ratio, "savings_ratio", user),
        Output(disposable_income, "disposable_income", user),
        Output(recommended_safe_allocation, "recommended_safe_allocation", user),
        Output(risk_level, "risk_level", user),
        
        # Financial advisor outputs
        Output(financial_health_score, "client_score", advisor),
        Output(debt_ratio, "client_debt_ratio", advisor),
        Output(savings_ratio, "client_savings_ratio", advisor),
        Output(risk_level, "client_risk_level", advisor),
        Output(age_risk, "client_age_risk", advisor),
        Output(credit_risk, "client_credit_risk", advisor),
        
        # Regulator outputs (limited view)
        Output(risk_level, "entity_risk_level", regulator),
        Output(debt_ratio, "entity_debt_ratio", regulator)
    ]
