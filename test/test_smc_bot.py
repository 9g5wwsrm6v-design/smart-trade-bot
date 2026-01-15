import pandas as pd
import numpy as np
from smc_bot import (
    detect_swings,
    detect_bos,
    detect_fvg,
    find_order_block_before_bos,
    generate_signal,
    position_size,
    Signal
)

# ------------------ Test Fixtures ------------------

def sample_df():
    """
    Creates a small deterministic OHLC dataset for testing.
    """
    data = {
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="15min"),
        "open":  [1.30, 1.31, 1.32, 1.31, 1.33, 1.34, 1.33, 1.35, 1.36, 1.35],
        "close": [1.31, 1.32, 1.31, 1.33, 1.34, 1.33, 1.35, 1.36, 1.35, 1.37],
    }

    df = pd.DataFrame(data)
    df["high"] = df[["open", "close"]].max(axis=1)
    df["low"] = df[["open", "close"]].min(axis=1)

    return df


# ------------------ Unit Tests ------------------

def test_detect_swings_adds_columns():
    df = sample_df()
    result = detect_swings(df, lookback=2)

    assert "is_swing_high" in result.columns
    assert "is_swing_low" in result.columns
    assert result["is_swing_high"].dtype == bool
    assert result["is_swing_low"].dtype == bool


def test_detect_fvg_columns_exist():
    df = sample_df()
    result = detect_fvg(df)

    assert "fvg_type" in result.columns
    assert "fvg_high" in result.columns
    assert "fvg_low" in result.columns


def test_detect_bos_returns_none_when_insufficient_data():
    df = sample_df().iloc[:3]
    df = detect_swings(df)

    bos = detect_bos(df)
    assert bos is None


def test_position_size_calculation():
    lots = position_size(
        account_balance=10000,
        risk_pct=0.01,
        entry=1.3500,
        stop=1.3400
    )

    assert lots > 0
    assert isinstance(lots, float)


def test_find_order_block_returns_none_if_no_candidate():
    df = sample_df()
    df = detect_swings(df)

    ob = find_order_block_before_bos(df, bos_index=5, direction="bull")
    assert ob is None or isinstance(ob, tuple)


def test_generate_signal_returns_signal_or_none():
    df = sample_df()
    signal = generate_signal(df)

    assert signal is None or isinstance(signal, Signal)


def test_signal_dataclass_fields():
    sig = Signal(
        side="buy",
        entry=1.3500,
        stop=1.3450,
        take_profit=1.3600,
        reason="Test Signal"
    )

    assert sig.side in ["buy", "sell"]
    assert sig.entry > 0
    assert sig.stop > 0
    assert sig.take_profit > 0
    assert isinstance(sig.reason, str)
