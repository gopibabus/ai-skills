#!/usr/bin/env python3
"""
Health Insurance Cost Calculator

Calculates total annual costs under different usage scenarios.
Helps users understand their potential healthcare expenses.
"""

class HealthInsuranceCostCalculator:
    def __init__(self, policy_data):
        """
        Initialize calculator with policy data.
        
        Args:
            policy_data (dict): Dictionary containing:
                - annual_premium: Monthly or annual premium
                - deductible: Annual deductible
                - oop_max: Out-of-pocket maximum
                - copays: Dict of service copays
                - coinsurance: Coinsurance percentage (e.g., 0.20 for 20%)
        """
        self.premium = policy_data.get('annual_premium', 0)
        self.deductible = policy_data.get('deductible', 0)
        self.oop_max = policy_data.get('oop_max', 0)
        self.copays = policy_data.get('copays', {})
        self.coinsurance = policy_data.get('coinsurance', 0.20)
        
    def calculate_scenario(self, services):
        """
        Calculate total cost for a given service usage scenario.
        
        Args:
            services (list): List of service tuples (service_type, count, cost_per_service)
            
        Returns:
            dict: Breakdown of costs
        """
        total_copays = 0
        deductible_charges = 0
        coinsurance_charges = 0
        
        # Track deductible met
        deductible_remaining = self.deductible
        
        for service_type, count, cost_per_service in services:
            # Check if service has copay
            if service_type in self.copays:
                total_copays += self.copays[service_type] * count
            else:
                # Apply to deductible first
                for _ in range(count):
                    if deductible_remaining > 0:
                        applied_to_deductible = min(cost_per_service, deductible_remaining)
                        deductible_charges += applied_to_deductible
                        deductible_remaining -= applied_to_deductible
                        
                        # Remaining goes to coinsurance
                        if cost_per_service > applied_to_deductible:
                            coinsurance_charges += (cost_per_service - applied_to_deductible) * self.coinsurance
                    else:
                        # Deductible met, only coinsurance applies
                        coinsurance_charges += cost_per_service * self.coinsurance
        
        # Calculate total out-of-pocket
        total_oop = total_copays + deductible_charges + coinsurance_charges
        
        # Cap at out-of-pocket maximum
        if total_oop > self.oop_max:
            total_oop = self.oop_max
            
        # Add premium
        total_annual_cost = self.premium + total_oop
        
        return {
            'premium': self.premium,
            'copays': total_copays,
            'deductible_paid': min(deductible_charges, self.deductible),
            'coinsurance': coinsurance_charges,
            'total_out_of_pocket': total_oop,
            'total_annual_cost': total_annual_cost,
            'oop_max_reached': total_oop >= self.oop_max
        }
    
    def preventive_only_scenario(self):
        """Calculate cost for using only preventive care (usually free)."""
        return {
            'scenario': 'Preventive Care Only',
            'services': 'Annual physical, routine screenings',
            'costs': {
                'premium': self.premium,
                'copays': 0,
                'deductible_paid': 0,
                'coinsurance': 0,
                'total_out_of_pocket': 0,
                'total_annual_cost': self.premium,
                'oop_max_reached': False
            }
        }
    
    def moderate_use_scenario(self):
        """Calculate cost for moderate healthcare usage."""
        services = [
            ('primary_care', 4, 200),  # 4 PCP visits
            ('specialist', 2, 300),     # 2 specialist visits
            ('urgent_care', 1, 400),    # 1 urgent care visit
            ('lab_work', 3, 150),       # 3 lab tests
        ]
        
        return {
            'scenario': 'Moderate Use',
            'services': '4 PCP visits, 2 specialist visits, 1 urgent care, 3 lab tests',
            'costs': self.calculate_scenario(services)
        }
    
    def high_use_scenario(self):
        """Calculate cost for high healthcare usage."""
        services = [
            ('primary_care', 6, 200),
            ('specialist', 4, 300),
            ('emergency_room', 1, 2000),
            ('outpatient_surgery', 1, 8000),
            ('imaging', 2, 1500),
            ('lab_work', 8, 150),
        ]
        
        return {
            'scenario': 'High Use (Outpatient Surgery)',
            'services': '6 PCP, 4 specialist, 1 ER, outpatient surgery, imaging, labs',
            'costs': self.calculate_scenario(services)
        }
    
    def max_oop_scenario(self):
        """Calculate worst-case scenario hitting out-of-pocket max."""
        return {
            'scenario': 'Maximum Out-of-Pocket',
            'services': 'Major medical event (hospitalization, surgery, etc.)',
            'costs': {
                'premium': self.premium,
                'copays': 0,
                'deductible_paid': self.deductible,
                'coinsurance': self.oop_max - self.deductible,
                'total_out_of_pocket': self.oop_max,
                'total_annual_cost': self.premium + self.oop_max,
                'oop_max_reached': True
            }
        }
    
    def compare_all_scenarios(self):
        """Generate comparison of all scenarios."""
        return {
            'preventive_only': self.preventive_only_scenario(),
            'moderate_use': self.moderate_use_scenario(),
            'high_use': self.high_use_scenario(),
            'max_oop': self.max_oop_scenario()
        }
    
    def format_currency(self, amount):
        """Format number as currency."""
        return f"${amount:,.2f}"
    
    def print_scenario_comparison(self):
        """Print formatted comparison of all scenarios."""
        scenarios = self.compare_all_scenarios()
        
        print("\n" + "="*80)
        print("HEALTH INSURANCE COST SCENARIOS - ANNUAL COMPARISON")
        print("="*80 + "\n")
        
        for scenario_name, scenario in scenarios.items():
            print(f"\n{scenario['scenario'].upper()}")
            print("-" * 60)
            print(f"Services: {scenario['services']}")
            print(f"\nCost Breakdown:")
            costs = scenario['costs']
            print(f"  Annual Premium:        {self.format_currency(costs['premium'])}")
            print(f"  Copays:                {self.format_currency(costs['copays'])}")
            print(f"  Deductible:            {self.format_currency(costs['deductible_paid'])}")
            print(f"  Coinsurance:           {self.format_currency(costs['coinsurance'])}")
            print(f"  Total Out-of-Pocket:   {self.format_currency(costs['total_out_of_pocket'])}")
            print(f"  {'='*40}")
            print(f"  TOTAL ANNUAL COST:     {self.format_currency(costs['total_annual_cost'])}")
            
            if costs['oop_max_reached']:
                print(f"  * Out-of-pocket maximum reached")
        
        print("\n" + "="*80 + "\n")


# Example usage
if __name__ == "__main__":
    # Example policy data
    example_policy = {
        'annual_premium': 4800,  # $400/month
        'deductible': 2000,
        'oop_max': 6000,
        'copays': {
            'primary_care': 25,
            'specialist': 50,
            'urgent_care': 75,
            'emergency_room': 300
        },
        'coinsurance': 0.20  # 20% after deductible
    }
    
    calculator = HealthInsuranceCostCalculator(example_policy)
    calculator.print_scenario_comparison()
