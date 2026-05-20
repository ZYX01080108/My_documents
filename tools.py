# tools.py
import os

# =================【功能实现区】=================
def save_academic_notes(filename, content):
    """在本地创建一个文本文件并写入内容"""
    base_dir = "D:\\Math_Notes\\" 
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    final_path = os.path.join(base_dir, filename) 
    
    try:
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"【系统通知】成功保存至：{final_path}"
    except Exception as e:
        return f"保存失败: {e}"
# =================【API 配置区】=================
# 把冗长的 JSON 说明书也搬过来，保持主程序的清爽
AGENT_TOOLS_SPEC = [
    {
        "type": "function",
        "function": {
            "name": "save_academic_notes",
            "description": "用于在本地保存文本文件。特别注意：如果用户要求保存多个不同的名词、主题，或者明确要求‘分别创建文件’，你【必须】在当前回合中连续、并行地多次调用此函数，为每个内容单独生成一个文件，绝对不能只合并保存为一个文件！",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "保存的文件名，必须以 .txt 结尾。例如 'topology_notes.txt'。"
                    },
                    "content": {
                        "type": "string",
                        "description": "需要保存的学术笔记、公式或详细文本内容。"
                    }
                },
                "required": ["filename", "content"]
            }
        }
    }
]