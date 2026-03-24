import os
import logging
from homework_10 import log_event


def read_log():
    if not os.path.exists("login_system.log"):
        return ""
    with open("login_system.log", "r") as f:
        return f.read()


def test_log_success():
    log_event("user1", "success")
    logs = read_log()
    assert "user1" in logs
    assert "success" in logs


def test_log_expired():
    log_event("user2", "expired")
    logs = read_log()
    assert "user2" in logs
    assert "expired" in logs


def test_log_failed():
    log_event("user3", "failed")
    logs = read_log()
    assert "user3" in logs
    assert "failed" in logs


def test_log_unknown_status():
    log_event("user4", "unknown")
    logs = read_log()
    assert "user4" in logs
    assert "unknown" in logs