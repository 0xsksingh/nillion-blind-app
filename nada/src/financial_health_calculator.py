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
    
    # Create constant values as SecretIntegers
    hundred = SecretInteger(100)
    thirty_six = SecretInteger(36)
    twenty = SecretInteger(20)
    zero = SecretInteger(0)
    base_score = SecretInteger(100)
    penalty_thirty = SecretInteger(30)
    penalty_fifty = SecretInteger(50)
    
    # Calculate financial metrics
    # Debt ratio = (total_debt * 100) / monthly_income
    debt_ratio = (total_debt * hundred) / monthly_income
    
    # Savings ratio = (monthly_savings * 100) / monthly_income
    savings_ratio = (monthly_savings * hundred) / monthly_income
    
    # Disposable income
    disposable_income = monthly_income - monthly_expenses
    
    # Calculate penalties and bonuses
    debt_penalty = If(
        debt_ratio > thirty_six,
        Then=penalty_thirty,
        Else=zero
    )
    
    savings_bonus = If(
        savings_ratio > twenty,
        Then=twenty,
        Else=zero
    )
    
    disposable_penalty = If(
        disposable_income < zero,
        Then=penalty_fifty,
        Else=zero
    )
    
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