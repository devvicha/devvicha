<a name="top"></a>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/header-dark.svg">
  <img alt="Vichaksha Geekiyanage, AI/ML Engineer working on voice AI and computer vision. I build voice agents that speak Sinhala, Tamil and English, WhatsApp AI agents serving 10K+ customers a day, vision systems that measure garments, and ML pipelines that keep retraining themselves." src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/vichaksha-geekiyanage-a3b293227/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Vichaksha_Geekiyanage-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://devvicha.github.io/Myportfolio_official/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-devvicha.github.io-24292f?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="mailto:vichakshaviduranga@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-Say_hello-0F766E?style=for-the-badge&logo=gmail&logoColor=white"></a>
</p>

<p align="center">
  <a href="#tour"><kbd>⚡ 60 second tour</kbd></a>&nbsp;
  <a href="#hiring"><kbd>🧭 Hiring for…</kbd></a>&nbsp;
  <a href="#work"><kbd>🛠️ Featured work</kbd></a>&nbsp;
  <a href="#research"><kbd>🔬 Research</kbd></a>&nbsp;
  <a href="#journey"><kbd>📈 Journey</kbd></a>&nbsp;
  <a href="#toolbox"><kbd>🧰 Toolbox</kbd></a>&nbsp;
  <a href="#ask-me"><kbd>💬 Ask me about</kbd></a>
</p>

> [!TIP]
> **Interviewing me?** Read the tour (it really is 60 seconds), use the table to jump to the work closest to your role, then expand any section for the architecture, the decisions behind it and the results. Most of my production code is private; I'm happy to walk through it live.

<a name="tour"></a>
## ⚡ The 60 second tour

**ආයුබෝවන්, I'm Vichaksha.** I'm an AI/ML engineer from Sri Lanka who likes taking models out of notebooks and putting them in front of real people.

- 🤖 **Associate AI/ML Engineer at Surge Robotics** since September 2025.
- 💬 **Production WhatsApp AI agents** serving **10K+ customers a day**. Order taking LLM agents on a NestJS and PostgreSQL platform with idempotent ingestion, Redis backed duplicate guards, SQL audit trails, human takeover and LLM observability with Fiddler AI.
- 🔬 **Low resource speech research.** I adapted Whisper large v2 with LoRA to transcribe Sinhala song lyrics for copyright detection, training only about 1% of its weights. The paper is accepted at **SICET 2026**.
- 👁️ **Computer vision for apparel.** A garment measurement system using YOLOv8 pose keypoints, ChArUco calibration and an MLflow continuous training loop, built with Idea8 (Pvt) Ltd and the University of Sri Jayewardenepura.
- 🎓 **BSc (Hons) in Electronics & Computer Science**, University of Kelaniya, where I also served as Secretary of the IEEE IES Student Branch Chapter.

<a name="hiring"></a>
## 🧭 Hiring for…? Start here

| If the role is | Look at | Ask me about |
|:--|:--|:--|
| 🧠 **AI / ML Engineer** | [Sinhala Lyrical ASR](#asr) · [Garment Measurement](#garment) | Why LoRA instead of full fine tuning, chunking long audio, keypoint design |
| 🤖 **LLM / AI Agent Engineer** | [WhatsApp AI Agents](#whatsapp) · [Voice Agents](#voice) | Keeping the model out of the maths, duplicate order protection, human takeover, Fiddler AI monitoring |
| ⚙️ **MLOps / ML Platform** | [WhatsApp AI Agents](#whatsapp) · [Garment Measurement](#garment) | CI/CD to staging and production, LLM observability, continuous training with MLflow |
| 🎙️ **Voice / Conversational AI** | [Voice Agents](#voice) · [WhatsApp AI Agents](#whatsapp) | Realtime streaming, reconnect strategy, tool calling, Sinhala STT and TTS |
| 👁️ **Computer Vision** | [Garment Measurement](#garment) · [More from the lab](#lab) | Pixel to millimetre calibration, dataset leakage, pose models |
| 🧩 **Backend / Full stack** | [WhatsApp AI Agents](#whatsapp) · [SmartForce HRMS](#hrms) | SQL schema design, idempotency, ledgers, WebSockets, microservices |
| 🔌 **Embedded / IoT** | [Smart Desk Assistant](#smartdesk) · [easyPark](#lab) | ESP32 with FreeRTOS, MQTT over TLS, device provisioning |

<a name="work"></a>
## 🛠️ Featured work

<sub>Click a card to jump to its story. Every story has a collapsible deep dive.</sub>

<p align="center">
<a href="#whatsapp"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/whatsapp-dark.svg"><img alt="Production WhatsApp AI Agents: idempotent ingestion, SQL audit trails, human takeover and LLM monitoring, serving 10K+ customers every day" src="assets/cards/whatsapp-light.svg" width="49%"></picture></a>
<a href="#asr"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/asr-dark.svg"><img alt="Sinhala Lyrical ASR: Whisper large v2 with LoRA for Sinhala songs, 15.7M trainable parameters" src="assets/cards/asr-light.svg" width="49%"></picture></a>
<a href="#garment"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/garment-dark.svg"><img alt="Garment Measurement: pose keypoints and ChArUco calibration with an 18 keypoint skeleton" src="assets/cards/garment-light.svg" width="49%"></picture></a>
<a href="#voice"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/voice-dark.svg"><img alt="Multilingual Voice Agents in Sinhala, Tamil and English" src="assets/cards/voice-light.svg" width="49%"></picture></a>
<a href="#smartdesk"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/smartdesk-dark.svg"><img alt="Smart Desk Assistant: ESP32-S3 node to MQTT, backend, mobile app and AI insights" src="assets/cards/smartdesk-light.svg" width="49%"></picture></a>
<a href="#hrms"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/cards/hrms-dark.svg"><img alt="SmartForce HRMS: 10 Spring Boot microservices" src="assets/cards/hrms-light.svg" width="49%"></picture></a>
</p>

---

<a name="whatsapp"></a>
### 💬 Production WhatsApp AI Agents · built to run, not just to demo

**Role:** end to end owner of the agent, API, database and deployments &nbsp;·&nbsp; **Scale:** 10K+ customers a day &nbsp;·&nbsp; **Code:** private client systems, happy to walk through them live

LLM agents that answer customers, take orders and hand conversations to staff on WhatsApp for Sri Lankan businesses. The chat is the easy part. Behind it sits a multi tenant NestJS platform on PostgreSQL, designed so that retries, double taps and model mistakes never turn into duplicate orders or wrong totals.

| Practice | How I built it | Why it matters |
|:--|:--|:--|
| 🗄️ **Relational data model** | PostgreSQL with Prisma: 25 tables, 16 enums, 50 unique constraints and indexes, 42 versioned migrations including data backfills | Orders, payments and conversations need integrity and history, not a JSON blob |
| 🔁 **Idempotency by design** | Unique `(tenant, wamid)` on messages, `(tenant, external order id)` on orders, unique provider event ids on payments, Redis `SET NX EX` message claims | WhatsApp and payment providers redeliver; a retry must never create a second order or credit |
| 🧱 **Layered duplicate guards** | Message id dedupe, system event filtering, canonical conversation identity, a per chat processing lock and an order confirmation state machine with an in flight guard | Customers double tap, networks retry, and a model can confirm the same order twice |
| 📒 **Ledgers and audit trails** | Append only usage and credit ledgers, order status history with actor, reason and timestamp | Every balance and every status change can be explained later |
| 🧮 **The model talks, code does the maths** | Prices and delivery charges computed by tested code; an immutable chat snapshot is taken at confirmation; the authoritative phone number is passed to the extractor; unknown values are flagged, never guessed | Stops hallucinated totals and cross customer mixups |
| 🔭 **LLM observability** | Fiddler AI monitoring of agent responses, structured logs, escalation flags with a reason | You can't fix what you can't see |
| 🙋 **Human in the loop** | Escalations, takeover windows, unread counts and a realtime staff inbox over Socket.IO with a Redis adapter | Some conversations need a person, fast |
| 🌐 **Resilient integrations** | Timeouts, exponential backoff on 5xx only, no retry on 4xx, a dead letter log for failed payloads, payload validation | Partial failures stay recoverable instead of silently lost |
| ⚡ **Query driven indexing** | Composite indexes shaped by real queries, such as tenant + status + placed date for revenue analytics | Dashboards stay fast as order history grows |
| 🔐 **Security and tenancy** | JWT for staff, API keys for machine clients, per tenant capability guards, presigned URLs for private media on S3 compatible storage | Tenants and features stay separated |
| ✅ **Tests and delivery** | Jest and node:test suites, including a test that interleaves 100 orders with zero cross customer mixups; Docker images built and deployed by GitHub Actions to staging and production with health checks | Ship often without breaking live chats |

<details>
<summary><b>🔍 Architecture</b></summary>
<br>

```mermaid
flowchart LR
  CUST["💬 Customer on WhatsApp"] --> IN
  subgraph agent["Agent service · Node.js"]
    IN["Message intake<br/>text, images, voice notes"] --> DD["Duplicate guards<br/>Redis SET NX, per chat lock"]
    DD --> LLM["Gemini agent<br/>tools, voice transcription"]
    LLM --> PX["Pricing and validation<br/>tested code"]
  end
  PX -->|"API key, retries, dead letter"| API
  subgraph platform["Platform API · NestJS"]
    API["REST API<br/>JWT, API keys, capability guards"] --> PG[("PostgreSQL<br/>Prisma migrations")]
    API --> RT["Realtime inbox<br/>Socket.IO + Redis adapter"]
    API --> S3[("S3 compatible storage<br/>presigned URLs")]
  end
  RT --> STAFF["🧑‍💼 Staff dashboard<br/>takeover and escalations"]
  LLM -. "responses" .-> FID["Fiddler AI<br/>LLM observability"]
  GHA["GitHub Actions"] -. "Docker build and deploy" .-> platform
```

</details>

<details>
<summary><b>🗄️ Core SQL tables</b></summary>
<br>

A slice of the schema: the tables behind conversations, orders and money.

```mermaid
erDiagram
  TENANT ||--o{ CONVERSATION : has
  CONVERSATION ||--o{ CONVERSATION_MESSAGE : contains
  TENANT ||--o{ CUSTOMER : serves
  TENANT ||--o{ ORDERS : receives
  CUSTOMER |o--o{ ORDERS : places
  ORDERS ||--o{ ORDER_ITEM : lists
  ORDERS ||--o{ ORDER_STATUS_HISTORY : "audited by"
  ORDERS ||--o{ ORDER_ATTACHMENT : "receipts and slips"
  TENANT ||--o{ TENANT_CAPABILITY : enables
  TENANT ||--o{ USAGE_LEDGER : "usage"
  TENANT ||--o{ TOP_UP_CREDIT_LEDGER : "credits"
  CONVERSATION {
    string tenant_id FK
    string wa_id "unique per tenant"
    boolean needs_attention
    datetime takeover_until
    int unread_count
  }
  CONVERSATION_MESSAGE {
    string wamid "unique per tenant, idempotent ingest"
    enum direction
    enum type
    datetime sent_at
  }
  ORDERS {
    string external_order_id "unique per tenant"
    enum channel
    enum status
    datetime placed_at "indexed with tenant and status"
  }
  ORDER_STATUS_HISTORY {
    enum from_status
    enum to_status
    enum actor_type
    string change_reason
  }
  TOP_UP_CREDIT_LEDGER {
    enum entry_type "append only"
    int minutes
    datetime created_at
  }
```

</details>

<details>
<summary><b>🧱 How one message passes the duplicate guards</b></summary>
<br>

```mermaid
flowchart TD
  M["Incoming WhatsApp message"] --> L1{"Message id already<br/>claimed in Redis?"}
  L1 -- yes --> DROP["Drop: redelivery"]
  L1 -- no --> L2{"Channel, newsletter<br/>or system event?"}
  L2 -- yes --> DROP2["Ignore"]
  L2 -- no --> L3["Resolve canonical<br/>conversation identity"]
  L3 --> L4["Per chat processing lock"]
  L4 --> AI["Agent reply and tools"]
  AI --> C{"Order confirmed?"}
  C -- no --> R["Reply to customer"]
  C -- yes --> G{"Submission already<br/>in flight or just placed?"}
  G -- yes --> ASK["Ask before creating<br/>a second order"]
  G -- no --> SNAP["Freeze chat snapshot,<br/>extract, price in code"]
  SNAP --> POST["POST to platform API<br/>unique per tenant order id"]
```

</details>

<a name="asr"></a>
### 🔬 Sinhala Lyrical ASR · Whisper + LoRA for copyright detection

**Context:** final year research, Department of Statistics and Computer Science, University of Kelaniya &nbsp;·&nbsp; **Paper:** *Enhancing Copyright Detection through Lyrics Analysis in Sinhala Song Audio* (SICET 2026) &nbsp;·&nbsp; **Code:** [Whisper-Fine-Tuning-For-Sinhala](https://github.com/devvicha/Whisper-Fine-Tuning-For-Sinhala) · [Fine-Tune-by-vicha](https://github.com/devvicha/Fine-Tune-by-vicha)

Speech models struggle with Sinhala songs: background music, poetic phrasing and stretched pronunciation all get in the way. I adapted Whisper to transcribe lyrics well enough to search and match them for copyright detection. The curve below is plotted straight from the training log in the repo.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/whisper-loss-dark.svg">
  <img alt="Training loss of Whisper large v2 with LoRA on Sinhala song audio, falling from 2.17 to 0.12 over 20,244 steps and 3 epochs" src="assets/whisper-loss-light.svg" width="100%">
</picture>

<details>
<summary><b>🔍 Pipeline and design decisions</b></summary>
<br>

```mermaid
flowchart LR
  A["🎵 Sinhala songs"] --> B["30 s chunks<br/>16 kHz"]
  B --> C["Whisper large v2<br/>+ LoRA adapters"]
  C --> D["Sinhala token forcing<br/>+ repetition control"]
  D --> E["Lyrics text"]
  E --> F[("Elasticsearch<br/>lyrics index")]
  F --> G["Copyright match"]
```

- **LoRA instead of full fine tuning.** Rank 32 adapters (α = 64) on the attention query and value projections train **15.7M parameters, about 1% of the 1.55B model**. It fits on Colab GPUs and keeps Whisper's multilingual ability intact.
- **30 second chunks** match Whisper's input window and turned the song collection into about 54K training clips.
- **Forced Sinhala language token**, so decoding never drifts into another language.
- **Chunking and segmentation logic** to break the repetition loops Whisper falls into on music.
- **Elasticsearch** over the transcribed lyrics for search and copyright detection.

**Stack:** PyTorch · Hugging Face Transformers, PEFT and Datasets · Google Colab · Elasticsearch

</details>

<a name="garment"></a>
### 👁️ Garment Measurement · computer vision that measures clothes

**With:** Idea8 (Pvt) Ltd and the University of Sri Jayewardenepura &nbsp;·&nbsp; **Code:** [Cloth-size-project](https://github.com/devvicha/Cloth-size-project) (public first version) · [Go_Pro_RTMP](https://github.com/devvicha/Go_Pro_RTMP) (camera control and streaming) · production code is private

Garment measurements (chest, shoulder, sleeve, length) are usually taken by hand with a tape. This system reads a garment laid on a green flat lay bed through a camera and returns the measurements in millimetres.

<details>
<summary><b>🔍 Architecture, lessons and results</b></summary>
<br>

```mermaid
flowchart LR
  CAM["📷 GoPro<br/>BLE + Wi-Fi control"] --> APP["PyQt desktop app"]
  APP --> ROI["Garment region<br/>on green flat lay bed"]
  ROI --> KP["YOLOv8 pose<br/>18 keypoint skeleton"]
  CAL["ChArUco calibration"] --> MM["Pixels to millimetres"]
  KP --> MM
  MM --> POM["Measurements<br/>chest, shoulder, sleeve, length"]
  subgraph ct["Continuous training"]
    RF["Roboflow labels"] --> TR["Training runs"]
    TR --> ML["MLflow tracking<br/>self hosted on Cloud Run"]
  end
  ML -. "new weights" .-> KP
```

- **Started simple, then hardened it.** The first version used a 12 keypoint T shirt model and one ArUco marker for scale. The current system uses an 18 keypoint skeleton for long sleeve garments and ChArUco boards for calibration.
- **Debugged the data, not just the model.** I traced failures to a corrupted calibration mesh that broke region detection, different garment types sharing one skeleton, and near duplicate burst frames leaking between train and test splits.
- **Continuous training** with MLflow, self hosted on Cloud Run, so every run is tracked as new labeled data comes in.

**Stack:** Python · Ultralytics YOLOv8 · OpenCV (ArUco, ChArUco) · PyQt · Roboflow · MLflow · Google Cloud Run · Open GoPro SDK

</details>

<a name="voice"></a>
### 🎙️ Multilingual Voice Agents · realtime speech in three languages

A series of realtime voice agents built to learn what actually works for Sinhala, Tamil and English callers.

| Project | What it does | What's interesting |
|:--|:--|:--|
| [Car wash booking agent](https://github.com/devvicha/Prestine_car_wash_Project) | Takes bookings by voice, quotes prices, logs complaints | Gemini Live native audio, live transcripts, tool calls validated by an Express + WebSocket backend that pushes booking events in real time |
| [Banking customer care agent](https://github.com/devvicha/sampath-bank-customer-care5_withRAGEMINI) | Answers product and service questions | RAG over a 40+ document knowledge base with FAISS and generated metadata, Sinhala and Tamil voice mode |
| [Resilient streaming](https://github.com/devvicha/RAG-integrated-calling) | Keeps calls alive on bad networks | Auto reconnect with exponential backoff (1 s to 16 s), a circuit breaker and tool error recovery |
| [Sinhala realtime STT](https://github.com/devvicha/Sinhala-Speech-to-text-gcp-Azure) | Live Sinhala captions and spoken replies | Azure Speech streaming, Sinhala neural TTS, Unicode normalisation |
| [Local live transcription](https://github.com/devvicha/Live_English_Transciptining_Iphone_VScode) | Offline English captions | faster-whisper with int8 on Apple Silicon, short windows with rolling context |

<details>
<summary><b>🔍 How one voice turn works (booking agent)</b></summary>
<br>

```mermaid
sequenceDiagram
  autonumber
  participant C as 🧑 Caller
  participant F as React client
  participant G as Gemini Live
  participant B as Booking API
  C->>F: Speaks in Sinhala, Tamil or English
  F->>G: Streams audio
  G-->>F: Live transcript and a tool call
  F->>B: Validate and save the booking
  B-->>F: Price and booking id
  F->>G: Tool result
  G-->>C: Confirms the booking by voice
  B--)F: WebSocket event for the dashboard
```

**Stack:** React · TypeScript · Vite · Node.js · Express · WebSockets · Gemini Live API · Azure Speech · faster-whisper · FAISS · Streamlit

</details>

<a name="smartdesk"></a>
### 🔌 Smart Desk Assistant · IoT from sensor to app

**Code:** [SmartDeskAssistant](https://github.com/devvicha/SmartDeskAssistant)

A desk node measures air quality, noise and light, and the app turns those readings into insights about the workspace.

<details>
<summary><b>🔍 System design</b></summary>
<br>

```mermaid
flowchart LR
  subgraph node["ESP32-S3 node · FreeRTOS"]
    S1["Gas and air quality"] --> FW["Firmware<br/>C, ESP-IDF"]
    S2["Noise"] --> FW
    S3["Light"] --> FW
  end
  PROV["Wi-Fi provisioning portal<br/>AP mode"] -.-> FW
  FW -->|"MQTT over TLS"| BR["Cloud MQTT broker"]
  BR --> API["Node.js + Express API<br/>PostgreSQL, JWT"]
  API --> APP["📱 Expo React Native app"]
  API --> AI["AI insights engine"]
```

- **Firmware:** FreeRTOS tasks on an ESP32-S3, a provisioning portal for Wi-Fi setup and credentials kept in NVS.
- **Backend:** TypeScript, Express and PostgreSQL with JWT auth for users, devices and readings.
- **Documented like a real system,** with concept maps and rich pictures before any code.

</details>

<a name="hrms"></a>
### 🧩 SmartForce HRMS · Spring Boot microservices

**Code:** [HR-Management-System](https://github.com/devvicha/HR-Management-System)

An HR platform split into 10 independent Spring Boot services backed by MongoDB: employees, departments, payroll, leave, attendance, assets, projects, tasks, to do lists and notices. Each service owns its domain and exposes its own REST API.

<a name="lab"></a>
### 🧪 More from the lab

| Project | What it is | Stack |
|:--|:--|:--|
| [Video SpO2 estimation](https://github.com/devvicha/Opensource_Research) | Contactless blood oxygen estimate from facial video: PPG signals from face regions go into a tiny transformer (4 layers, 2 heads) served with FastAPI | PyTorch · OpenCV · FastAPI |
| [Kite skeletonization](https://github.com/devvicha/Kite_Project) | U²Net segmentation with a learnable thinning layer and Focal Tversky loss to extract kite skeletons | PyTorch · Albumentations |
| [Sign language detection](https://github.com/devvicha/SignLanguageDetection) | Real time sign detection with YOLOv8, exported to ONNX and served with Flask | YOLOv8 · ONNX · Flask |
| [easyPark](https://github.com/devvicha/easyPark) | IoT parking: sensors and a NodeMCU ESP32 update Firebase in real time, and the app guides drivers to free spots | Arduino · Firebase · Google Maps |
| [GoPro control and RTMP](https://github.com/devvicha/Go_Pro_RTMP) | Controls a GoPro from macOS over BLE and Wi-Fi, then live streams it to a backend over RTMP | Open GoPro SDK · Python |
| [House value prediction](https://github.com/devvicha/House-Value-Prediction-System-using-linear-Algebra) | House price model built from linear algebra fundamentals | NumPy · Jupyter |

<a name="research"></a>
## 🔬 Research and publications

- 📄 **Enhancing Copyright Detection through Lyrics Analysis in Sinhala Song Audio**, SICET 2026. Sinhala lyrical ASR with Whisper + LoRA and lyrics matching with Elasticsearch. [Details ↑](#asr)
- 🎓 Final year research in the Department of Statistics and Computer Science, University of Kelaniya.
- 🩺 Open research prototype: [contactless SpO2 estimation from facial video](https://github.com/devvicha/Opensource_Research).

<a name="journey"></a>
## 📈 Journey

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/devvicha/devvicha/main/assets/journey-dark.svg">
  <img alt="Journey. 2020 to 2022: A/L Physical Science at Nalanda College, People's Bank teller and admin, speaker on ML and automation. 2023: easyPark IoT parking, sign language detection, AIESEC team lead. 2024: IEEE IES Secretary at University of Kelaniya, Robot Battle coordinator, Sinhala ASR research starts. 2025: joined Surge Robotics as Associate AI/ML Engineer, voice and WhatsApp agents. 2026: production WhatsApp AI agents, SICET 2026 paper, IEEE GenAI Challenge talk, BSc (Hons) completed." src="assets/journey-light.svg" width="100%">
</picture>

<a name="toolbox"></a>
## 🧰 Toolbox

<sub>Grouped by what I use them for.</sub>

| Area | Tools |
|:--|:--|
| **ML and deep learning** | <img src="https://skillicons.dev/icons?i=py,pytorch,tensorflow,sklearn,opencv" height="34" alt="Python, PyTorch, TensorFlow, scikit-learn, OpenCV"><br>Hugging Face Transformers · PEFT / LoRA · Ultralytics YOLOv8 · Roboflow |
| **Speech and LLMs** | Whisper and faster-whisper · Gemini Live · Azure Speech · LangChain · RAG with Qdrant, FAISS and Elasticsearch |
| **MLOps and cloud** | <img src="https://skillicons.dev/icons?i=gcp,docker,terraform,azure,linux" height="34" alt="Google Cloud, Docker, Terraform, Azure, Linux"><br>Cloud Run · Vertex AI · MLflow |
| **Backend and data** | <img src="https://skillicons.dev/icons?i=nodejs,express,fastapi,flask,spring,postgres,mongodb,mysql,firebase,elasticsearch" height="34" alt="Node.js, Express, FastAPI, Flask, Spring, PostgreSQL, MongoDB, MySQL, Firebase, Elasticsearch"><br>WebSockets · REST · async webhooks |
| **Frontend and mobile** | <img src="https://skillicons.dev/icons?i=react,ts,js,vite,tailwind" height="34" alt="React, TypeScript, JavaScript, Vite, Tailwind CSS"><br>Expo React Native · PyQt · Streamlit |
| **Embedded and IoT** | <img src="https://skillicons.dev/icons?i=arduino,c,java" height="34" alt="Arduino, C, Java"><br>ESP32 · FreeRTOS · MQTT · NodeMCU |

## 🎤 Leadership and speaking

- 🎙️ **Guest speaker**, IEEE IES Generative AI Challenge 2026 introductory session (February 2026)
- 🗂️ **Secretary**, IEEE Industrial Electronics Society Student Branch Chapter, University of Kelaniya (2024): events and workshops for 100+ students
- 🤖 **Coordinator**, IEEE Robot Battle at the University of Kelaniya (2024): 200+ participants, sponsorships secured
- 🌍 **Team lead**, AIESEC IGV charity project (2023)
- 🎤 **Webinar speaker**, ECSC TechnoSymphony on machine learning and industrial automation (2022): 100+ attendees
- 🤝 Regular at **AICSL** AI community meetups in Sri Lanka

<a name="ask-me"></a>
## 💬 Questions I'd love to be asked

<sub>Short answers here. The long versions make good interview conversations.</sub>

<details>
<summary><b>How do you make Whisper work on Sinhala songs without retraining all of it?</b></summary>
<br>

LoRA adapters (rank 32) on the attention query and value projections of Whisper large v2, so only 15.7M of 1.55B parameters train. Songs are cut into 30 second chunks to match Whisper's window, the Sinhala language token is forced at decode time, and segmentation logic stops the repetition loops that music causes. [Full story ↑](#asr)

</details>

<details>
<summary><b>How do you stop a WhatsApp agent from creating duplicate orders?</b></summary>
<br>

With layers, because duplicates come from different places. Redeliveries are caught by claiming each message id in Redis with `SET NX EX`, which survives restarts. Double taps and parallel messages are serialised by a per chat lock. A model confirming twice is caught by an order state machine that blocks a second submission while one is in flight or was just placed, and asks the customer instead. Finally, the database enforces a unique order id per tenant, so even a bug upstream can't write the same order twice. [Full story ↑](#whatsapp)

</details>

<details>
<summary><b>How do you monitor an LLM agent in production?</b></summary>
<br>

Agent responses are monitored with Fiddler AI, alongside structured logs. Conversations that need a person are flagged with a reason and surface in a realtime staff inbox, where staff can take over for a set window. Failed outbound payloads go to a dead letter log instead of disappearing, so nothing is silently lost. [Full story ↑](#whatsapp)

</details>

<details>
<summary><b>Why not let the LLM calculate prices?</b></summary>
<br>

Because it will eventually be confidently wrong. The model handles the conversation; prices and delivery charges come from tested code, and anything the code can't determine is flagged instead of guessed. The order is extracted from an immutable snapshot of the chat taken at confirmation, with the customer's real phone number passed in, so new messages or a hallucinated number can't leak into it. [Full story ↑](#whatsapp)

</details>

<details>
<summary><b>How do you keep a realtime voice call alive on a bad network?</b></summary>
<br>

Each kind of failure gets its own response. Transient drops reconnect automatically with exponential backoff (1, 2, 4, 8, 16 seconds). Repeated failures trip a circuit breaker so the client stops hammering the server. A failing tool returns an error to the model instead of killing the stream, so the conversation carries on. [Code](https://github.com/devvicha/RAG-integrated-calling)

</details>

<details>
<summary><b>What broke in the garment pipeline, and how did you find it?</b></summary>
<br>

Three things, none of them the model architecture: a corrupted calibration mesh file that broke region detection, different garment types forced into one keypoint skeleton, and near duplicate burst frames that leaked between train and test splits and made results look better than they were. The lesson I took away: audit the data pipeline before tuning the model. [Full story ↑](#garment)

</details>

<details>
<summary><b>How do your models keep improving after launch?</b></summary>
<br>

For garment measurement, a continuous training loop with MLflow self hosted on Cloud Run tracks every run as new labeled data arrives from Roboflow. For the WhatsApp agents, I'm experimenting with MLflow prompt optimization to improve prompts systematically instead of by hand.

</details>

## 📫 Let's talk

I'm always happy to talk about production LLM agents, voice AI for low resource languages and computer vision in manufacturing.

**[LinkedIn](https://www.linkedin.com/in/vichaksha-geekiyanage-a3b293227/)** · **[Portfolio](https://devvicha.github.io/Myportfolio_official/)** · **[Email](mailto:vichakshaviduranga@gmail.com)**

<p align="center"><a href="#top">⬆ Back to top</a></p>
<p align="center"><sub>The header, cards, timeline and loss chart are SVGs generated from my own project data by <a href="scripts/gen_assets.py">scripts/gen_assets.py</a>.</sub></p>
