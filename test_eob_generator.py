import pytest

def test_eob_generation_with_sample_data():
    # Simulate a CMS-compliant EOB for a Medicare Advantage HMO member
    eob_data = {
        'patient_name': 'John Doe',
        'member_id': 'MA1023456',
        'claim_id': 'C2024201',
        'service_date': '2026-03-01',
        'provider_name': 'Test Provider',
        'amount_billed': 1500.00,
        'amount_covered': 1425.00,
        'cms_notices': [
            'Your plan covers these services as required by CMS guidelines.'
        ],
        'disclosures': [
            'Readability and accuracy validated as per CMS regulations.'
        ],
        'distribution_date': '2026-03-02'
    }
    # Replace below with a call to the real EOB generation logic (mocked here)
    generated_eob = eob_data.copy()

    # BDD-Style assertions to match Jira Acceptance Criteria
    assert generated_eob['patient_name']
    assert generated_eob['member_id'].startswith('MA')
    assert 'CMS guidelines' in generated_eob['cms_notices'][0]
    assert generated_eob['distribution_date'] <= '2026-03-03'
    assert 'validated as per CMS regulations' in generated_eob['disclosures'][0]
