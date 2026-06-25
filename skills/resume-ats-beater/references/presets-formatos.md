# Presets de Cargo & Formatos Canônicos

> Referência para auditoria LinkedIn e currículo ATS. Cobre profissionais especializados em geral — não apenas dev.

---

## Presets de Cargo

Cada preset contém: **label**, **role**, **keywords**, **headline_areas**, **headline_tech** (ferramentas/competências).

### Tecnologia

| Label | Headline Canônica |
|---|---|
| `backend-engineer` | Backend Engineer \| APIs, Microservices & Distributed Systems \| Python · Java · Go · PostgreSQL · AWS · Kubernetes |
| `frontend-engineer` | Frontend Engineer \| Web Apps, UX Performance & Design Systems \| React · TypeScript · Next.js · CSS · Performance |
| `fullstack-engineer` | Full Stack Engineer \| Product Engineering, APIs & Full Stack Delivery \| React · Node.js · TypeScript · PostgreSQL · AWS |
| `data-engineer` | Data Engineer \| Data Platform, CDP & Reliability \| GCP · Airflow · BigQuery · Spark · Terraform · dbt |
| `devops-engineer` | DevOps / SRE \| Cloud Infrastructure, Reliability & Platform Ops \| Kubernetes · Terraform · AWS · Docker · CI/CD |
| `mobile-engineer` | Mobile Engineer \| Mobile Apps, Performance & Cross-Platform \| Kotlin · Swift · Flutter · React Native |
| `staff-engineer` | Staff Software Engineer \| Platform Architecture, Scale & Technical Leadership \| System Design · Distributed Systems · Cloud |

### Dados & Analytics

| Label | Headline Canônica |
|---|---|
| `data-scientist` | Data Scientist \| Machine Learning, Statistical Modeling & Business Intelligence \| Python · R · TensorFlow · SQL · Tableau |
| `data-analyst` | Data Analyst \| Business Intelligence, Reporting & Data Visualization \| SQL · Power BI · Tableau · Excel · Python |
| `analytics-engineer` | Analytics Engineer \| Data Modeling, Metrics & Self-Serve Analytics \| dbt · SQL · Looker · BigQuery · Snowflake |

### Marketing & Growth

| Label | Headline Canônica |
|---|---|
| `growth-marketer` | Growth Marketing Manager \| Acquisition, Retention & Experimentation \| Google Ads · Meta Ads · GA4 · HubSpot · A/B Testing |
| `product-marketer` | Product Marketing Manager \| Positioning, Launch Strategy & Sales Enablement \| Messaging · Competitive Intel · Content · GTM |
| `seo-specialist` | SEO Specialist \| Technical SEO, Content Strategy & Link Building \| Ahrefs · Screaming Frog · GSC · GA4 · Schema |

### Finanças & Negócios

| Label | Headline Canônica |
|---|---|
| `financial-analyst` | Financial Analyst \| FP&A, Modeling & Strategic Planning \| Excel · Power BI · SAP · Bloomberg · SQL |
| `product-manager` | Product Manager \| Discovery, Roadmap & Delivery \| Jira · Amplitude · Figma · SQL · OKRs |
| `management-consultant` | Management Consultant \| Strategy, Operations & Digital Transformation \| McKinsey 7S · Lean · Excel · PowerPoint |

### Engenharia & Indústria

| Label | Headline Canônica |
|---|---|
| `mechanical-engineer` | Mechanical Engineer \| Product Design, FEA & Manufacturing \| SolidWorks · AutoCAD · ANSYS · GD&T · Lean Manufacturing |
| `civil-engineer` | Civil Engineer \| Structural Design, Project Management & BIM \| AutoCAD · Revit · SAP2000 · MS Project · BIM 360 |

> **NOTA:** Estes são exemplos. O usuário pode definir qualquer cargo — o agente deve adaptar keywords e sugestões ao contexto fornecido.

---

## Formatos Canônicos

### Headline LinkedIn

**Formato:** `{Posição} | {Áreas de trabalho mais fortes} | {Ferramentas/Competências com ·}`

**Regras:**
- Exatamente 3 blocos separados por `|`
- Bloco 1: cargo/posição (com senioridade quando relevante)
- Bloco 2: áreas de domínio / especialidades
- Bloco 3: ferramentas, tecnologias ou competências-chave separadas por `·`
- Máximo 220 caracteres

**Exemplo:**
```
Senior Data Engineer | Data Platform, CDP & Reliability | GCP · Airflow · BigQuery · Spark · Terraform
```

---

### Bullet de Experiência (LinkedIn)

**Formato:** `Ação + métrica em destaque + ferramentas/tecnologias + impacto para a empresa`

**Regras:**
- ~3 linhas máximo por bullet
- Máximo 5 bullets por experiência
- Iniciar com verbo de ação
- Incluir pelo menos 1 métrica por bullet quando possível

**Exemplo:**
```
Productionized a multi-agent AI remediation platform using Google ADK, FastAPI, LLMs, RAG,
Kubernetes, and GitHub-hosted runbooks, resolving ~70% of recurring low-risk KTLO incidents
across Airflow, Dataproc, BigQuery, and Keboola
```

---

### About LinkedIn

**Modelo narrativo:**
1. Abertura com anos de experiência + foco principal
2. Empresa atual com escala/métricas
3. Áreas de atuação
4. Experiência anterior com provas
5. Lista de domínios/competências/stack no final

**Tamanho:** 1000–2000 caracteres ideal

**Exemplo:**
```
I'm a Senior Data Engineer and Cloud Data Architect with 6+ years of experience focused on
helping create and support scalable, reliable, and governed data platforms across GCP and Azure.

At ShopNova, I work on petabyte-scale data platforms supporting 2,000+ pipelines, 500+
Airflow/Composer DAGs, and large-scale GCP workloads. [...]

My strongest areas are Cloud Data Architecture, Data Engineering, Airflow/Composer, GCP, Azure,
BigQuery, Dataproc, Databricks, PySpark, Terraform, Kubernetes, CDP, Observability, and AI
Automation.
```

---

### Bullet de Currículo (ATS)

**Formato:** `Verbo de ação + resultado quantificado + contexto/ferramenta`

**Regras:**
- 1–2 linhas por bullet
- 4–6 bullets por experiência
- Priorizar impacto mensurável
- Usar verbos de ação fortes (Projetou, Implementou, Reduziu, Automatizou, Liderou, Otimizou)

**Exemplo:**
```
Reduziu tempo de processamento de pipelines em 40% ao migrar jobs Spark para Dataproc Serverless com Terraform
Automatizou 200+ DAGs no Airflow/Composer, eliminando 15h/semana de intervenção manual
```
