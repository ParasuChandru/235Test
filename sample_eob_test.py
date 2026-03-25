import datetime
import pytest

def get_mock_eob():
    return {
        "member_id": "123456789",
        "member_name": "Jane Doe",
        "claim_id": "CLM0001",
        "date_of_service": "2026-03-01",
        "provider": "Springfield Clinic",
        "total_charge": 175.00,
        "allowed_amount": 160.00,
        "paid_amount": 120.00,
        "notices": [
            "This EOB is generated under CMS Medicare Advantage HMO rules.",
            "Review your benefits and contact us if discrepancies are found."
        ],
        "disclosures": [
            "Processed according to Test insurance policy and CMS guidelines."
        ],
        "distribution_date": str(datetime.date.today()),
        "readability_score": 73,  # Flesch Reading Ease, example metric
    }


# tests
def test_required_notices():
    eob = get_mock_eob()
    notices = " \n".join(eob["notices"])
    assert "CMS Medicare Advantage HMO" in notices, "Missing CMS notice"

def test_required_disclosures():
    eob = get_mock_eob()
    assert any("CMS" in d for d in eob["disclosures"]), "Missing CMS disclosure"

def test_claim_content():
    eob = get_mock_eob()
    for field in ["member_id", "claim_id", "provider", "total_charge", "allowed_amount", "paid_amount"]:
        assert eob[field], f"Missing {field}"

def test_distribution_timeline():
    eob = get_mock_eob()
    dist_date = datetime.datetime.strptime(eob["distribution_date"], "%Y-%m-%d").date()
    assert (datetime.date.today() - dist_date).days <= 5, "EOB not distributed within CMS timeline"

def test_readability_score():
    eob = get_mock_eob()
    assert eob["readability_score"] >= 60, "EOB does not meet readability standards"
