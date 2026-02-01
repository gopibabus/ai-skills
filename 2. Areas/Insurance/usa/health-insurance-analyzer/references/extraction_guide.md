# Health Insurance Document Extraction Guide

This guide provides structured patterns for extracting information from health insurance documents.

## Section Identification Patterns

Health insurance documents typically organize information in these sections:

### Summary of Benefits and Coverage (SBC)
- Usually first 2-4 pages
- Contains high-level overview
- Standardized format required by ACA
- Key tables: deductibles, out-of-pocket max, copays

### Schedule of Benefits
- Detailed service-by-service breakdown
- Often organized alphabetically or by category
- Contains specific dollar amounts or percentages
- Look for footnotes explaining coverage details

### Exclusions and Limitations
- What's NOT covered
- Annual visit limits
- Prior authorization requirements
- Usually near end of document

### Definitions
- Medical terminology
- Plan-specific terms
- Coverage criteria

## Key Terms to Search For

When extracting information, search for these terms:

### Financial Terms
- "Deductible" (individual/family, in-network/out-of-network)
- "Out-of-pocket maximum" or "out-of-pocket limit"
- "Coinsurance"
- "Copay" or "copayment"
- "Premium"
- "Allowed amount" or "negotiated rate"

### Coverage Terms
- "Covered services"
- "Preventive care"
- "Medically necessary"
- "Prior authorization" or "pre-authorization"
- "Formulary" (for prescriptions)
- "In-network" vs "out-of-network"

### Benefit Limits
- "Annual maximum"
- "Lifetime maximum"
- "Visit limit"
- "Calendar year"
- "Plan year"

## Common Document Formats

### Table-Based Documents
Extract using column headers:
- Service/Benefit
- In-Network Cost
- Out-of-Network Cost
- Additional Information

### Narrative-Style Documents
Look for structure like:
"[Service Name]: You pay [amount] after deductible"
"[Service Name]: No charge (preventive care)"

### Grid/Matrix Format
Common for prescription drug benefits:
- Rows: Tier levels (1-4)
- Columns: Retail vs Mail-order, 30-day vs 90-day supply

## Data Validation Checks

After extraction, verify:

1. **Consistency checks:**
   - Does individual deductible ≤ family deductible?
   - Does out-of-pocket max ≥ deductible?
   - Are in-network costs ≤ out-of-network costs?

2. **Completeness checks:**
   - Are both individual AND family limits provided?
   - Are both in-network AND out-of-network costs listed?
   - Is the plan year clearly stated?

3. **Logic checks:**
   - If service says "after deductible," is deductible amount stated?
   - If coinsurance applies, is the percentage specified?
   - Are preventive services marked as $0 or 100% covered?

## Handling Ambiguous Information

**When multiple values are listed:**
- Check if it's individual vs family
- Check if it's in-network vs out-of-network
- Check if it's different tiers (Bronze, Silver, Gold)

**When information seems missing:**
- Check for footnotes or asterisks
- Look in definitions section
- May need to note as "Not specified - verify with insurer"

**When terms are unclear:**
- Use context clues from surrounding text
- Cross-reference with definitions section
- Default to conservative interpretation (higher cost to patient)

## Extraction Template

Use this template structure when extracting data:

```
POLICY BASICS
Plan Name: [extract]
Plan Type: [HMO/PPO/EPO/HDHP/etc]
Insurance Carrier: [extract]
Policy Year: [extract]
Network: [extract]

DEDUCTIBLES
Individual In-Network: $[amount]
Family In-Network: $[amount]
Individual Out-of-Network: $[amount]
Family Out-of-Network: $[amount]
Notes: [what counts toward deductible]

OUT-OF-POCKET MAXIMUM
Individual In-Network: $[amount]
Family In-Network: $[amount]
Individual Out-of-Network: $[amount]
Family Out-of-Network: $[amount]
Notes: [what counts toward OOP max]

PREVENTIVE CARE
Annual Physical: [cost]
Immunizations: [cost]
Cancer Screenings: [cost]
Well-Child Visits: [cost]
Notes: [any limits or exclusions]

PRIMARY & SPECIALTY CARE
Primary Care Visit: [copay/coinsurance]
Specialist Visit: [copay/coinsurance]
Urgent Care: [copay/coinsurance]
Telehealth: [copay/coinsurance]

HOSPITAL SERVICES
Emergency Room: [copay/coinsurance]
Inpatient Hospital: [copay/coinsurance per day/stay]
Outpatient Surgery: [copay/coinsurance]
Ambulance: [copay/coinsurance]

DIAGNOSTIC SERVICES
Lab Work: [cost]
X-rays: [cost]
CT/PET Scans: [cost]
MRI: [cost]

PRESCRIPTIONS
Tier 1 (Generic): [copay] retail / [copay] mail
Tier 2 (Preferred Brand): [copay] retail / [copay] mail
Tier 3 (Non-Preferred): [copay] retail / [copay] mail
Tier 4 (Specialty): [copay/coinsurance]

MENTAL HEALTH
Outpatient Therapy: [copay/coinsurance]
Inpatient Mental Health: [copay/coinsurance]

ADDITIONAL SERVICES
Physical Therapy: [copay] ([X] visits/year limit)
Chiropractic: [copay] ([X] visits/year limit)
Acupuncture: [copay] ([X] visits/year limit)
Durable Medical Equipment: [coinsurance]
Home Health Care: [cost]

MATERNITY (if applicable)
Prenatal Care: [cost]
Delivery: [cost]
Postnatal Care: [cost]

VISION & DENTAL (if included)
Eye Exam: [cost] ([frequency])
Glasses/Contacts: [allowance]
Dental Cleaning: [cost] ([frequency])

EXCLUSIONS & LIMITATIONS
[List key exclusions]

PRIOR AUTHORIZATION REQUIRED
[List services requiring pre-auth]
```

## Special Considerations

### High-Deductible Health Plans (HDHPs)
- Note HSA eligibility
- Track HSA contribution limits
- Preventive care usually exempt from deductible

### HMO Plans
- Emphasize need for PCP referrals
- Note out-of-network coverage (usually only emergency)
- Check if specific hospitals/providers required

### PPO Plans
- Clear distinction between in-network and out-of-network
- May have separate deductibles for each
- Note balance billing risk for out-of-network

### Medicare Advantage Plans
- Note Parts A, B, C, D coverage
- Star ratings if mentioned
- Special enrollment periods
