# InsightOS Requirements

## 1. Project Goal

InsightOS is an autonomous business intelligence system that uses agentic AI, generative AI, tool calling, structured data analysis, and retrieval-augmented generation to investigate business questions and produce evidence-backed insights.

## 2. Functional Requirements

### Data Ingestion
- FR-01: The system shall support CSV file uploads.
- FR-02: The system shall support Excel file uploads.
- FR-03: The system shall detect dataset columns and data types.
- FR-04: The system shall identify missing values and basic data-quality issues.

### Data Analysis
- FR-05: The system shall allow users to ask natural-language questions about uploaded data.
- FR-06: The system shall generate and execute analytical SQL queries.
- FR-07: The system shall perform Python-based statistical analysis when required.
- FR-08: The system shall calculate descriptive statistics and business metrics.
- FR-09: The system shall generate appropriate visualizations.

### Agentic AI
- FR-10: The system shall decompose complex analytical questions into smaller tasks.
- FR-11: The system shall select appropriate tools based on the user request.
- FR-12: The system shall execute multiple analytical steps autonomously.
- FR-13: The system shall support iterative investigation when additional analysis is required.

### RAG and Documents
- FR-14: The system shall support business documents such as PDF reports.
- FR-15: The system shall retrieve relevant information from uploaded documents.
- FR-16: The system shall combine structured dataset findings with document evidence.

### Validation
- FR-17: The system shall validate generated conclusions against available evidence.
- FR-18: The system shall flag unsupported or weak claims.
- FR-19: The system shall retry or re-plan analysis when validation fails.

### Reporting
- FR-20: The system shall generate a final business intelligence report.
- FR-21: The report shall contain key findings, supporting evidence, and recommended actions.
- FR-22: The system shall provide traceability for analytical steps and tool usage.

## 3. Non-Functional Requirements

- NFR-01: API keys and secrets shall not be exposed publicly.
- NFR-02: The system shall log agent actions and tool calls.
- NFR-03: The system shall handle tool failures gracefully.
- NFR-04: Generated claims should be traceable to supporting evidence.
- NFR-05: The backend should use modular, testable components.
- NFR-06: The system should provide clear error messages.
- NFR-07: The application should support future extension to additional agents and tools.
- NFR-08: The system should be deployable using containerized infrastructure.

## 4. Initial MVP Scope

The first version of InsightOS will support:

- CSV dataset ingestion
- Dataset profiling
- Natural-language analytical questions
- SQL-based analysis
- Basic Python statistical analysis
- LLM tool calling
- Evidence-backed responses

RAG, multi-agent orchestration, advanced visualization, critic validation, and the React dashboard will be added in later phases.