# Trustensor: Decentralized Trust Scoring for AI Agents

**Subnet Design Proposal for the [Bittensor Subnet Ideathon 2026](https://www.hackquest.io/hackathons/Bittensor-Subnet-Ideathon)**

---

Trustensor is a Bittensor subnet that creates a decentralized, incentive-driven marketplace for AI agent trust evaluation. Miners compete to build the best trust scoring models. Validators benchmark them against curated ground truth. The result: continuously improving trust scores that feed into ERC-8004 registries, agent marketplaces, DeFi protocols, and wallets.

## How It Works

```
Agent Data Package ──> Miners (trust scoring models) ──> TrustScoreSynapse
                                                              │
Validators (ground truth comparison) <────────────────────────┘
         │
         └──> Yuma Consensus ──> TAO Emissions
```

**Three evaluation layers:**

1. **Static Code Analysis** — scan agent source code for vulnerabilities, permission mismatches, and malicious patterns
2. **Behavioral Analysis** — analyze runtime execution traces, API calls, and resource access patterns
3. **Metadata Verification** — cross-reference declared permissions, author history, and registry records

## Repository Structure

```
├── proposal/
│   └── proposal.md             # Full subnet design proposal (the Ideathon submission)
├── idea/                       # Research notes, market analysis, design thinking
└── trustensor/                 # Placeholder implementation (development begins post-Ideathon)
    ├── neurons/
    │   ├── miner.py
    │   └── validator.py
    ├── protocol/
    │   └── synapse.py
    └── evaluation/
        └── scoring.py
```

## Read the Proposal

The full design is in **[proposal/proposal.md](proposal/proposal.md)** — covering incentive mechanism design, scoring algorithms, commercial model, dTAO economics, competitive analysis, and roadmap.

## Status

Ideathon phase. Implementation in progress.

## Team

**Aby** — Founding Engineer ([GitHub](https://github.com/abynysf/))
