# 2025-11-21-

## Safe Division Function

This repository contains a Python implementation of a `safe_division` function that prevents division by zero errors.

### Features

- **Division by zero protection**: Raises a `ValueError` when attempting to divide by zero
- **Comprehensive error handling**: Provides clear error messages
- **Full test coverage**: Includes unit tests for various scenarios

### Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns 5.0

# Division by zero (raises ValueError)
try:
    result = safe_division(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Prints: Error: Cannot divide by zero
```

### Running the Code

To run the example:
```bash
python3 safe_division.py
```

To run the tests:
```bash
python3 -m unittest test_safe_division.py -v
```

### Files

- `safe_division.py`: Main module containing the safe division function
- `test_safe_division.py`: Unit tests for the safe division function
# 任務三：執行測試，觀察綠燈與紅燈結果

這個專案示範了單元測試中的綠燈（測試通過）和紅燈（測試失敗）結果，以及例外處理（Exception Handling）的重要性。

## 專案檔案

### 主要程式檔案
- **`safe_division.py`** - 具有完整例外處理的安全除法函式
- **`safe_division_no_exception_handling.py`** - 沒有例外處理的版本（用於示範紅燈）

### 測試檔案
- **`test_safe_division.py`** - 完整的單元測試（綠燈示範）
- **`test_safe_division_no_exception_handling.py`** - 針對無例外處理版本的測試（紅燈示範）

### 文件
- **`TEST_RESULTS.md`** - 完整的測試結果記錄和分析

## 快速開始

### 執行綠燈測試（所有測試通過）
```bash
python3 -m unittest test_safe_division.py -v
```

### 執行紅燈測試（顯示測試失敗）
```bash
python3 -m unittest test_safe_division_no_exception_handling.py -v
```

## 測試結果摘要

### ✅ 綠燈（有例外處理）
- 所有 7 個測試通過
- 程式能安全處理除以零的情況
- 返回 `None` 而不是崩潰

### ❌ 紅燈（無例外處理）
- 6 個測試通過，1 個測試失敗
- `test_division_by_zero` 測試失敗
- 拋出 `ZeroDivisionError` 導致程式崩潰

## 學習要點

1. **例外處理的重要性**：適當的錯誤處理能防止程式崩潰
2. **單元測試的價值**：測試能夠及早發現程式中的問題
3. **防呆機制**：讓程式更加穩定、安全和可靠
4. **測試驅動開發**：綠燈和紅燈幫助我們驗證程式的正確性

詳細的測試結果和分析請參見 [TEST_RESULTS.md](TEST_RESULTS.md)。
