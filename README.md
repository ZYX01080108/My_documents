# My_documents
基于 Python 和 大模型 API 的自动化本地文件处理智能体
项目简介：这是一个具备记忆能力的自主智能体。
核心技术：采用了工具层与调度层解耦的双文件架构（main.py + tools.py）。
技术亮点：使用了 JSON Schema 规范大模型输出，并实现了并行工具调用 (Parallel Tool Calling) 来处理复杂的复合任务。
