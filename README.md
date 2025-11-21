# 防呆裝置說明 (Fail-Safe Mechanism Demonstration)

這個專案展示了如何實作防呆機制，以 Python 的 `safe_division` 函式為例，防止除以零的錯誤。

## 任務一：撰寫防呆 safe_division 函式 ✅

### 檔案：`safe_division.py`

實作了 `safe_division(a, b)` 函式，具有以下特性：

- 接受兩個參數 `a`（被除數）和 `b`（除數）
- 當 `b != 0` 時，返回 `a / b` 的結果
- 當 `b == 0` 時，返回 `None`，防止 `ZeroDivisionError`
- 包含完整的文檔字串和使用範例

### 使用範例

```python
from safe_division import safe_division

# 正常除法
result = safe_division(10, 2)  # 返回 5.0

# 負數除法
result = safe_division(-10, 2)  # 返回 -5.0

# 除以零（安全處理）
result = safe_division(10, 0)  # 返回 None（不會崩潰）
```

## 任務二：自動生成單元測試 ✅

### 檔案：`test_safe_division.py`

使用 Python 的內建 `unittest` 框架，生成了全面的單元測試，涵蓋：

1. **正常數值相除**
   - 正數除法
   - 負數除法
   - 浮點數除法

2. **邊界值測試**
   - 零作為被除數
   - 極大數值
   - 極小數值

3. **防呆機制測試**
   - 除以零的情況（關鍵測試）

### 執行測試

```bash
# 執行所有測試
python3 -m unittest test_safe_division -v

# 或直接執行測試檔案
python3 test_safe_division.py
```

## 任務三：觀察綠燈與紅燈結果 ✅

### 快速開始

有三種方式可以觀察綠燈與紅燈的測試結果：

#### 方法 1：互動式示範（推薦）⭐

```bash
python3 demonstrate_red_light.py
```

這個腳本會自動切換有/無防呆保護的版本，讓你清楚看到綠燈和紅燈的差異。

#### 方法 2：快速示範

```bash
python3 test_results_demo.py
```

快速展示兩種情境的測試結果，無需互動。

#### 方法 3：手動測試

查看 [如何觀察綠燈與紅燈.md](./如何觀察綠燈與紅燈.md) 了解詳細步驟。

### 綠燈（通過）🟢

執行單元測試後，所有預期的測試案例都通過，顯示為綠燈：

```
✓ PASS: Normal division (10 / 2) = 5.0
✓ PASS: Negative division (-10 / 2) = -5.0
✓ PASS: Zero numerator (0 / 5) = 0.0
✓ PASS: Division by zero (10 / 0) = None (safely handled)
✓ PASS: Float division (7 / 2) = 3.5

🟢 結果：所有測試通過！(GREEN LIGHT - All tests passed!)
```

這代表 `safe_division` 函式能正確處理各種情境，包含處理除以零的狀況，使程式不會當機。

### 紅燈（失敗）🔴

當 `safe_division` 函式中的「處理除以零」的程式碼被移除後，再次執行測試會出現紅燈：

```
✓ PASS: Normal division (10 / 2) = 5.0
✓ PASS: Negative division (-10 / 2) = -5.0
✓ PASS: Zero numerator (0 / 5) = 0.0
✗ FAIL: Division by zero (10 / 0) raised ZeroDivisionError: division by zero
         程式未妥善處理除以零的情況！

🔴 結果：測試失敗！(RED LIGHT - Tests failed!)
```

針對除以零的單元測試會失敗，因為程式直接丟出 `ZeroDivisionError`，未被妥善處理。

## 測試結果摘要

| 測試案例 | 帶防呆機制 | 無防呆機制 |
|---------|-----------|-----------|
| 正常除法 (10 / 2) | ✅ 通過 | ✅ 通過 |
| 負數除法 (-10 / 2) | ✅ 通過 | ✅ 通過 |
| 零被除數 (0 / 5) | ✅ 通過 | ✅ 通過 |
| 除以零 (10 / 0) | ✅ 通過 (返回 None) | ❌ 失敗 (ZeroDivisionError) |
| 浮點數除法 (7 / 2) | ✅ 通過 | ✅ 通過 |

## 結論

這個示範清楚說明了**防呆機制（Fail-Safe Mechanism）的重要性**：

1. ✅ **有防呆機制**：程式能安全處理各種輸入，包括錯誤情況，不會崩潰
2. ❌ **無防呆機制**：程式在遇到除以零時會拋出異常，導致程式中斷

防呆裝置確保了程式的**健壯性（Robustness）**和**可靠性（Reliability）**，是軟體工程中的最佳實踐。

## 專案結構

```
.
├── README.md                      # 專案說明文件
├── safe_division.py               # 防呆函式實作（有保護）✅
├── safe_division_no_protection.py # 無保護版本（僅供示範）⚠️
├── test_safe_division.py          # 單元測試
├── test_results_demo.py           # 快速示範腳本
├── demonstrate_red_light.py       # 互動式示範腳本（推薦）⭐
└── 如何觀察綠燈與紅燈.md           # 詳細操作說明
```

## 環境需求

- Python 3.6 或更高版本
- 內建 `unittest` 模組（Python 標準庫）

## 作者

GitHub Copilot Implementation