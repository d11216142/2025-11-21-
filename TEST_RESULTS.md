# 任務三：執行測試，觀察綠燈與紅燈結果

## 測試結果記錄

### 綠燈（通過）：

執行 Copilot 生成的單元測試後，所有預期的測試案例都通過，顯示為綠燈。

**測試文件：** `test_safe_division.py`  
**被測試函式：** `safe_division.py`

#### 測試執行命令：
```bash
python3 -m unittest test_safe_division.py -v
```

#### 測試結果：
```
test_decimal_division ... ok
test_division_by_zero ... ok
test_large_numbers ... ok
test_negative_division ... ok
test_normal_division ... ok
test_small_numbers ... ok
test_zero_divided_by_number ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

**說明：**
- ✅ 正常的數值相除測試通過
- ✅ 負數相除測試通過
- ✅ 邊界值相除測試通過
- ✅ 除以零的測試通過（返回 None 而非拋出錯誤）

這代表 `safe_division` 函式能正確處理各種情境，包含處理除以零的狀況，使程式不會當機。

---

### 紅燈（失敗）：

當我將 `safe_division` 函式中的「處理除以零」的那一行程式碼註解或刪除後，再次執行單元測試，結果出現紅燈。

**測試文件：** `test_safe_division_no_exception_handling.py`  
**被測試函式：** `safe_division_no_exception_handling.py`

#### 測試執行命令：
```bash
python3 -m unittest test_safe_division_no_exception_handling.py -v
```

#### 測試結果：
```
test_decimal_division ... ok
test_division_by_zero ... ERROR
test_large_numbers ... ok
test_negative_division ... ok
test_normal_division ... ok
test_small_numbers ... ok
test_zero_divided_by_number ... ok

======================================================================
ERROR: test_division_by_zero
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_safe_division_no_exception_handling.py", line 31, in test_division_by_zero
    result = safe_division(10, 0)
  File "safe_division_no_exception_handling.py", line 24, in safe_division
    return a / b
ZeroDivisionError: division by zero

----------------------------------------------------------------------
Ran 7 tests in 0.001s

FAILED (errors=1)
```

---

## 哪個測試失敗？請簡單說明原因：

### 失敗的測試：
**`test_division_by_zero`** - 測試當 b 為零時，safe_division 是否能妥善處理

### 失敗原因：
失敗的是測試「當 b 為零時，safe_division 是否能妥善處理」的單元測試。原因是函式內部**沒有處理除以零的例外**，導致執行時拋出 `ZeroDivisionError` 錯誤，測試無法通過。

### 程式碼比較：

#### ✅ 有例外處理（綠燈）：
```python
def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Warning: Cannot divide {a} by zero. Returning None.")
        return None
```

#### ❌ 無例外處理（紅燈）：
```python
def safe_division(a, b):
    return a / b
    # 沒有 try-except 區塊來捕捉 ZeroDivisionError
```

### 重要性說明：

這證明了**防呆機制（Exception Handling）的重要性**：

1. **穩定性**：有例外處理的程式能夠優雅地處理錯誤情況，不會因為除以零而崩潰
2. **可靠性**：程式會返回一個可預測的值（None），而不是拋出未處理的例外
3. **使用者體驗**：提供友善的警告訊息，讓使用者知道發生了什麼問題
4. **程式安全**：防止程式意外終止，能讓程式更加穩定安全

## 測試覆蓋範圍

單元測試涵蓋以下情境：

1. ✅ **正常除法**：正數相除
2. ✅ **負數除法**：負數與正數、負數與負數的各種組合
3. ✅ **除以零**：最關鍵的測試案例（防呆機制）
4. ✅ **零除以數字**：邊界值測試
5. ✅ **小數除法**：浮點數運算
6. ✅ **大數除法**：極值測試
7. ✅ **精度測試**：小數點精度驗證

## 結論

透過綠燈與紅燈的測試結果對比，我們清楚地看到：

- **綠燈**表示所有測試通過，程式具備完善的錯誤處理機制
- **紅燈**表示測試失敗，暴露了程式中缺少必要的防呆措施

這個實驗充分證明了**單元測試**和**例外處理**在軟體開發中的重要性，它們是確保程式品質和穩定性的關鍵要素。
