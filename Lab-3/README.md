# SE Project — Student Club Event Ticketing & Budget Portal

**Aaditya Vijaywargi — SRN: PES1UG24AM003**

Software Engineering lab deliverables: UML design (use-case + component diagrams) and Jira Agile planning for the Student Club Event Ticketing & Budget Portal.

## Contents

| File | Description |
|---|---|
| `Student_Club_Portal_Report.docx` / `.pdf` | Full report — use-case diagram, component diagram, traceability, Jira backlog, sprint/burndown/velocity evidence, gap analysis, reflection. |
| [SVG](../Lab-1/use-case-diagram.svg) / [PNG](../Lab-1/use_case_diagram.png) | UML use-case diagram (actors: Club Lead, Campus Admin). |
| [PDF](../Lab-2/component-diagram.pdf) / [PNG](../Lab-2/component-diagram.png) | UML component diagram (microservices architecture). |
| `jira-screenshots/` | Screenshots from the SCRUM Jira project — backlog, board, timeline, burndown, velocity. |

## Requirement ID map

| Req. ID | Description | Jira Key |
|---|---|---|
| FR-001 | Request Budget Approval (multi-stage workflow) | SCRUM-10 |
| FR-002 | Submit Event Proposal | SCRUM-9 |
| FR-003 | Generate QR Tickets | SCRUM-11 |
| FR-004 | Scan Ticket at Check-in | SCRUM-12 |
| FR-005 | Submit Expense Report & Budget Reconciliation | SCRUM-13 |
| NFR-001 | QR Scanner Latency < 100ms | SCRUM-14 |
| NFR-002 | Encrypted Data & Role-Based Access Control | SCRUM-15 |
| FR-006 *(proposed, not yet in Jira)* | Notify on approval/check-in status changes | — |

See the report's Section 10 for the one gap found (Notification Service has no backlog story yet) and the recommended fix.
