import os
import sys
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

# =====================================================================
# STEP 1: TẢI BIẾN MÔI TRƯỜNG TỪ FILE .ENV & CẤU HÌNH MODEL
# =====================================================================
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL   = os.getenv("GROQ_MODEL")

if not GROQ_API_KEY or not GROQ_MODEL:
    print("❌ Lỗi: Cấu hình .env chưa đầy đủ.")
    sys.exit(1)

client = Groq(api_key=GROQ_API_KEY)

# =====================================================================
# STEP 2: AUDIT LOGGER — CAPTURE TOÀN BỘ STDOUT VÀO FILE LOG
# =====================================================================
class AuditLogger:
    def __init__(self, log_file):
        self.terminal = sys.stdout
        self.log = open(log_file, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def stop(self):
        sys.stdout = self.terminal
        self.log.close()

# =====================================================================
# STEP 3: HÀM GỌI AGENT (1 LỜI GỌI GROQ API)
# =====================================================================
def run_agent(agent_name, system_prompt, user_prompt):
    print(f"\n{'='*60}")
    print(f"🤖 [{agent_name}] đang xử lý...")
    print(f"{'='*60}")

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ],
        temperature=0.2
    )

    result = response.choices[0].message.content
    print(result)
    return result

# =====================================================================
# STEP 4: DYNAMIC SKILL LOADER (CƠ CHẾ NẠP SKILL TỪ FILE MARKDOWN)
# =====================================================================
def load_skill_instruction(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Lỗi vật lý: Không tìm thấy tệp tin Skill tại {file_path}")
        sys.exit(1)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Thực hiện nạp động toàn bộ luật Instruction từ thư mục vào hệ thống
try:
    AGENT_1_SYSTEM = load_skill_instruction("agent_skills/agent_1_spec_analyst.md")
    AGENT_2_SYSTEM = load_skill_instruction("agent_skills/agent_2_domain_testing.md")
    AGENT_3_SYSTEM = load_skill_instruction("agent_skills/agent_3_bva.md")
    AGENT_4_SYSTEM = load_skill_instruction("agent_skills/agent_4_report_writer.md")
except Exception as e:
    print(f"❌ Lỗi trong quá trình nạp tệp cấu hình Skill: {str(e)}")
    sys.exit(1)

# =====================================================================
# STEP 5: HÀM XUẤT AI AUDIT REPORT CHUẨN KIỂM TOÁN DỮ LIỆU
# =====================================================================
def generate_ai_audit_report(raw_spec, agent_outputs, final_report):
    report_file = "AI_Audit_Report.md"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(report_file):
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("# AI AUDIT REPORT\n\n")
        entry_number = 1
    else:
        with open(report_file, "r", encoding="utf-8") as f:
            content = f.read()
        entry_number = content.count("## Entry") + 1

    fence = "```"
    entry_content = f"""
---

## Entry {entry_number}

### AI tool name
* {GROQ_MODEL} (via Groq API — 4-Agent Pipeline with Decoupled Skills)

### Date and time
* {current_time}

### Prompt
#### [Input Feature Specification]
{fence}text
{raw_spec.strip()}
{fence}

#### [Agent 1 System Prompt — Spec Analyst]
{fence}text
{AGENT_1_SYSTEM.strip()}
{fence}

#### [Agent 2 System Prompt — Domain Testing]
{fence}text
{AGENT_2_SYSTEM.strip()}
{fence}

#### [Agent 3 System Prompt — BVA]
{fence}text
{AGENT_3_SYSTEM.strip()}
{fence}

#### [Agent 4 System Prompt — Report Writer]
{fence}text
{AGENT_4_SYSTEM.strip()}
{fence}

### The AI output

**[Agent 1 — Spec Analysis]**
{agent_outputs['agent1']}

**[Agent 2 — Domain Testing]**
{agent_outputs['agent2']}

**[Agent 3 — BVA]**
{agent_outputs['agent3']}

**[Final Delivered Artifact]**
{final_report}

"""
    with open(report_file, "a", encoding="utf-8") as f:
        f.write(entry_content)

    if os.path.exists("groq_internal.log"):
        os.remove("groq_internal.log")

# =====================================================================
# STEP 6: LUỒNG CHẠY THỰC TẾ
# =====================================================================
if __name__ == "__main__":
    logger = AuditLogger("groq_internal.log")
    sys.stdout = logger

    # Load spec từ file riêng
    input_specification = load_skill_instruction("input_spec.md")

    print("🚀 4-Agent Pipeline khởi động... Vui lòng đợi.")

    # Agent 1: Phân tích spec
    analysis = run_agent(
        agent_name="Agent 1 — Spec Analyst",
        system_prompt=AGENT_1_SYSTEM,
        user_prompt=f"Hãy phân tích spec sau:\n\n{input_specification}"
    )

    # Agent 2 & 3: Chạy song song (Domain Testing & BVA dùng chung analysis)
    # Nếu muốn sequential thì gọi tuần tự như dưới
    domain_tests = run_agent(
        agent_name="Agent 2 — Domain Testing",
        system_prompt=AGENT_2_SYSTEM,
        user_prompt=f"Kết quả phân tích spec:\n\n{analysis}"
    )

    bva_tests = run_agent(
        agent_name="Agent 3 — BVA",
        system_prompt=AGENT_3_SYSTEM,
        user_prompt=f"Kết quả phân tích spec:\n\n{analysis}"
    )

    # Agent 4: Tổng hợp báo cáo cuối
    final_report = run_agent(
        agent_name="Agent 4 — Report Writer",
        system_prompt=AGENT_4_SYSTEM,
        user_prompt=f"## Domain Testing\n\n{domain_tests}\n\n## BVA\n\n{bva_tests}"
    )

    # Lưu file test cases thô
    with open("Temporary_Feature_Output.md", "w", encoding="utf-8") as f:
        f.write(final_report)

    print("\n✅ ĐÃ HOÀN THÀNH NGON LÀNH!")
    print("- Báo cáo test case đã lưu tại: Temporary_Feature_Output.md")
    print("- Audit log đã xuất tại: AI_Audit_Report.md")

    logger.stop()

    # Kích hoạt hàm ghi nhận Audit Report với đầy đủ hệ thống Prompt đã custom
    generate_ai_audit_report(
        raw_spec=input_specification,
        agent_outputs={
            'agent1': analysis,
            'agent2': domain_tests,
            'agent3': bva_tests
        },
        final_report=final_report
    )

    