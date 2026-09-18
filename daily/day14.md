Exceptions: catch specific errors when you can take useful action; don't blindly catch Exception.
raise: performs whatever handling/action you need, then rethrows the exception so the failure propagates.
finally: runs after the try/except flow, useful for guaranteed cleanup.
Logging: logger.info(), .warning(), .error() provide structured operational history instead of print().
logging.basicConfig(level=...): controls which severity levels are emitted.
logger = logging.getLogger(__name__): creates/retrieves the logger associated with the current module.
Tracebacks: read from the bottom for the actual error, then upward to see the call chain that led there.
JSON validation: distinguished:
malformed JSON → JSONDecodeError
valid JSON but wrong structure → ValueError
missing required keys → ValueError
Built a realistic order_loader project combining Path → JSON → validation → exceptions → logging.
Tomorrow: Days 19–20 Python data processing, integrated into this project, then pandas afterward.