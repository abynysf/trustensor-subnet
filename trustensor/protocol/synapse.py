"""
Trustensor Protocol Definitions

Defines the communication protocol between miners and validators:
- AgentDataPackage: what validators send to miners (agent source code, behavior logs, metadata)
- TrustScoreSynapse: what miners return (trust score, classification, flags, reasoning)

See proposal Section 4.2 for full schema.
"""

import bittensor as bt
from typing import List, Optional


class AgentDataPackage(bt.Synapse):
    """Data package sent from validator to miner for trust evaluation."""

    agent_id: str = ""
    source_code: dict = {}       # language, files, dependencies
    behavior_logs: dict = {}     # execution traces, API calls, file system access
    declared_permissions: list = []
    metadata: dict = {}          # framework, version, author, registry

    # TODO: implement full schema


class TrustScoreSynapse(bt.Synapse):
    """Trust evaluation response from miner to validator."""

    agent_id: str = ""
    trust_score: float = 0.0             # 0-100
    classification: str = ""             # benign / suspicious / malicious
    severity: str = ""                   # none / low / medium / high / critical
    flags: List[dict] = []               # specific issues found with evidence
    reasoning: str = ""                  # explanation citing files, lines, patterns

    # TODO: implement full schema
