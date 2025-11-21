"""
Demonstration script showing green light and red light test results.

This script demonstrates:
1. Green Light (綠燈): All tests pass when safe_division has proper protection
2. Red Light (紅燈): Tests fail when the division by zero protection is removed
"""

import sys


def safe_division_with_protection(a, b):
    """Safe division WITH division by zero protection."""
    if b == 0:
        return None
    return a / b


def safe_division_without_protection(a, b):
    """Safe division WITHOUT division by zero protection (will raise error)."""
    return a / b


def run_green_light_demo():
    """Demonstrate GREEN LIGHT scenario - all tests pass."""
    print("=" * 70)
    print("綠燈測試 (GREEN LIGHT) - With Protection")
    print("=" * 70)
    print()
    
    test_cases = [
        ("Normal division (10 / 2)", 10, 2),
        ("Negative division (-10 / 2)", -10, 2),
        ("Zero numerator (0 / 5)", 0, 5),
        ("Division by zero (10 / 0)", 10, 0),
        ("Float division (7 / 2)", 7, 2),
    ]
    
    all_passed = True
    for description, a, b in test_cases:
        try:
            result = safe_division_with_protection(a, b)
            if b == 0:
                if result is None:
                    print(f"✓ PASS: {description} = None (safely handled)")
                else:
                    print(f"✗ FAIL: {description} = {result} (expected None)")
                    all_passed = False
            else:
                expected = a / b
                if result == expected:
                    print(f"✓ PASS: {description} = {result}")
                else:
                    print(f"✗ FAIL: {description} = {result} (expected {expected})")
                    all_passed = False
        except Exception as e:
            print(f"✗ FAIL: {description} raised {type(e).__name__}: {e}")
            all_passed = False
    
    print()
    if all_passed:
        print("🟢 結果：所有測試通過！(GREEN LIGHT - All tests passed!)")
    else:
        print("🔴 結果：部分測試失敗 (Some tests failed)")
    print()


def run_red_light_demo():
    """Demonstrate RED LIGHT scenario - tests fail without protection."""
    print("=" * 70)
    print("紅燈測試 (RED LIGHT) - Without Protection")
    print("=" * 70)
    print()
    print("⚠️  警告：移除了除以零的保護機制")
    print("⚠️  WARNING: Division by zero protection has been removed")
    print()
    
    test_cases = [
        ("Normal division (10 / 2)", 10, 2),
        ("Negative division (-10 / 2)", -10, 2),
        ("Zero numerator (0 / 5)", 0, 5),
        ("Division by zero (10 / 0)", 10, 0),  # This will fail!
    ]
    
    all_passed = True
    for description, a, b in test_cases:
        try:
            result = safe_division_without_protection(a, b)
            if b == 0:
                # If we get here, something is wrong - should have raised error
                print(f"✗ FAIL: {description} = {result} (expected ZeroDivisionError)")
                all_passed = False
            else:
                expected = a / b
                if result == expected:
                    print(f"✓ PASS: {description} = {result}")
                else:
                    print(f"✗ FAIL: {description} = {result} (expected {expected})")
                    all_passed = False
        except ZeroDivisionError as e:
            print(f"✗ FAIL: {description} raised ZeroDivisionError: {e}")
            print(f"         程式未妥善處理除以零的情況！")
            all_passed = False
        except Exception as e:
            print(f"✗ FAIL: {description} raised {type(e).__name__}: {e}")
            all_passed = False
    
    print()
    if all_passed:
        print("🟢 結果：所有測試通過 (All tests passed)")
    else:
        print("🔴 結果：測試失敗！(RED LIGHT - Tests failed!)")
        print("💡 這證明了防呆機制的重要性 (This demonstrates the importance of fail-safe mechanisms)")
    print()


def main():
    print("\n")
    print("*" * 70)
    print("防呆裝置測試示範 (Fail-Safe Mechanism Demonstration)")
    print("safe_division 函式測試")
    print("*" * 70)
    print("\n")
    
    # Run green light demo first
    run_green_light_demo()
    
    # Run red light demo
    run_red_light_demo()
    
    print("=" * 70)
    print("結論 (CONCLUSION)")
    print("=" * 70)
    print("""
綠燈（通過）：
• 執行單元測試後，所有預期的測試案例（如正常的數值相除、負數相除、邊界值相除）
  都通過，顯示為綠燈。
• 這代表 safe_division 函式能正確處理各種情境，包含處理除以零的狀況，
  使程式不會當機。

紅燈（失敗）：
• 當 safe_division 函式中的「處理除以零」的程式碼被移除後，
  再次執行單元測試，結果出現紅燈。
• 針對除以零的單元測試會失敗，因為程式直接丟出 ZeroDivisionError，
  未被妥善處理。

這個示範清楚說明了防呆機制（Fail-Safe Mechanism）的重要性！
    """)


if __name__ == "__main__":
    main()
