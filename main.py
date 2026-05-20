# main.py
import json
from openai import OpenAI

# 【核心魔法】：从你刚刚建的 tools.py 里，把函数和说明书“借”过来！
from tools import save_academic_notes, AGENT_TOOLS_SPEC

client = OpenAI(
    api_key="sk-7bc0d08c5f86485597e1832b5e6f0f70",  # 请填入新Key
    base_url="https://api.deepseek.com"
)

messages_history = [
    {"role": "system", "content": "你是一个严谨的学术助手。请用中文回答问题，遇到专业术语请给出英文对照。"}
]

print("====================================")
print(" 模块化智能体 Agent (V2.0) 已上线！")
print("====================================\n")

while True:
    user_input = input("你: ")
    if user_input == "退出":
        print("Agent: 再见！")
        break
        
    messages_history.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages_history,
            tools=AGENT_TOOLS_SPEC, # 直接使用从 tools.py 导入的说明书
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        
        if response_message.tool_calls:
            call_count = len(response_message.tool_calls)
            print(f"\n🤖 [Agent 思考]: 检测到 {call_count} 个自动化任务，正在执行...")
            messages_history.append(response_message)
            
            for tool_call in response_message.tool_calls:
                # 路由判断：如果是 save_academic_notes 这个动作
                if tool_call.function.name == "save_academic_notes":
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # 直接调用从 tools.py 导入的函数
                    tool_output = save_academic_notes(
                        filename=function_args.get("filename", "default.txt"),
                        content=function_args.get("content", "")
                    )
                    
                    print(tool_output) 
                    messages_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_output
                    })
                    
            final_response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages_history
            )
            print(f"\nAgent: {final_response.choices[0].message.content}\n")
            
        else:
            agent_answer = response_message.content
            print(f"\nAgent: {agent_answer}\n")
            messages_history.append({"role": "assistant", "content": agent_answer})
            
    except Exception as e:
        print(f"\n运行错误: {e}\n")