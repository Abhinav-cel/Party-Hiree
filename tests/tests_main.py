import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantity import validate_quantity

def test_validate_quantity():
    # --- Arrange ---
    # Expected error messages or booleans based on your test plan
    expected_fail = False
    expected_pass = True
    
    # --- Act ---
    # 1. Invalid Inputs (Text and Decimals)
    txt_input = validate_quantity("XLII")
    dec_input = validate_quantity("1.5")
    
    # 2. Out of Bounds Boundaries
    low_out_input = validate_quantity("0")
    hi_out_input  = validate_quantity("501")
    
    # 3. Expected Valid Boundaries (1 and 500)
    low_bound_input = validate_quantity("1")
    hi_bound_input  = validate_quantity("500")
    
    # 4. Normal Valid Data
    normal_input = validate_quantity("2")

    # --- Assert ---
    # Assert Invalid Inputs Fail
    assert txt_input == expected_fail
    assert dec_input == expected_fail
    
    # Assert Out of Bound Limits Fail
    assert low_out_input == expected_fail
    assert hi_out_input  == expected_fail
    
    # Assert Exact Limits Pass
    assert low_bound_input == expected_pass
    assert hi_bound_input  == expected_pass
    
    # Assert Normal Values Pass
    assert normal_input == expected_pass