---
name: health-insurance-analyzer
description: Analyzes health insurance policy documents (PDF, DOCX, or text) to extract and organize key information including coverage benefits, deductibles, out-of-pocket maximums, copays, coinsurance, covered services, exclusions, and benefit timelines. Use when users need to understand their health insurance policy details, compare plans, calculate costs, or identify when to use specific benefits for maximum value.
---

# Health Insurance Analyzer

This skill helps extract, organize, and present health insurance policy information in a clear, actionable format.

## Analysis Process

Follow these steps to analyze a health insurance document:

### 1. Extract Policy Information

Read the insurance document and identify these key sections:

**Basic Policy Information:**
- Plan name and type (HMO, PPO, EPO, POS, HDHP)
- Policy/member ID format
- Insurance carrier
- Policy year/effective dates
- Network information

**Financial Responsibility:**
- Annual deductible (individual and family)
- Out-of-pocket maximum (individual and family)
- Premium amount (if stated)
- Whether deductible applies to all services or specific ones

**Cost-Sharing Details:**
- Copayments for different service types
- Coinsurance percentages
- When copay vs coinsurance applies
- Differences between in-network and out-of-network

### 2. Categorize Benefits

Organize benefits into clear categories:

**Preventive Care:**
- Annual wellness visits
- Screenings (cancer, diabetes, cholesterol, etc.)
- Immunizations
- Well-child visits
- Note: Usually 100% covered, no deductible

**Primary & Specialty Care:**
- Primary care physician visits
- Specialist visits
- Urgent care
- Telehealth/virtual visits

**Diagnostic Services:**
- Lab work
- X-rays and imaging
- Diagnostic tests

**Hospital Services:**
- Inpatient hospitalization
- Outpatient surgery
- Emergency room
- Ambulance services

**Prescription Drugs:**
- Tier structure (generic, preferred brand, non-preferred, specialty)
- Retail vs mail-order differences
- Prior authorization requirements

**Mental Health & Substance Abuse:**
- Therapy/counseling sessions
- Inpatient mental health treatment
- Substance abuse treatment

**Additional Benefits:**
- Physical therapy
- Chiropractic care
- Durable medical equipment
- Home health care
- Maternity care
- Vision and dental (if included)

### 3. Identify Timeline-Sensitive Benefits

Highlight benefits with timing considerations:

**Annual Reset Items:**
- Deductible resets (usually January 1)
- Out-of-pocket max resets
- Preventive care allowances (annual physicals, screenings)

**Limited Visit Benefits:**
- Chiropractic care (e.g., 20 visits per year)
- Physical therapy (e.g., 30 visits per year)
- Acupuncture (e.g., 12 visits per year)

**One-Time or Periodic Benefits:**
- Annual eye exams
- Routine colonoscopy (every 10 years after 45)
- Mammograms (annual after 40)
- Dental cleanings (if included, typically 2 per year)

**Use-It-Or-Lose-It:**
- FSA/HSA contribution deadlines
- Grace periods for claims

### 4. Calculate Maximum Benefit Scenarios

Help users understand their potential costs:

**Best-Case Scenario (Preventive Only):**
- Premium only
- Free preventive services

**Moderate Use:**
- Premium + typical copays
- Example: 4 PCP visits, 1 specialist, annual preventive

**Maximum Out-of-Pocket:**
- Premium + out-of-pocket max
- When this is reached
- What happens after

**Key Cost Thresholds:**
- At what point does deductible get met with typical services
- When to schedule elective procedures (before/after deductible met)

### 5. Flag Important Exclusions & Limitations

Note what's NOT covered:

- Cosmetic procedures
- Experimental treatments
- Out-of-network providers (if applicable)
- Services requiring prior authorization
- Annual or lifetime limits on specific services

### 6. Create Timeline Recommendations

Suggest optimal timing for benefits:

**Q1 (January-March):**
- Schedule annual preventive visits early
- Plan for deductible reset
- Review if high-deductible items should be scheduled later

**Q2-Q3 (April-September):**
- Mid-year check on deductible progress
- Schedule non-urgent procedures if deductible nearly met

**Q4 (October-December):**
- Use remaining limited visits (PT, chiropractic)
- Schedule procedures if close to out-of-pocket max
- Max out FSA/HSA before year-end

## Output Format

Present findings in this structure:

### 1. Policy Summary
Quick reference table with plan type, deductibles, out-of-pocket max, key copays

### 2. Your Financial Responsibility
Clear breakdown of what you pay and when

### 3. Covered Benefits by Category
Organized list with specific cost-sharing for each service

### 4. Timeline & Maximizing Benefits
Month-by-month guidance on when to use benefits

### 5. Important Limitations & Exclusions
What to watch out for

### 6. Cost Scenarios
Examples of total annual costs under different usage patterns

## Handling Complex Documents

**If document is lengthy:**
- Use the references/extraction_guide.md for structured extraction patterns
- Process section by section
- Verify all numbers are accurately captured

**If information is unclear:**
- Note ambiguities
- Suggest what to clarify with insurance company
- Make reasonable assumptions but state them clearly

**If comparing multiple plans:**
- Create side-by-side comparison tables
- Highlight key differences
- Calculate breakeven points

## Common Pitfalls to Avoid

- Don't confuse deductible with out-of-pocket maximum
- Remember some services don't apply to deductible
- Note difference between individual and family limits
- Check if preventive care is truly $0 or if there are exceptions
- Verify in-network vs out-of-network differences
