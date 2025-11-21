#!/usr/bin/env python3
"""
Script to demonstrate RED LIGHT vs GREEN LIGHT test results.

This script shows what happens when you:
1. Run tests WITH protection (GREEN LIGHT ✅)
2. Run tests WITHOUT protection (RED LIGHT ❌)

Usage:
    python3 demonstrate_red_light.py
"""

import subprocess
import sys
import shutil
import os


def run_tests(version_name, use_protection=True):
    """Run tests and return the result."""
    print("=" * 70)
    if use_protection:
        print(f"🟢 綠燈測試 (GREEN LIGHT) - {version_name}")
        print("使用 safe_division.py (有防呆保護)")
    else:
        print(f"🔴 紅燈測試 (RED LIGHT) - {version_name}")
        print("使用 safe_division_no_protection.py (無防呆保護)")
    print("=" * 70)
    print()
    
    # Backup original file (remove old backup if exists)
    backup_file = 'safe_division_backup.py'
    if os.path.exists(backup_file):
        os.remove(backup_file)
    if os.path.exists('safe_division.py'):
        shutil.copy('safe_division.py', backup_file)
    
    try:
        if not use_protection:
            # Temporarily replace with no-protection version
            if os.path.exists('safe_division_no_protection.py'):
                try:
                    shutil.copy('safe_division_no_protection.py', 'safe_division.py')
                    print("⚠️  已暫時移除防呆保護機制")
                    print("⚠️  Division by zero protection temporarily removed\n")
                except (IOError, OSError) as e:
                    print(f"❌ Error replacing file: {e}")
                    return False
        
        # Run the tests
        result = subprocess.run(
            [sys.executable, '-m', 'unittest', 'test_safe_division', '-v'],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ 測試結果：所有測試通過 (All tests passed)")
        else:
            print("\n❌ 測試結果：測試失敗 (Tests failed)")
        
        print()
        return result.returncode == 0
        
    finally:
        # Restore original file safely
        backup_file = 'safe_division_backup.py'
        if os.path.exists(backup_file):
            try:
                # Remove current file if it exists
                if os.path.exists('safe_division.py'):
                    os.remove('safe_division.py')
                shutil.move(backup_file, 'safe_division.py')
            except (IOError, OSError) as e:
                print(f"⚠️  Warning: Could not restore original file: {e}")
                print(f"   Backup is at: {backup_file}")


def main():
    print("\n")
    print("*" * 70)
    print("防呆裝置測試示範 - 綠燈 vs 紅燈")
    print("Fail-Safe Mechanism Test Demonstration - Green Light vs Red Light")
    print("*" * 70)
    print("\n")
    
    # Test 1: With protection (GREEN LIGHT)
    green_passed = run_tests("With Protection", use_protection=True)
    
    print("\n" + "=" * 70)
    print("按 Enter 繼續查看紅燈測試... (Press Enter to see RED LIGHT test...)")
    print("=" * 70)
    input()
    print("\n")
    
    # Test 2: Without protection (RED LIGHT)
    red_passed = run_tests("Without Protection", use_protection=False)
    
    # Summary
    print("\n")
    print("=" * 70)
    print("📊 測試結果總結 (SUMMARY)")
    print("=" * 70)
    print()
    
    if green_passed and not red_passed:
        print("✅ 綠燈測試：通過 (GREEN LIGHT: Passed)")
        print("❌ 紅燈測試：失敗 (RED LIGHT: Failed)")
        print()
        print("🎯 結論：防呆機制成功！")
        print("   Conclusion: Fail-safe mechanism works correctly!")
        print()
        print("說明：")
        print("• 有防呆保護時，程式能安全處理除以零的情況")
        print("• 移除防呆保護後，程式會因為 ZeroDivisionError 而失敗")
        print("• 這證明了防呆機制的重要性！")
    elif green_passed and red_passed:
        print("⚠️  警告：兩個測試都通過了")
        print("   這表示紅燈測試可能沒有正確測試除以零的情況")
    else:
        print("❌ 綠燈測試應該要通過但卻失敗了")
        print("   請檢查 safe_division.py 的實作")
    
    print()


if __name__ == "__main__":
    main()
