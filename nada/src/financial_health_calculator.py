from nada_dsl import *

def nada_main():
    # Define parties
    user = Party(name="Party1")
    advisor = Party(name="Party2")
    
    # Secure inputs from user
    monthly_income = SecretInteger(Input(name="monthly_income", party=user))
    total_debt = SecretInteger(Input(name="total_debt", party=user))
    monthly_savings = SecretInteger(Input(name="monthly_savings", party=user))
    monthly_expenses = SecretInteger(Input(name="monthly_expenses", party=user))
    
    # Create constant values
    hundred = Integer(100)
    thirty_six = Integer(36)
    twenty = Integer(20)
    zero = Integer(0)
    base_score = Integer(100)
    penalty_thirty = Integer(30)
    penalty_fifty = Integer(50)
    
    # Calculate financial metrics
    debt_ratio = (total_debt * hundred) / monthly_income
    savings_ratio = (monthly_savings * hundred) / monthly_income
    disposable_income = monthly_income - monthly_expenses
    
    # Calculate penalties and bonuses
    debt_penalty = (debt_ratio > thirty_six).if_else(penalty_thirty, zero)
    savings_bonus = (savings_ratio > twenty).if_else(twenty, zero)
    disposable_penalty = (disposable_income < zero).if_else(penalty_fifty, zero)
    
    # Calculate final score
    financial_health_score = base_score - debt_penalty + savings_bonus - disposable_penalty
    
    return [
        Output(financial_health_score, "health_score", user),
        Output(debt_ratio, "debt_ratio", user),
        Output(savings_ratio, "savings_ratio", user),
        Output(disposable_income, "disposable_income", user),
        Output(financial_health_score, "client_score", advisor),
        Output(debt_ratio, "client_debt_ratio", advisor),
        Output(savings_ratio, "client_savings_ratio", advisor)
    ]